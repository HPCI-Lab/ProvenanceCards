
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# ── paths (edit if needed) ────────────────────────────────────────────────────
FILE1 = "results/leaveoneout2.csv"   # leave-one-out
FILE2 = "results/leaveoneout3.csv"   # baseline / single-card

OUTPUT_DIR = "./figures"             # where to save figures
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── palette ───────────────────────────────────────────────────────────────────
CARD_COLORS = {
    "DataCard":           "#4C72B0",
    "Finetuning Model Card": "#DD8452",
    "Pretraining Model Card":"#55A868",
    "Workflow Card":      "#C44E52",
}
DIFF_COLOR   = "#8172B3"
EASY_COLOR   = "#2ca02c"
MED_COLOR    = "#ff7f0e"
HARD_COLOR   = "#d62728"
DIFFICULTY_PALETTE = {"easy": EASY_COLOR, "medium": MED_COLOR, "hard": HARD_COLOR}

METRICS      = ["similarity", "llm_as_judge_1", "llm_as_judge_2"]
METRIC_LABELS = ["Similarity", "LLM Judge 1", "LLM Judge 2"]

# ── helpers ───────────────────────────────────────────────────────────────────
def composite(df: pd.DataFrame) -> pd.Series:
    return df[METRICS].mean(axis=1)


def savefig(name: str):
    path = os.path.join(OUTPUT_DIR, name)
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  saved → {path}")


# ═════════════════════════════════════════════════════════════════════════════
# 1. LOAD & PREPARE
# ═════════════════════════════════════════════════════════════════════════════
print("Loading data …")
df1 = pd.read_csv(FILE1, sep=";")
df2 = pd.read_csv(FILE2, sep=";")

# map numeric 'without' codes → card names
card_map = {
    0: "DataCard",
    1: "Finetuning Model Card",
    2: "Pretraining Model Card",
    3: "Workflow Card",
}
df1["card_removed"] = df1["without"].map(card_map)

# composite score
df1["composite"] = composite(df1)
df2["composite"] = composite(df2)

# difficulty order
diff_order = ["easy", "medium", "hard"]

print(f"  File 1: {len(df1)} rows  |  cards removed: {sorted(df1['card_removed'].unique())}")
print(f"  File 2: {len(df2)} rows  |  modalities: {sorted(df2['without'].unique())}")
print()


# ═════════════════════════════════════════════════════════════════════════════
# 2.  FIGURE 1 — Leave-one-out: per-card mean scores (bar chart, 3 metrics)
# ═════════════════════════════════════════════════════════════════════════════
print("Figure 1: per-card mean scores …")

card_order = list(card_map.values())
summary1 = (
    df1.groupby("card_removed")[METRICS]
    .mean()
    .reindex(card_order)
)

fig, ax = plt.subplots(figsize=(10, 5))
x = np.arange(len(card_order))
colors = ["#4C72B0", "#DD8452", "#55A868", "#C44E52"]

summary1.T.plot.bar(color=colors, ax=ax)

ax.set_xticks(range(len(METRIC_LABELS)))
ax.set_xticklabels(METRIC_LABELS, fontsize=11, rotation=45)
ax.set_ylabel("Mean Score", fontsize=12)
ax.set_title("Leave-One-Out: Mean Scores When Each Card Is Removed", fontsize=13, fontweight="bold")
ax.set_ylim(0, 1.05)
ax.legend(title="Card Removed", fontsize=10)
ax.axhline(0, color="black", linewidth=0.5)
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()
savefig("fig1_card_mean_scores.png")

# ═════════════════════════════════════════════════════════════════════════════
# 3.  FIGURE 2 — Card influence: degradation vs. baseline (file 2)
#     baseline = all cards; others = single-card context
# ═════════════════════════════════════════════════════════════════════════════
print("Figure 2: degradation vs baseline …")

# clean up 'without' labels in file 2
modality_rename = {
    "baseline":    "Baseline\n(all cards)",
    "datacard":    "DataCard\nonly",
    "finetuned":   "Finetuning MC\nonly",
    "pretrained":  "Pretraining MC\nonly",
    "workflow":    "Workflow Card\nonly",
    "workflowcard":"Workflow Card\nonly",   # merge
}
df2["modality"] = df2["without"].map(modality_rename)

# merge workflow / workflowcard
summary2 = df2.groupby("modality")[METRICS + ["composite"]].mean()

baseline_vals = summary2.loc["Baseline\n(all cards)"]
delta = summary2.subtract(baseline_vals)

mod_order = [
    "DataCard\nonly",
    "Finetuning MC\nonly",
    "Pretraining MC\nonly",
    "Workflow Card\nonly",
]
delta_ordered = delta.reindex(mod_order)

fig, ax = plt.subplots(figsize=(10, 5))
x = np.arange(len(mod_order))
bar_colors = [CARD_COLORS["DataCard"],
              CARD_COLORS["Finetuning Model Card"],
              CARD_COLORS["Pretraining Model Card"],
              CARD_COLORS["Workflow Card"]]
bars = ax.bar(x, delta_ordered["composite"], color=bar_colors, alpha=0.85, zorder=3)

for bar, val in zip(bars, delta_ordered["composite"]):
    ax.text(bar.get_x() + bar.get_width() / 2, val + (0.003 if val >= 0 else -0.012),
            f"{val:+.3f}", ha="center", va="bottom" if val >= 0 else "top", fontsize=10)

ax.set_xticks(x)
ax.set_xticklabels(mod_order, fontsize=10)
ax.set_ylabel("Δ Composite Score (all metrics) vs. Baseline", fontsize=12)
ax.set_title("Single-Card Context: Score Degradation Relative to Full Baseline",
             fontsize=13, fontweight="bold")
ax.axhline(0, color="black", linewidth=1)
ax.grid(axis="y", alpha=0.3, zorder=0)
ax.set_ylim(-0.32, 0)
fig.tight_layout()
savefig("fig2_single_card_degradation.png")

# ═════════════════════════════════════════════════════════════════════════════
# 4.  FIGURE 3 — Difficulty vs. score (file 1 leave-one-out)
# ═════════════════════════════════════════════════════════════════════════════
print("Figure 3: difficulty vs composite score …")

diff_means = (
    df1.groupby(["type_", "card_removed"])["composite"]
    .mean()
    .unstack("card_removed")
    .reindex(diff_order)
    [card_order]
)

fig, ax = plt.subplots(figsize=(9, 5))
x = np.arange(len(diff_order))
width = 0.2
diff_means.T.plot.bar(color=list(CARD_COLORS.values()), ax=ax)
ax.set_xticklabels(list(card_map.values()), rotation=45)#["Easy", "Medium", "Hard"], fontsize=12)
ax.set_xlabel("Card Removed", fontsize=12)
ax.set_ylabel("Mean Composite Score", fontsize=12)
ax.set_title("Composite Score by Difficulty & Card Removed", fontsize=13, fontweight="bold")
ax.set_ylim(0, 1.0)
ax.legend(title="Card Removed", fontsize=9)
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()
savefig("fig3_difficulty_by_card.png")


# ═════════════════════════════════════════════════════════════════════════════
# 5.  FIGURE 4 — Hard questions: score distribution per card (violin)
# ═════════════════════════════════════════════════════════════════════════════
print("Generating distribution plot for difficulty levels...")

diff_order = ["easy", "medium", "hard"]
available_diffs = [d for d in diff_order if d in df1["type_"].unique()]
if not available_diffs:
    available_diffs = sorted(df1["type_"].unique())

DIFF_COLORS = ["#66c2a5", "#fc8d62", "#8da0cb"] 

fig, axes = plt.subplots(1, 3, figsize=(13, 5), sharey=True)
for ax, metric, mlabel in zip(axes, METRICS, METRIC_LABELS):
    data = [df1[df1["type_"] == d][metric].dropna().values for d in available_diffs]
    parts = ax.violinplot(data, positions=range(len(available_diffs)), showmedians=True, showextrema=True)
    
    for i, pc in enumerate(parts["bodies"]):
        pc.set_facecolor(DIFF_COLORS[i % len(DIFF_COLORS)])
        pc.set_alpha(0.75)
    
    parts["cmedians"].set_color("black")
    ax.set_xticks(range(len(available_diffs)))
    ax.set_xticklabels([d.capitalize() for d in available_diffs], fontsize=10)
    ax.set_title(mlabel, fontsize=11)
    ax.set_ylim(-0.05, 1.05)
    ax.grid(axis="y", alpha=0.3)

axes[0].set_ylabel("Score", fontsize=12)
fig.suptitle("Score Distribution Across Difficulty Levels", fontsize=13, fontweight="bold")
fig.tight_layout()
savefig("fig4_question_distribution.png")


# ═════════════════════════════════════════════════════════════════════════════
# 6.  FIGURE 5 — Difficulty × Metric heatmap (file 1)
# ═════════════════════════════════════════════════════════════════════════════
print("Figure 5: difficulty × aggregated metric heatmap …")

# 1. Aggregate the two LLM judges into a single average column
df1["llm_judge_avg"] = df1[["llm_as_judge_1", "llm_as_judge_2"]].mean(axis=1)

# 2. Identify the base metrics (excluding the individual judges) 
# and add the new aggregated judge column
base_metrics = [m for m in METRICS if m not in ["llm_as_judge_1", "llm_as_judge_2"]]
final_metrics_list = base_metrics + ["llm_judge_avg"]

# 3. Calculate the composite metric (mean of all base scores + aggregated judge)
df1["composite_metric"] = df1[final_metrics_list].mean(axis=1)

# Define the final columns and labels to display in the heatmap
HEATMAP_METRICS = final_metrics_list + ["composite_metric"]
HEATMAP_LABELS = [m.replace("_", " ").title() for m in final_metrics_list] + ["Overall Composite"]

# Prepare heatmap data
heatmap_data = (
    df1.groupby("type_")[HEATMAP_METRICS]
    .mean()
    .reindex(diff_order)
)
heatmap_data.index = ["Easy", "Medium", "Hard"]

# Plotting
fig, ax = plt.subplots(figsize=(8, 5))
im = ax.imshow(heatmap_data.values, cmap="RdYlGn", vmin=0, vmax=1, aspect="auto")

ax.set_xticks(range(len(HEATMAP_METRICS)))
ax.set_xticklabels(HEATMAP_LABELS, fontsize=10, rotation=15)
ax.set_yticks(range(len(heatmap_data)))
ax.set_yticklabels(heatmap_data.index, fontsize=11)

# Annotate heatmap with values
for i in range(len(heatmap_data)):
    for j in range(len(HEATMAP_METRICS)):
        val = heatmap_data.values[i, j]
        ax.text(j, i, f"{val:.2f}", ha="center", va="center",
                fontsize=11, fontweight="bold",
                color="black" if 0.4 < val < 0.7 else "white")

plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
ax.set_title("Aggregated Performance by Difficulty", fontsize=13, fontweight="bold")
fig.tight_layout()

savefig("fig5_difficulty_heatmap_aggregated.png")


# ═════════════════════════════════════════════════════════════════════════════
# 7. FIGURE 6 — One Card Only Validation (Heatmap)
# ═════════════════════════════════════════════════════════════════════════════
print("Figure 6: one card only validation heatmap …")

# Join and prepare the data
questions = pd.read_csv("dataset/questions/Questions_Nicola.csv")
df2_joined = df2.join(questions, on="answer")

# Aggregate by 'without' (the card) and 'Type' (difficulty)
# We pivot so cards are columns and difficulty types are rows
df2_pivot = (
    df2_joined.groupby(["without", "Type"])["composite"]
    .mean()
    .reset_index()
    .pivot(index="Type", columns="without", values="composite")
)

# Ensure the difficulty order is consistent with previous charts
diff_order = ["easy", "medium", "hard"]
available_indices = [d for d in diff_order if d in df2_pivot.index]

# Plotting
fig, ax = plt.subplots(figsize=(12, 5))
sns.heatmap(
    df2_pivot, 
    annot=True, 
    fmt=".2f", 
    cmap="RdYlGn", 
    cbar_kws={'label': 'Mean Composite Score'},
    ax=ax,
    annot_kws={"fontweight": "bold"}
)

# Styling to match previous figures
ax.set_title("Validation: Performance when only one specific card is removed", 
             fontsize=13, fontweight="bold", pad=20)
ax.set_xlabel("Card Used", fontsize=12)
ax.set_ylabel("Question Focus", fontsize=12)

# Clean up labels (Capitalize difficulties and clean card names)
ax.set_yticklabels([t.get_text().capitalize() for t in ax.get_yticklabels()], rotation=0)
ax.set_xticklabels(["Baseline", "Only Data Card", "Only Finetuning MC", "Only Pretraining MC", "Only Workflow Card"], rotation=45, ha="right")

fig.tight_layout()
savefig("fig6_one_card_validation_heatmap.png")

# ═════════════════════════════════════════════════════════════════════════════
# 8.  FIGURE 7 — Card influence ranking: drop from single-card to baseline (file 2)
#     Three sub-panels, one per metric
# ═════════════════════════════════════════════════════════════════════════════
print("Figure 7: per-metric delta single-card vs baseline …")

baseline_row = df2[df2["without"] == "baseline"].groupby("type_")[METRICS].mean()
single_rows  = df2[df2["without"] != "baseline"].copy()

# merge workflow variants
single_rows["without"] = single_rows["without"].replace(
    {"workflowcard": "workflow"}
)

sc_summary = single_rows.groupby(["without", "type_"])[METRICS].mean()

fig, axes = plt.subplots(1, 3, figsize=(14, 5), sharey=False)
mod_labels = {
    "datacard":  "DataCard",
    "finetuned": "Finetuning MC",
    "pretrained":"Pretraining MC",
    "workflow":  "Workflow Card",
}
x = np.arange(len(diff_order))
width = 0.2
for ax, metric, mlabel in zip(axes, METRICS, METRIC_LABELS):
    for i, (mod_key, mod_label) in enumerate(mod_labels.items()):
        deltas = []
        for diff in diff_order:
            try:
                sc_val = sc_summary.loc[(mod_key, diff), metric]
            except KeyError:
                sc_val = np.nan
            base_val = baseline_row.loc[diff, metric] if diff in baseline_row.index else np.nan
            deltas.append(sc_val - base_val)
        color = list(CARD_COLORS.values())[i]
        ax.bar(x + (i - 1.5) * width, deltas, width, label=mod_label,
               color=color, alpha=0.85)

    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(["Easy", "Medium", "Hard"], fontsize=10)
    ax.set_title(mlabel, fontsize=11)
    ax.set_ylabel("Δ Score vs Baseline", fontsize=10)
    ax.grid(axis="y", alpha=0.3)

axes[0].legend(title="Single Card", fontsize=8, title_fontsize=9)
fig.suptitle("Single-Card Context: Per-Metric Δ vs. Full Baseline, by Difficulty", fontsize=13, fontweight="bold")
fig.tight_layout()
savefig("fig7_singlecard_permetric_delta.png")


# ═════════════════════════════════════════════════════════════════════════════
# 8. FIGURE 8 — Data size of provenance cards
# ═════════════════════════════════════════════════════════════════════════════
print("Figure 8: size of cards related to use case and card type …")

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

path = Path("dataset/cards")
all_files = [f for f in os.listdir(path) if f.endswith('.md')] # Assuming json cards

# Helper function to convert bytes to KB
def to_kb(size_list):
    return [s / 1024 for s in size_list]

# --- Data Preparation for Subplot 1 (Card Type) ---
card_types = ["workflow", "data", "model"]
type_sizes = {t: to_kb([os.path.getsize(path / f) for f in all_files if t in f]) for t in card_types}
type_means = [np.mean(type_sizes[t]) if type_sizes[t] else 0 for t in card_types]

# --- Data Preparation for Subplot 2 (Use Case x Card Type) ---
use_cases = ["1", "2", "3", "4", "5"]
# We'll create a matrix: rows = use cases, columns = card types
grouped_data = []
for uc in use_cases:
    row = []
    for t in card_types:
        sizes = to_kb([os.path.getsize(path / f) for f in all_files if uc in f and t in f])
        print(sizes)
        row.append(np.mean(sizes) if sizes else 0)
    grouped_data.append(row)
grouped_data = np.array(grouped_data) # Shape: (5, 3)
print(grouped_data)

# --- Plotting ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
colors = ["#66c2a5", "#fc8d62", "#8da0cb"] # Consistent with previous diff colors

# Subplot 1: Mean Size by Card Type
ax1.bar(card_types, type_means, color=colors, edgecolor='black', alpha=0.8)
ax1.set_title("Mean Card Size by Type", fontsize=13, fontweight="bold")
ax1.set_ylabel("Size (KB)", fontsize=12)
ax1.grid(axis='y', linestyle='--', alpha=0.6)
ax1.set_xticklabels([t.capitalize() for t in card_types])

# Subplot 2: Grouped Bar Chart (Use Case and Card Type)
x = np.arange(len(use_cases))
width = 0.25

for i, t in enumerate(card_types):
    ax2.bar(x + (i * width), grouped_data[:, i], width, label=t.capitalize(), 
            color=colors[i], edgecolor='black', alpha=0.8)

ax2.set_title("Mean Size by Use Case & Card Type", fontsize=13, fontweight="bold")
ax2.set_xlabel("Use Case ID", fontsize=12)
ax2.set_xticks(x + width)
ax2.set_xticklabels([f"UC {uc}" for uc in use_cases])
ax2.legend(title="Card Type")
ax2.grid(axis='y', linestyle='--', alpha=0.6)

fig.suptitle("Provenance Card Data Size Analysis", fontsize=15, fontweight="bold")
# fig.tight_layout(rect=[0, 0.03, 1, 0.95])

savefig("fig8_card_sizes.png")

# ═════════════════════════════════════════════════════════════════════════════
# 10. NUMERIC REPORT
# ═════════════════════════════════════════════════════════════════════════════
print()
print("=" * 65)
print("NUMERIC SUMMARY")
print("=" * 65)

print("\n── File 1 (Leave-One-Out): Composite by Card Removed ──")
print(df1.groupby("card_removed")["composite"].agg(["mean", "std", "median"])
        .reindex(card_order).round(4).to_string())

print("\n── File 1: Composite by Difficulty ──")
print(df1.groupby("type_")["composite"].agg(["mean", "std"])
        .reindex(diff_order).round(4).to_string())

print("\n── File 1: Composite by Card × Difficulty ──")
ct = df1.groupby(["card_removed", "type_"])["composite"].mean().unstack().reindex(card_order)[diff_order]
print(ct.round(4).to_string())

print("\n── File 2 (Modality): Composite by Context ──")
print(df2.groupby("modality")["composite"].agg(["mean", "std", "median"])
        .round(4).to_string())

print("\n── Card Influence Ranking (least → most degradation when removed) ──")
ranked = (
    df1.groupby("card_removed")["composite"].mean()
    .reindex(card_order)
    .sort_values(ascending=False)
)
print("  Higher score = less degradation when this card is removed")
print("  (i.e. the card matters LESS)\n")
for rank, (card, score) in enumerate(ranked.items(), 1):
    print(f"  {rank}. {card:<28} composite = {score:.4f}")

print()
print("All figures saved to:", os.path.abspath(OUTPUT_DIR))