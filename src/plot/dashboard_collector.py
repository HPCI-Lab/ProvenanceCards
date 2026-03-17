import argparse
import warnings
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
from matplotlib.backends.backend_pdf import PdfPages

warnings.filterwarnings("ignore")

# ── CLI ───────────────────────────────────────────────────────────────────────
parser = argparse.ArgumentParser()
parser.add_argument("--csv", default="results.csv")
parser.add_argument("--out", default="dashboard_collector.pdf")
args = parser.parse_args()

# ── Palette ───────────────────────────────────────────────────────────────────
PALETTE = {"yprov": "#4C72B0", "flowcept": "#DD8452"}
BG      = "#F7F8FA"

DATASET_LABELS = {
    "example":           "Example",
    "fusion":            "Fusion",
    "nasa":              "NASA",
    "train_test_splits": "Train/Test",
    "turbolence":        "Turbulence",
}

# ── Load & enrich ─────────────────────────────────────────────────────────────
df = pd.read_csv(args.csv)
df["schema"]  = df["file"].apply(
    lambda x: "yprov" if ("_Y.json" in x or "_Y.md" in x or "_Y.jsonl" in x) else "flowcept"
)
df["format"]  = df["file"].apply(lambda x: "card" if "/cards/" in x else "json")
df["dataset"] = (
    df["file"]
    .apply(lambda x: x.split("/")[-1].split("__")[0])
    .str.replace(r"(_F|_Y)\.(jsonl|json|md)$", "", regex=True)
)

schemas   = ["yprov", "flowcept"]
schema_df = {s: df[df["schema"] == s] for s in schemas}

# ── Metric catalogue ──────────────────────────────────────────────────────────
# (column, display_label, ylim_or_None, higher_is_better)
METRICS = [
    ("absolute_factual_coverage_score",  "Abs. Coverage Score",     (0, 1),    True),
    ("relative_factual_coverage_score",  "Rel. Coverage Score",     (0, 1),    True),
    ("relative_factual_coverage_f1",     "Rel. Coverage F1",        (0, 1),    True),
    ("hallucination_rate",               "Hallucination Rate",      (0, 1),    False),
    ("rouge_l_f1",                       "ROUGE-L F1",              (0, 0.2),  True),
    ("semantic_mean_sim",                "Semantic Consistency",    (0, 1),    True),
    ("bleu",                             "BLEU Score",              (0, 0.015),True),
    ("tokens_for_coverage",              "Tokens for Coverage",     None,      False),
    ("total_words",                      "Output Length (words)",   None,      True),
]

# ── Helpers ───────────────────────────────────────────────────────────────────
def style_ax(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linewidth=0.5, alpha=0.5)
    ax.set_axisbelow(True)


def simple_bar(ax, metric, title, ylabel, ylim=None):
    """Two bars: yprov vs flowcept with 95% CI error bars."""
    means = [schema_df[s][metric].mean() for s in schemas]
    errs  = [1.96 * schema_df[s][metric].sem() for s in schemas]
    x     = np.arange(2)
    bars  = ax.bar(x, means, color=[PALETTE[s] for s in schemas], width=0.5,
                   yerr=errs, capsize=5, error_kw=dict(elinewidth=1.2, ecolor="#555"),
                   zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels(["yProv", "FlowCept"], fontsize=10)
    ax.set_title(title, fontsize=10, fontweight="bold", pad=6)
    ax.set_ylabel(ylabel, fontsize=8)
    if ylim:
        ax.set_ylim(ylim)
    style_ax(ax)
    for bar, m in zip(bars, means):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + (ylim[1] * 0.02 if ylim else m * 0.03),
                f"{m:.4f}", ha="center", va="bottom", fontsize=8)


def per_dataset_delta(ax, metric, title, ylabel, ylim=None, higher_is_better=True):
    """
    Grouped bars per dataset (yprov vs flowcept) with delta annotation.
    Arrow is green when yprov > flowcept and higher_is_better, red otherwise.
    """
    datasets = sorted(df["dataset"].unique())
    x        = np.arange(len(datasets))
    w        = 0.35

    yp_vals = [schema_df["yprov"][schema_df["yprov"]["dataset"] == d][metric].mean()
               for d in datasets]
    fc_vals = [schema_df["flowcept"][schema_df["flowcept"]["dataset"] == d][metric].mean()
               for d in datasets]

    ax.bar(x - w / 2, yp_vals, w, color=PALETTE["yprov"],    label="yProv",    zorder=3)
    ax.bar(x + w / 2, fc_vals, w, color=PALETTE["flowcept"], label="FlowCept", zorder=3)

    for xi, (yv, fv) in enumerate(zip(yp_vals, fc_vals)):
        delta     = yv - fv
        positive  = (delta > 0) == higher_is_better
        col       = "#2ca02c" if positive else "#d62728"
        sym       = "▲" if delta > 0 else "▼"
        ref_top   = max(yv, fv)
        pad       = (ylim[1] * 0.04) if ylim else (ref_top * 0.06 + 1e-6)
        ax.text(xi, ref_top + pad, f"{sym}{abs(delta):.3f}",
                ha="center", va="bottom", fontsize=6.5, color=col, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels([DATASET_LABELS.get(d, d) for d in datasets], fontsize=8)
    ax.set_title(title, fontsize=10, fontweight="bold", pad=6)
    ax.set_ylabel(ylabel, fontsize=8)
    if ylim:
        ax.set_ylim(ylim)
    style_ax(ax)
    ax.legend(fontsize=8, framealpha=0.8)


def radar_chart(ax, metrics_radar):
    """Radar with min=-0.1, normalised 0–1 across both schemas."""
    cats   = [m[1] for m in metrics_radar]
    cols   = [m[0] for m in metrics_radar]
    N      = len(cats)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), cats, fontsize=8)
    ax.set_rmin(-0.1)

    all_vals = np.array([[schema_df[s][c].mean() for c in cols] for s in schemas])
    col_min  = all_vals.min(axis=0)
    col_rng  = np.where(all_vals.max(axis=0) - col_min > 0,
                        all_vals.max(axis=0) - col_min, 1)

    for s, color in PALETTE.items():
        raw    = np.array([schema_df[s][c].mean() for c in cols])
        normed = (raw - col_min) / col_rng
        vals   = normed.tolist() + normed[:1].tolist()
        ax.plot(angles, vals, color=color, linewidth=2)
        ax.fill(angles, vals, color=color, alpha=0.15)

    patches = [mpatches.Patch(color=PALETTE[s], label=s.capitalize()) for s in schemas]
    ax.legend(handles=patches, loc="upper right",
              bbox_to_anchor=(1.4, 1.15), fontsize=9, framealpha=0.8)
    ax.set_title("Multi-Metric Radar\n(normalised, min=−0.1)", fontsize=10,
                 fontweight="bold", pad=20)


def heatmap(ax, metric, title):
    datasets = sorted(df["dataset"].unique())
    mat      = np.array([[schema_df[s][schema_df[s]["dataset"] == d][metric].mean()
                          for d in datasets] for s in schemas])
    vmax     = 1 if mat.max() <= 1 else None
    im       = ax.imshow(mat, cmap="RdYlGn", aspect="auto", vmin=0, vmax=vmax)
    ax.set_xticks(range(len(datasets)))
    ax.set_xticklabels([DATASET_LABELS.get(d, d) for d in datasets], fontsize=8)
    ax.set_yticks(range(2))
    ax.set_yticklabels(["yProv", "FlowCept"], fontsize=9)
    ax.set_title(title, fontsize=10, fontweight="bold", pad=6)
    for i in range(2):
        for j, d in enumerate(datasets):
            v = mat[i, j]
            if not np.isnan(v):
                ax.text(j, i, f"{v:.3f}", ha="center", va="center", fontsize=8,
                        fontweight="bold", color="white" if v < 0.35 else "black")
    plt.colorbar(im, ax=ax, fraction=0.04, pad=0.03)


# ── Build PDF ─────────────────────────────────────────────────────────────────
with PdfPages(args.out) as pdf:

    # ── Page 1: Overall comparison ────────────────────────────────────────────
    fig = plt.figure(figsize=(22, 26))
    fig.patch.set_facecolor(BG)
    fig.text(0.5, 0.977, "Collector Comparison: yProv vs FlowCept",
             ha="center", fontsize=18, fontweight="bold", color="#1a1a2e")
    fig.text(0.5, 0.966, "Aggregated across all datasets and formats",
             ha="center", fontsize=10, color="#555")

    gs = gridspec.GridSpec(3, 3, figure=fig,
                           top=0.955, bottom=0.04,
                           left=0.06, right=0.97,
                           hspace=0.5, wspace=0.38)

    plot_order = [
        ("absolute_factual_coverage_score", "Abs. Coverage Score",    (0, 1)),
        ("relative_factual_coverage_score", "Rel. Coverage Score",    (0, 1)),
        ("relative_factual_coverage_f1",    "Rel. Coverage F1",       (0, 1)),
        ("hallucination_rate",              "Hallucination Rate",     (0, 1)),
        ("rouge_l_f1",                      "ROUGE-L F1",             (0, 0.2)),
        ("semantic_mean_sim",               "Semantic Consistency",   (0, 1)),
        ("bleu",                            "BLEU Score",             (0, 0.015)),
        ("tokens_for_coverage",             "Tokens for Coverage",    None),
        ("total_words",                     "Output Length (words)",  None),
    ]

    for idx, (col, label, ylim) in enumerate(plot_order):
        r, c = divmod(idx, 3)
        ax = fig.add_subplot(gs[r, c])
        if col in df.columns:
            simple_bar(ax, col, label, label, ylim)
        else:
            ax.set_title(f"{label}\n(column missing)", fontsize=9, color="grey")
            style_ax(ax)

    pdf.savefig(fig, bbox_inches="tight", facecolor=BG)
    plt.close(fig)

    # ── Page 2: Per-dataset delta ─────────────────────────────────────────────
    fig2 = plt.figure(figsize=(22, 26))
    fig2.patch.set_facecolor(BG)
    fig2.text(0.5, 0.977, "yProv vs FlowCept — Delta per Dataset",
              ha="center", fontsize=18, fontweight="bold", color="#1a1a2e")
    fig2.text(0.5, 0.966,
              "▲/▼ shows yProv − FlowCept  •  green = yProv better, red = FlowCept better",
              ha="center", fontsize=10, color="#555")

    gs2 = gridspec.GridSpec(3, 3, figure=fig2,
                            top=0.955, bottom=0.04,
                            left=0.06, right=0.97,
                            hspace=0.5, wspace=0.38)

    for idx, (col, label, ylim, hib) in enumerate(METRICS):
        r, c = divmod(idx, 3)
        ax = fig2.add_subplot(gs2[r, c])
        if col in df.columns:
            per_dataset_delta(ax, col, label, label, ylim, hib)
        else:
            ax.set_title(f"{label}\n(column missing)", fontsize=9, color="grey")
            style_ax(ax)

    pdf.savefig(fig2, bbox_inches="tight", facecolor=BG)
    plt.close(fig2)

    # ── Page 3: Radar + Heatmaps ──────────────────────────────────────────────
    fig3 = plt.figure(figsize=(22, 14))
    fig3.patch.set_facecolor(BG)
    fig3.text(0.5, 0.97, "yProv vs FlowCept — Radar & Heatmaps",
              ha="center", fontsize=16, fontweight="bold", color="#1a1a2e")

    gs3 = gridspec.GridSpec(1, 3, figure=fig3,
                            top=0.90, bottom=0.08,
                            left=0.05, right=0.97,
                            wspace=0.4)

    radar_metrics = [
        ("absolute_factual_coverage_score", "Abs. Coverage"),
        ("relative_factual_coverage_f1",    "Rel. Coverage F1"),
        ("rouge_l_f1",                      "ROUGE-L F1"),
        ("semantic_mean_sim",               "Semantic Sim"),
        ("bleu",                            "BLEU"),
        ("hallucination_rate",              "Hallucination"),
    ]
    radar_metrics = [(c, l) for c, l in radar_metrics if c in df.columns]

    ax_radar = fig3.add_subplot(gs3[0, 0], polar=True)
    radar_chart(ax_radar, radar_metrics)

    ax_h1 = fig3.add_subplot(gs3[0, 1])
    if "absolute_factual_coverage_score" in df.columns:
        heatmap(ax_h1, "absolute_factual_coverage_score", "Abs. Coverage Heatmap")

    ax_h2 = fig3.add_subplot(gs3[0, 2])
    if "hallucination_rate" in df.columns:
        heatmap(ax_h2, "hallucination_rate", "Hallucination Rate Heatmap")

    pdf.savefig(fig3, bbox_inches="tight", facecolor=BG)
    plt.close(fig3)

    meta = pdf.infodict()
    meta["Title"] = "Collector Comparison Dashboard"

print(f"✅  Saved → {args.out}")
