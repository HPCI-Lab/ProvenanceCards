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
parser.add_argument("--csv", default="results_cards.csv")
parser.add_argument("--out", default="dashboard_models.pdf")
args = parser.parse_args()

# ── Palette — one colour per model ───────────────────────────────────────────
MODEL_COLORS = {
    "Llama-3.2-3B":     "#4C72B0",
    "Mistral-7B-v0.3":  "#DD8452",
    "Phi-4-Mini":       "#55A868",
    "Qwen2.5-Coder-7B": "#C44E52",
}
BG = "#F7F8FA"

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
df["dataset"] = (
    df["file"]
    .apply(lambda x: x.split("/")[-1].split("__")[0])
    .str.replace(r"(_F|_Y)\.(jsonl|json|md)$", "", regex=True)
)

MODELS   = list(df["model"].unique())
COLORS   = [MODEL_COLORS.get(m, f"C{i}") for i, m in enumerate(MODELS)]
DATASETS = sorted(df["dataset"].unique())

model_df = {m: df[df["model"] == m] for m in MODELS}

# ── Metric catalogue  (col, label, ylim, higher_is_better) ───────────────────
METRICS = [
    ("absolute_factual_coverage_score", "Abs. Coverage Score",   (0, 1),     True),
    ("relative_factual_coverage_score", "Rel. Coverage Score",   (0, 1),     True),
    ("relative_factual_coverage_f1",    "Rel. Coverage F1",      (0, 1),     True),
    ("hallucination_rate",              "Hallucination Rate",    (0, 1),     False),
    ("rouge_l_f1",                      "ROUGE-L F1",            (0, 0.2),   True),
    ("semantic_mean_sim",               "Semantic Consistency",  (0, 1),     True),
    ("bleu",                            "BLEU Score",            (0, 0.015), True),
    ("tokens_for_coverage",             "Tokens for Coverage",   None,       False),
    ("total_words",                     "Output Length (words)", None,       True),
]

# ── Helpers ───────────────────────────────────────────────────────────────────
def style_ax(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linewidth=0.5, alpha=0.5)
    ax.set_axisbelow(True)


def model_bar(ax, metric, title, ylim=None):
    """One bar per model, aggregated across all datasets/schemas."""
    means = [model_df[m][metric].mean() for m in MODELS]
    errs  = [1.96 * model_df[m][metric].sem() for m in MODELS]
    x     = np.arange(len(MODELS))
    bars  = ax.bar(x, means, color=COLORS, width=0.55,
                   yerr=errs, capsize=5,
                   error_kw=dict(elinewidth=1.2, ecolor="#555"), zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels([m.replace("-", "-\n") for m in MODELS], fontsize=8)
    ax.set_title(title, fontsize=10, fontweight="bold", pad=6)
    if ylim:
        ax.set_ylim(ylim)
    style_ax(ax)
    pad = (ylim[1] * 0.02) if ylim else 0
    for bar, m in zip(bars, means):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + pad,
                f"{m:.3f}", ha="center", va="bottom", fontsize=7.5)


def per_dataset_bars(ax, metric, title, ylim=None, higher_is_better=True):
    """Clustered bars: one cluster per dataset, one bar per model."""
    n_m   = len(MODELS)
    width = 0.8 / n_m
    x     = np.arange(len(DATASETS))

    for i, (m, color) in enumerate(zip(MODELS, COLORS)):
        vals = [model_df[m][model_df[m]["dataset"] == d][metric].mean()
                for d in DATASETS]
        offset = (i - (n_m - 1) / 2) * width
        ax.bar(x + offset, vals, width, color=color, label=m, zorder=3)

    ax.set_xticks(x)
    ax.set_xticklabels([DATASET_LABELS.get(d, d) for d in DATASETS], fontsize=8)
    ax.set_title(title, fontsize=10, fontweight="bold", pad=6)
    if ylim:
        ax.set_ylim(ylim)
    style_ax(ax)
    ax.legend(fontsize=7, framealpha=0.8, ncol=2)


def per_schema_bars(ax, metric, title, ylim=None):
    """
    2×N_MODELS grouped bars: yprov block vs flowcept block.
    Shows whether model ranking is consistent across collectors.
    """
    schemas = ["yprov", "flowcept"]
    n_m     = len(MODELS)
    width   = 0.35 / n_m
    group_x = np.array([0, 0.6])          # two group centres

    for i, (m, color) in enumerate(zip(MODELS, COLORS)):
        vals = [model_df[m][model_df[m]["schema"] == s][metric].mean()
                for s in schemas]
        offset = (i - (n_m - 1) / 2) * width
        ax.bar(group_x + offset, vals, width, color=color, label=m, zorder=3)

    ax.set_xticks(group_x)
    ax.set_xticklabels(["yProv", "FlowCept"], fontsize=10)
    ax.set_title(title, fontsize=10, fontweight="bold", pad=6)
    if ylim:
        ax.set_ylim(ylim)
    style_ax(ax)
    ax.legend(fontsize=7, framealpha=0.8, ncol=2)


def rank_table(ax, metrics_subset):
    """
    Heatmap-style rank table: models × metrics.
    Cell = rank (1 = best), coloured green→red.
    """
    cols   = [m[0] for m in metrics_subset if m[0] in df.columns]
    labels = [m[1] for m in metrics_subset if m[0] in df.columns]
    hibs   = [m[3] for m in metrics_subset if m[0] in df.columns]

    means  = np.array([[model_df[m][c].mean() for c in cols] for m in MODELS])
    # Rank: 1 = best
    ranks  = np.zeros_like(means, dtype=int)
    for j, hib in enumerate(hibs):
        order = np.argsort(means[:, j])
        if hib:
            order = order[::-1]
        for rank, idx in enumerate(order):
            ranks[idx, j] = rank + 1

    im = ax.imshow(ranks, cmap="RdYlGn_r", aspect="auto", vmin=1, vmax=len(MODELS))
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontsize=7.5, rotation=30, ha="right")
    ax.set_yticks(range(len(MODELS)))
    ax.set_yticklabels(MODELS, fontsize=9)
    ax.set_title("Model Ranking (1 = best per metric)", fontsize=10,
                 fontweight="bold", pad=6)

    for i in range(len(MODELS)):
        for j in range(len(cols)):
            r = ranks[i, j]
            ax.text(j, i, str(r), ha="center", va="center", fontsize=10,
                    fontweight="bold",
                    color="white" if r >= 3 else "black")
    plt.colorbar(im, ax=ax, fraction=0.03, pad=0.03,
                 ticks=[1, 2, 3, 4], label="Rank")


def radar_chart(ax, metrics_radar):
    """Radar per model, normalised 0–1, min=-0.1."""
    cats   = [m[1] for m in metrics_radar]
    cols   = [m[0] for m in metrics_radar]
    N      = len(cats)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), cats, fontsize=8)
    ax.set_rmin(-0.1)

    all_vals = np.array([[model_df[m][c].mean() for c in cols] for m in MODELS])
    col_min  = all_vals.min(axis=0)
    col_rng  = np.where(all_vals.max(axis=0) - col_min > 0,
                        all_vals.max(axis=0) - col_min, 1)

    for m, color in zip(MODELS, COLORS):
        raw    = np.array([model_df[m][c].mean() for c in cols])
        normed = (raw - col_min) / col_rng
        vals   = normed.tolist() + normed[:1].tolist()
        ax.plot(angles, vals, color=color, linewidth=2, label=m)
        ax.fill(angles, vals, color=color, alpha=0.10)

    patches = [mpatches.Patch(color=c, label=m) for m, c in zip(MODELS, COLORS)]
    ax.legend(handles=patches, loc="upper right",
              bbox_to_anchor=(1.55, 1.2), fontsize=8, framealpha=0.8)
    ax.set_title("Multi-Metric Radar\n(normalised, min=−0.1)",
                 fontsize=10, fontweight="bold", pad=20)


# ── Build PDF ─────────────────────────────────────────────────────────────────
with PdfPages(args.out) as pdf:

    # ── Page 1: Aggregated model comparison ──────────────────────────────────
    fig = plt.figure(figsize=(22, 26))
    fig.patch.set_facecolor(BG)
    fig.text(0.5, 0.977, "Model Comparison — Provenance Cards",
             ha="center", fontsize=18, fontweight="bold", color="#1a1a2e")
    fig.text(0.5, 0.966,
             f"Models: {', '.join(MODELS)}  •  Format: Cards  •  Aggregated across all datasets",
             ha="center", fontsize=10, color="#555")

    gs = gridspec.GridSpec(3, 3, figure=fig,
                           top=0.955, bottom=0.04,
                           left=0.06, right=0.97,
                           hspace=0.55, wspace=0.38)

    for idx, (col, label, ylim, _) in enumerate(METRICS):
        r, c = divmod(idx, 3)
        ax = fig.add_subplot(gs[r, c])
        if col in df.columns:
            model_bar(ax, col, label, ylim)
        else:
            ax.set_title(f"{label}\n(column missing)", fontsize=9, color="grey")
            style_ax(ax)

    pdf.savefig(fig, bbox_inches="tight", facecolor=BG)
    plt.close(fig)

    # ── Page 2: Per-dataset breakdown ────────────────────────────────────────
    fig2 = plt.figure(figsize=(22, 26))
    fig2.patch.set_facecolor(BG)
    fig2.text(0.5, 0.977, "Model Comparison — Per Dataset",
              ha="center", fontsize=18, fontweight="bold", color="#1a1a2e")
    fig2.text(0.5, 0.966, "One cluster per dataset, one bar per model",
              ha="center", fontsize=10, color="#555")

    gs2 = gridspec.GridSpec(3, 3, figure=fig2,
                            top=0.955, bottom=0.04,
                            left=0.06, right=0.97,
                            hspace=0.55, wspace=0.38)

    for idx, (col, label, ylim, hib) in enumerate(METRICS):
        r, c = divmod(idx, 3)
        ax = fig2.add_subplot(gs2[r, c])
        if col in df.columns:
            per_dataset_bars(ax, col, label, ylim, hib)
        else:
            ax.set_title(f"{label}\n(column missing)", fontsize=9, color="grey")
            style_ax(ax)

    pdf.savefig(fig2, bbox_inches="tight", facecolor=BG)
    plt.close(fig2)

    # ── Page 3: Per-collector breakdown ──────────────────────────────────────
    fig3 = plt.figure(figsize=(22, 26))
    fig3.patch.set_facecolor(BG)
    fig3.text(0.5, 0.977, "Model Comparison — yProv vs FlowCept",
              ha="center", fontsize=18, fontweight="bold", color="#1a1a2e")
    fig3.text(0.5, 0.966,
              "Does model ranking change depending on the provenance collector?",
              ha="center", fontsize=10, color="#555")

    gs3 = gridspec.GridSpec(3, 3, figure=fig3,
                            top=0.955, bottom=0.04,
                            left=0.06, right=0.97,
                            hspace=0.55, wspace=0.38)

    for idx, (col, label, ylim, _) in enumerate(METRICS):
        r, c = divmod(idx, 3)
        ax = fig3.add_subplot(gs3[r, c])
        if col in df.columns:
            per_schema_bars(ax, col, label, ylim)
        else:
            ax.set_title(f"{label}\n(column missing)", fontsize=9, color="grey")
            style_ax(ax)

    pdf.savefig(fig3, bbox_inches="tight", facecolor=BG)
    plt.close(fig3)

    # ── Page 4: Radar + Rank table ────────────────────────────────────────────
    fig4 = plt.figure(figsize=(22, 14))
    fig4.patch.set_facecolor(BG)
    fig4.text(0.5, 0.97, "Model Comparison — Radar & Ranking Table",
              ha="center", fontsize=16, fontweight="bold", color="#1a1a2e")

    gs4 = gridspec.GridSpec(1, 2, figure=fig4,
                            top=0.90, bottom=0.08,
                            left=0.05, right=0.97,
                            wspace=0.45)

    radar_metrics = [
        ("absolute_factual_coverage_score", "Abs. Coverage"),
        ("relative_factual_coverage_f1",    "Rel. Coverage F1"),
        ("rouge_l_f1",                      "ROUGE-L F1"),
        ("semantic_mean_sim",               "Semantic Sim"),
        ("bleu",                            "BLEU"),
        ("hallucination_rate",              "Hallucination"),
    ]
    radar_metrics = [(c, l) for c, l in radar_metrics if c in df.columns]

    ax_radar = fig4.add_subplot(gs4[0, 0], polar=True)
    radar_chart(ax_radar, radar_metrics)

    ax_rank = fig4.add_subplot(gs4[0, 1])
    rank_table(ax_rank, METRICS)

    pdf.savefig(fig4, bbox_inches="tight", facecolor=BG)
    plt.close(fig4)

    meta = pdf.infodict()
    meta["Title"] = "Model Comparison Dashboard — Provenance Cards"

print(f"✅  Saved → {args.out}")
