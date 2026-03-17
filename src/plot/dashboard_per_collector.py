
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings("ignore")

# ── Config ──────────────────────────────────────────────────────────────────
CSV_PATH = "results/analysis_results.csv"
OUT_PATH = "dashboard_per_collector.pdf"

PALETTE = {
    "yprov":    "#4C72B0",
    "flowcept": "#DD8452",
    "json":     "#55A868",
    "card":     "#C44E52",
}

# Groups for combo comparisons
GROUP_COLORS = {
    "yprov + json":  "#4C72B0",
    "yprov + card":  "#76A8D8",
    "flowcept + json": "#DD8452",
    "flowcept + card": "#F0B97A",
}

DATASET_LABELS = {
    "example":           "Example",
    "fusion":            "Fusion",
    "nasa":              "NASA",
    "train_test_splits": "Train/Test",
    "turbolence":        "Turbulence",
}

# ── Load & enrich data ───────────────────────────────────────────────────────
df = pd.read_csv(CSV_PATH)
df["format"] = df["file"].apply(lambda x: "card" if "/cards/" in x else "json")
df["schema"] = df["file"].apply(
    lambda x: "yprov" if ("_Y.json" in x or "_Y.md" in x) else "flowcept"
)
df["dataset"] = (
    df["file"]
    .apply(lambda x: x.split("/")[-1].split("__")[0])
    .str.replace(r"(_F|_Y)\.(jsonl|json|md)$", "", regex=True)
)
df["group"] = df["schema"] + " + " + df["format"]


# ── Helpers ──────────────────────────────────────────────────────────────────
def mean_ci(series):
    """Return (mean, 95% CI half-width) for a pandas Series."""
    m  = series.mean()
    se = series.sem()
    return m, 1.96 * se


def grouped_bar(ax, groups, metric, color_map, title, ylabel, ylim=None):
    """Horizontal grouped bar for a dict {label: series}."""
    labels = list(groups.keys())
    means  = [groups[g][metric].mean() for g in labels]
    errs   = [1.96 * groups[g][metric].sem() for g in labels]
    colors = [color_map[g] for g in labels]
    x = np.arange(len(labels))
    bars = ax.bar(x, means, color=colors, width=0.55,
                  yerr=errs, capsize=4, error_kw=dict(elinewidth=1.2, ecolor="#555"))
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_title(title, fontsize=10, fontweight="bold", pad=6)
    ax.set_ylabel(ylabel, fontsize=8)
    if ylim:
        ax.set_ylim(ylim)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linewidth=0.5, alpha=0.5)
    ax.set_axisbelow(True)
    # Value labels
    for bar, mean in zip(bars, means):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.005,
                f"{mean:.3f}", ha="center", va="bottom", fontsize=7.5)
    return ax


def per_dataset_bars(ax, metric, title, ylabel):
    """4-bar cluster (yprov/flowcept × json/card) per dataset."""
    datasets  = sorted(df["dataset"].unique())
    n_groups  = len(datasets)
    n_bars    = 4
    width     = 0.18
    x         = np.arange(n_groups)
    grp_order = ["yprov + json", "yprov + card", "flowcept + json", "flowcept + card"]
    for i, grp in enumerate(grp_order):
        sub    = df[df["group"] == grp].set_index("dataset")
        vals   = [sub.loc[d, metric] if d in sub.index else np.nan for d in datasets]
        offset = (i - 1.5) * width
        ax.bar(x + offset, vals, width=width, color=GROUP_COLORS[grp],
               label=grp, zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels([DATASET_LABELS[d] for d in datasets], fontsize=8)
    ax.set_title(title, fontsize=10, fontweight="bold", pad=6)
    ax.set_ylabel(ylabel, fontsize=8)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linewidth=0.5, alpha=0.5, zorder=0)
    ax.set_axisbelow(True)
    ax.legend(fontsize=7, ncol=2, framealpha=0.7)


def radar_chart(ax, categories, group_data, colors, title):
    """Normalised radar / spider chart."""
    N     = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), categories, fontsize=8)

    # Normalise each metric 0-1 across all groups
    all_vals = np.array([[group_data[g][c] for c in categories] for g in group_data])
    col_min  = all_vals.min(axis=0)
    col_max  = all_vals.max(axis=0)
    col_rng  = np.where(col_max - col_min > 0, col_max - col_min, 1)

    for grp, color in zip(group_data, colors):
        raw   = np.array([group_data[grp][c] for c in categories])
        normed = (raw - col_min) / col_rng
        values = normed.tolist() + normed[:1].tolist()
        ax.plot(angles, values, color=color, linewidth=1.8, alpha=0.5, linestyle="solid")
        ax.fill(angles, values, color=color, alpha=0.12)

    ax.set_title(title, fontsize=10, fontweight="bold", pad=18)
    patches = [mpatches.Patch(color=c, label=g) for g, c in zip(group_data, colors)]
    ax.legend(handles=patches, loc="upper right", bbox_to_anchor=(1.35, 1.15), fontsize=7.5, framealpha=0.8)
    ax.set_rmin(-0.1)


def heatmap(ax, pivot_metric, title, cmap="RdYlGn"):
    datasets = sorted(df["dataset"].unique())
    groups   = ["yprov + json", "yprov + card", "flowcept + json", "flowcept + card"]
    mat      = np.full((len(groups), len(datasets)), np.nan)
    for i, grp in enumerate(groups):
        sub = df[df["group"] == grp].set_index("dataset")
        for j, d in enumerate(datasets):
            if d in sub.index:
                mat[i, j] = sub.loc[d, pivot_metric]
    im = ax.imshow(mat, cmap=cmap, aspect="auto", vmin=0,
                   vmax=1 if mat[~np.isnan(mat)].max() <= 1 else None)
    ax.set_xticks(range(len(datasets)))
    ax.set_xticklabels([DATASET_LABELS[d] for d in datasets], fontsize=8)
    ax.set_yticks(range(len(groups)))
    ax.set_yticklabels(groups, fontsize=8)
    ax.set_title(title, fontsize=10, fontweight="bold", pad=6)
    # Annotate cells
    for i in range(len(groups)):
        for j in range(len(datasets)):
            if not np.isnan(mat[i, j]):
                ax.text(j, i, f"{mat[i, j]:.2f}", ha="center", va="center",
                        fontsize=8, fontweight="bold",
                        color="white" if mat[i, j] < 0.35 else "black")
    plt.colorbar(im, ax=ax, fraction=0.03, pad=0.03)


# ── Build page ───────────────────────────────────────────────────────────────
schema_groups = {s: df[df["schema"] == s] for s in ["yprov", "flowcept"]}
format_groups = {f: df[df["format"] == f] for f in ["json", "card"]}
combo_groups  = {g: df[df["group"] == g] for g in GROUP_COLORS}

with PdfPages(OUT_PATH) as pdf:

    # ── Page 1: Main dashboard ───────────────────────────────────────────────
    fig = plt.figure(figsize=(22, 14))
    fig.patch.set_facecolor("#F7F8FA")

    # Title banner
    fig.text(0.5, 0.975, "Provenance Cards Benchmark — Results Dashboard", ha="center", va="top", fontsize=18, fontweight="bold", color="#1a1a2e")
    fig.text(0.5, 0.953, "Model: Llama-3.2-3B  •  Datasets: Example, Fusion, NASA, Train/Test Splits, Turbulence", ha="center", va="top", fontsize=10, color="#555")

    gs = gridspec.GridSpec(4, 4, figure=fig,
                           top=0.9, bottom=0.04,
                           left=0.06, right=0.97,
                           hspace=0.52, wspace=0.38)

    # ── Row 0: Schema comparison (yprov vs flowcept) ─────────────────────────
    ax00 = fig.add_subplot(gs[0, 0])
    grouped_bar(ax00, schema_groups, "absolute_factual_coverage_score", PALETTE, "Coverage Score\n(yprov vs flowcept)", "Score", ylim=(0, 1))

    ax00 = fig.add_subplot(gs[0, 1])
    grouped_bar(ax00, schema_groups, "relative_factual_coverage_score", PALETTE, "Coverage Score\n(yprov vs flowcept)", "Score", ylim=(0, 1))

    ax00 = fig.add_subplot(gs[0, 2])
    grouped_bar(ax00, schema_groups, "relative_factual_coverage_f1", PALETTE, "Coverage Score\n(yprov vs flowcept)", "Score", ylim=(0, 1))

    ax01 = fig.add_subplot(gs[0, 3])
    grouped_bar(ax01, schema_groups, "tokens_for_coverage", PALETTE, "Hallucination Rate\n(yprov vs flowcept)", "Rate", ylim=(0, 1))

    ax01 = fig.add_subplot(gs[1, 0])
    grouped_bar(ax01, schema_groups, "hallucination_rate", PALETTE, "Hallucination Rate\n(yprov vs flowcept)", "Rate", ylim=(0, 1))

    ax02 = fig.add_subplot(gs[1, 1])
    grouped_bar(ax02, schema_groups, "rouge_l_f1", PALETTE, "ROUGE-L F1\n(yprov vs flowcept)", "F1", ylim=(0, 0.15))

    ax02 = fig.add_subplot(gs[1, 2])
    grouped_bar(ax02, schema_groups, "distinct_n", PALETTE, "ROUGE-L F1\n(yprov vs flowcept)", "F1", ylim=(0, 0.15))

    ax02 = fig.add_subplot(gs[1, 3])
    grouped_bar(ax02, schema_groups, "self_bleu", PALETTE, "ROUGE-L F1\n(yprov vs flowcept)", "F1", ylim=(0, 0.15))


    # ── Row 2: Per-dataset breakdowns ─────────────────────────────────────────
    ax20 = fig.add_subplot(gs[2, 0])
    per_dataset_bars(ax20, "relative_factual_coverage_score", "Coverage Score per Dataset", "Score")

    ax21 = fig.add_subplot(gs[2, 1])
    per_dataset_bars(ax21, "hallucination_rate", "Hallucination Rate per Dataset", "Rate")

    ax22 = fig.add_subplot(gs[2, 2])
    per_dataset_bars(ax22, "rouge_l_f1", "ROUGE-L F1 per Dataset", "F1")

    ax02 = fig.add_subplot(gs[2, 3])
    grouped_bar(ax02, schema_groups, "bleu_multi_ref", PALETTE, "ROUGE-L F1\n(yprov vs flowcept)", "F1", ylim=(0, 0.15))
    

    # ── Row 3: Radar + Heatmap ────────────────────────────────────────────────
    ax30 = fig.add_subplot(gs[3, 0], polar=True)
    radar_cats = ["Coverage", "ROUGE-L F1", "Semantic Sim", "1-Hallucination", "BLEU"]
    radar_data = {}
    cols = []
    for grp in GROUP_COLORS:
        if "yprov" not in grp: continue
        sub = df[df["group"] == grp]
        cols.append(GROUP_COLORS[grp])
        radar_data[grp] = {
            "Coverage":       sub["relative_factual_coverage_score"].mean(),
            "ROUGE-L F1":     sub["rouge_l_f1"].mean(),
            "Semantic Sim":   sub["semantic_mean_sim"].mean(),
            "1-Hallucination": 1 - sub["hallucination_rate"].mean(),
            "BLEU":           sub["bleu"].mean() * 100,   # rescale so it's visible
        }
    radar_chart(ax30, radar_cats, radar_data, cols, "Multi-Metric Radar\n(all groups, normalised 0–1)")
    ax30 = fig.add_subplot(gs[3, 1], polar=True)
    radar_cats = ["Coverage", "ROUGE-L F1", "Semantic Sim", "1-Hallucination", "BLEU"]
    radar_data = {}
    cols = []
    for grp in GROUP_COLORS:
        if "flowcept" not in grp: continue
        sub = df[df["group"] == grp]
        cols.append(GROUP_COLORS[grp])
        radar_data[grp] = {
            "Coverage":       sub["relative_factual_coverage_score"].mean(),
            "ROUGE-L F1":     sub["rouge_l_f1"].mean(),
            "Semantic Sim":   sub["semantic_mean_sim"].mean(),
            "1-Hallucination": 1 - sub["hallucination_rate"].mean(),
            "BLEU":           sub["bleu"].mean() * 100,   # rescale so it's visible
        }
    radar_chart(ax30, radar_cats, radar_data, cols, "Multi-Metric Radar\n(all groups, normalised 0–1)")

    ax31 = fig.add_subplot(gs[3, 2])
    heatmap(ax31, "relative_factual_coverage_score", "Coverage Score Heatmap\n(group × dataset)")

    pdf.savefig(fig, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)

    ax02 = fig.add_subplot(gs[3, 3])
    grouped_bar(ax02, schema_groups, "total_words", PALETTE, "ROUGE-L F1\n(yprov vs flowcept)", "F1", ylim=(0, 0.15))

    # ax02 = fig.add_subplot(gs[3, 4])
    # grouped_bar(ax02, schema_groups, "total_sentences", PALETTE, "ROUGE-L F1\n(yprov vs flowcept)", "F1", ylim=(0, 0.15))

    metrics_p2 = [
        ("relative_factual_coverage_score", "Coverage Score" ), # (0, 1)),
        ("hallucination_rate","Hallucination Rate"), #  (0, 1)),
        ("rouge_l_f1", "ROUGE-L F1"), # (0, 0.18)),
        ("semantic_mean_sim", "Semantic Consistency"), #  (0.3, 0.9)),
        ("bleu", "BLEU Score"), #  (0, 0.012)),
        ("total_words", "Output Length (words)"), #, None),
    ]

    # ── Page 3: Schema deep-dive ─────────────────────────────────────────────
    fig3 = plt.figure(figsize=(22, 12))
    fig3.patch.set_facecolor("#F7F8FA")

    fig3.text(0.5, 0.975, "yProv vs FlowCept — Quality Delta per Dataset", ha="center", va="top", fontsize=16, fontweight="bold", color="#1a1a2e")

    gs3 = gridspec.GridSpec(2, 3, figure=fig3,
                            top=0.93, bottom=0.06,
                            left=0.07, right=0.97,
                            hspace=0.48, wspace=0.38)

    for idx, (metric, label) in enumerate(metrics_p2):
        r, c = divmod(idx, 3)
        ax = fig3.add_subplot(gs3[r, c])
        datasets = sorted(df["dataset"].unique())
        x = np.arange(len(datasets))
        width    = 0.35

        yp_vals = [df[(df["schema"] == "yprov") & (df["dataset"] == d)][metric].mean() for d in datasets]
        fc_vals = [df[(df["schema"] == "flowcept") & (df["dataset"] == d)][metric].mean() for d in datasets]

        ax.bar(x - width / 2, yp_vals, width, color=PALETTE["yprov"],   label="yProv",    zorder=3)
        ax.bar(x + width / 2, fc_vals, width, color=PALETTE["flowcept"], label="FlowCept", zorder=3)

        for xi, (yv, fv) in enumerate(zip(yp_vals, fc_vals)):
            delta = yv - fv
            col   = "#2ca02c" if delta > 0 else "#d62728"
            sym   = "▲" if delta > 0 else "▼"
            ypos  = max(yv, fv) + max(yv, fv) * 0.05 + 0.001
            ax.text(xi, ypos, f"{sym}{abs(delta):.3f}", ha="center", va="bottom", fontsize=6.5, color=col, fontweight="bold")

        ax.set_xticks(x)
        ax.set_xticklabels([DATASET_LABELS[d] for d in datasets], fontsize=8)
        ax.set_title(label, fontsize=10, fontweight="bold", pad=6)
        ax.set_ylabel(label, fontsize=8)
        # if ylim:
        #     ax.set_ylim(ylim)
        ax.spines[["top", "right"]].set_visible(False)
        ax.yaxis.grid(True, linewidth=0.5, alpha=0.5, zorder=0)
        ax.set_axisbelow(True)
        ax.legend(fontsize=8, framealpha=0.7)

    pdf.savefig(fig3, bbox_inches="tight", facecolor=fig3.get_facecolor())
    plt.close(fig3)

    # PDF metadata
    meta = pdf.infodict()
    meta["Title"]   = "Provenance Cards Benchmark Dashboard"
    meta["Author"]  = "Benchmark Pipeline"
    meta["Subject"] = "LLM provenance card evaluation results"

print(f"✅  Dashboard saved → {OUT_PATH}")
