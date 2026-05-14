
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
METRIC_LABELS = ["Similarity", "LLM Judge"]

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
summary1["llm_as_judge"] = summary1["llm_as_judge_1"] + summary1["llm_as_judge_2"]
summary1["llm_as_judge"] /= 2.0
summary1 = summary1.drop(["llm_as_judge_1", "llm_as_judge_2"], axis=1)

fig, ax = plt.subplots(figsize=(8, 5))
x = np.arange(len(card_order))
colors = ["#4C72B0", "#DD8452", "#55A868", "#C44E52"]

print(summary1)
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
# print("Figure 2: degradation vs top answer …")

# # clean up 'without' labels in file 2
modality_rename = {
    "baseline":    "Top Answer\n(all cards)",
    "datacard":    "DataCard\nonly",
    "finetuned":   "Finetuning MC\nonly",
    "pretrained":  "Pretraining MC\nonly",
    "workflow":    "Workflow Card\nonly",
    "workflowcard":"Workflow Card\nonly",   # merge
}
df2["modality"] = df2["without"].map(modality_rename)

# merge workflow / workflowcard
summary2 = df2.groupby("modality")[METRICS + ["composite"]].mean()

baseline_vals = summary2.loc["Top Answer\n(all cards)"]
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
ax.set_ylabel("Δ Composite Score (all metrics) vs. Top Answer", fontsize=12)
ax.set_title("Single-Card Context: Score Degradation Relative to Top Answer",
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
questions = pd.read_csv("dataset/questions/Questions_latest.csv")
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
ax.set_xticklabels(["Top Answer", "Only Data Card", "Only Finetuning MC", "Only Pretraining MC", "Only Workflow Card"], rotation=45, ha="right")

fig.tight_layout()
savefig("fig6_one_card_validation_heatmap.png")

# ── FIGURE 6 TABLE GENERATION ────────────────────────────────────────────────
print("\n" + "="*80)
print("TABLE FOR FIGURE 6: VALUES IN RANGE [0, Top Answer]")
print("="*80)

# 1. Ensure the pivot is correctly formed
# We look at the actual values in the 'without' column to avoid key errors
available_modalities = df2_joined['without'].unique()

# Mapping for the columns (internal names -> display names)
col_map = {
    "baseline":    "Top Answer",
    "datacard":    "Only DataCard",
    "finetuned":   "Only Finetuning MC",
    "pretrained":  "Only Pretraining MC",
    "workflow":    "Only Workflow Card",
    "workflowcard":"Only Workflow Card" # Handle variant
}

# 2. Extract the pivoted data
# We use the 'Type' from questions as the index (Difficulty/Category)
table_raw = (
    df2_joined.groupby(["Type", "without"])["composite"]
    .mean()
    .unstack("without")
)

# 3. Handle Scaling: [0, Top Answer] 
# Absolute values are already in this range relative to the baseline.
# We will filter and rename to match your request.
cols_to_print = [c for c in col_map.keys() if c in table_raw.columns]
final_table = table_raw[cols_to_print].rename(columns=col_map)

# Remove duplicate 'Only Workflow Card' if both 'workflow' and 'workflowcard' exist
final_table = final_table.loc[:, ~final_table.columns.duplicated()]

print("--- Absolute Mean Scores ---")
print(final_table.round(4).to_string())

# 4. Normalized Table (Scaled so Top Answer = 1.0)
print("\n--- Normalized to Top Answer (Baseline = 1.0) ---")
if "baseline" in table_raw.columns:
    norm_table = table_raw[cols_to_print].div(table_raw["baseline"], axis=0).rename(columns=col_map)
    norm_table = norm_table.loc[:, ~norm_table.columns.duplicated()]
    print(norm_table.round(4).to_string())
else:
    print("Baseline column not found, could not normalize.")

print("="*80)

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
    ax.set_ylabel("Δ Score vs Top Answer", fontsize=10)
    ax.grid(axis="y", alpha=0.3)

axes[0].legend(title="Single Card", fontsize=8, title_fontsize=9)
fig.suptitle("Single-Card Context: Per-Metric Δ vs. Top Answer, by Difficulty", fontsize=13, fontweight="bold")
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


# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 9 — DataCard: Card Size vs. Answer Quality
#
# Uses leaveoneout3.csv (FILE2), keeping only rows where without == "datacard"
# (i.e. questions answered using the DataCard alone).
# For each question/answer, the size of the corresponding DataCard (in KB) is
# looked up from dataset/cards/*.md and plotted against the composite score.
# ═════════════════════════════════════════════════════════════════════════════

import os, re
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

# ── paths ─────────────────────────────────────────────────────────────────────
FILE2      = "results/leaveoneout3.csv"
CARDS_DIR  = Path("dataset/cards")
OUTPUT_DIR = "./figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)

METRICS = ["similarity", "llm_as_judge_1", "llm_as_judge_2"]

DIFFICULTY_PALETTE = {
    "easy":   "#2ca02c",
    "medium": "#ff7f0e",
    "hard":   "#d62728",
}

# ── helpers ───────────────────────────────────────────────────────────────────
def composite(df):
    return df[METRICS].mean(axis=1)

def savefig(name):
    path = os.path.join(OUTPUT_DIR, name)
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  saved → {path}")


# ── 1. Load data ──────────────────────────────────────────────────────────────
print("Loading data …")
df2 = pd.read_csv(FILE2, sep=";")
df2["composite"] = composite(df2)

# Keep only DataCard-only rows
dc = df2[df2["without"] == "workflow"].copy()
print(f"  DataCard rows: {len(dc)}")


# ── 2. Build card-size lookup  ────────────────────────────────────────────────
# Files are named like  "1_data_card.md", "3_data_card.md", etc.
# We extract the use-case number from the filename.
all_md = [f for f in os.listdir(CARDS_DIR) if f.endswith(".md")]
data_md = [f for f in all_md if "data" in f.lower()]

size_by_uc = {}   # {use_case_str: size_in_KB}
for fname in data_md:
    m = re.search(r"(\d+)", fname)
    if m:
        uc = m.group(1)
        size_by_uc[uc] = os.path.getsize(CARDS_DIR / fname) / 1024
print(f"  DataCard sizes found: {size_by_uc}")


# ── 3. Map use-case to each row ───────────────────────────────────────────────
# The 'answer' column (or a similar column) typically encodes the use-case ID.
# We try several heuristics:
#   a) a column named 'use_case' / 'uc' / 'usecase'
#   b) extract digit(s) from the 'answer' column string

def extract_uc(val):
    m = re.search(r"(\d+)", str(val))
    return m.group(1) if m else None

uc_col = None
for candidate in ["use_case", "uc", "usecase", "use_case_id"]:
    if candidate in dc.columns:
        uc_col = candidate
        break

if uc_col:
    dc["uc"] = dc[uc_col].astype(str)
else:
    # Fall back: parse from 'answer' column if it exists
    ref_col = "answer" if "answer" in dc.columns else dc.columns[0]
    dc["uc"] = dc[ref_col].apply(extract_uc)
    print(f"  No explicit use-case column found – extracted from '{ref_col}'")

dc["card_size_kb"] = dc["uc"].map(size_by_uc)

# Drop rows where we couldn't determine size
dc = dc.dropna(subset=["card_size_kb"])
print(f"  Rows after size join: {len(dc)}")

if dc.empty:
    raise RuntimeError(
        "No rows could be matched to a card size. "
        "Check that leaveoneout3.csv contains a column linking to use-case IDs "
        "and that dataset/cards/ holds the DataCard .md files."
    )


# ── 4. Plot ───────────────────────────────────────────────────────────────────
print("Figure 9: DataCard size vs answer quality …")

diff_order = ["easy", "medium", "hard"]
available_diffs = [d for d in diff_order if d in dc["type_"].values]

fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
fig.suptitle(
    "WorkflowCard Size vs Answer Quality",
    fontsize=14, fontweight="bold", y=1.02
)

for ax, metric, mlabel in zip(axes, METRICS, ["Similarity", "LLM Judge 1", "LLM Judge 2"]):
    for diff in available_diffs:
        sub = dc[dc["type_"] == diff]
        if sub.empty:
            continue
        color = DIFFICULTY_PALETTE.get(diff, "gray")
        ax.scatter(
            sub["card_size_kb"], sub[metric],
            color=color, alpha=0.55, s=55, label=diff.capitalize(),
            edgecolors="white", linewidths=0.4, zorder=3
        )

    # Overall regression line
    x_all = dc["card_size_kb"].values
    y_all = dc[metric].values
    mask  = ~np.isnan(x_all) & ~np.isnan(y_all)
    if mask.sum() > 2:
        slope, intercept, r, p, _ = stats.linregress(x_all[mask], y_all[mask])
        x_line = np.linspace(x_all[mask].min(), x_all[mask].max(), 200)
        ax.plot(x_line, slope * x_line + intercept,
                color="black", linewidth=1.8, linestyle="--", zorder=4,
                label=f"Trend  r={r:.2f}")
        ax.text(0.97, 0.05, f"r = {r:.2f}\np = {p:.3f}",
                transform=ax.transAxes, ha="right", va="bottom",
                fontsize=9, bbox=dict(boxstyle="round,pad=0.3",
                                      fc="white", ec="gray", alpha=0.8))

    ax.set_xlabel("DataCard Size (KB)", fontsize=11)
    ax.set_title(mlabel, fontsize=11, fontweight="bold")
    ax.set_ylim(-0.05, 1.05)
    ax.grid(alpha=0.3)
    if ax is axes[0]:
        ax.set_ylabel("Score", fontsize=12)

# Shared legend
handles = [
    mlines.Line2D([], [], color=DIFFICULTY_PALETTE[d], marker="o",
                  linestyle="None", markersize=7, label=d.capitalize())
    for d in available_diffs
] + [
    mlines.Line2D([], [], color="black", linestyle="--", linewidth=1.8, label="Trend (all)")
]
fig.legend(handles=handles, title="Difficulty", loc="lower center",
           ncol=len(available_diffs) + 1, fontsize=10,
           bbox_to_anchor=(0.5, -0.05), frameon=True)

fig.tight_layout()
savefig("fig9_datacard_size_vs_quality.png")
print("Done.")

# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 10 — Per-Question Consistency + Judge Agreement, by Difficulty
#
# A 2-row × 3-column figure (one column per difficulty level).
#
# TOP ROW — Per-question metric variance:
#   For every question, compute the std-dev across the 3 metrics
#   (similarity, llm_as_judge_1, llm_as_judge_2). Plot each question as
#   a horizontal strip: composite mean on the x-axis, std-dev encoded as
#   vertical spread / error bar. Questions are sorted by composite score.
#   Colour = variance magnitude (low→green, high→red).
#
# BOTTOM ROW — Judge agreement scatter:
#   LLM Judge 1 (x) vs LLM Judge 2 (y), one dot per question.
#   Dot colour = similarity score (diverging palette so outliers pop).
#   Dashed identity line y=x; Pearson r annotated.
#
# Both rows are split by difficulty (easy | medium | hard) so the two
# analyses can be read in parallel.
# ═════════════════════════════════════════════════════════════════════════════

import os
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
from matplotlib.gridspec import GridSpec
from scipy import stats

# ── config ────────────────────────────────────────────────────────────────────
FILE2      = "results/leaveoneout3.csv"
OUTPUT_DIR = "./figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)

METRICS       = ["similarity", "llm_as_judge_1", "llm_as_judge_2"]
METRIC_LABELS = ["Similarity", "LLM Judge 1", "LLM Judge 2"]
DIFF_ORDER    = ["easy", "medium", "hard"]

DIFF_ACCENT = {          # title / spine accent colour per difficulty column
    "easy":   "#2ca02c",
    "medium": "#e07b00",
    "hard":   "#d62728",
}

CMAP_VAR  = "RdYlGn_r"   # low variance = green, high = red
CMAP_SIM  = "RdYlBu"     # similarity score: blue-ish = high, red = low

# ── load ──────────────────────────────────────────────────────────────────────
df = pd.read_csv(FILE2, sep=";")
df["composite"] = df[METRICS].mean(axis=1)
df["metric_std"] = df[METRICS].std(axis=1)

# normalise for colour mapping
var_norm  = mcolors.Normalize(vmin=df["metric_std"].min(), vmax=df["metric_std"].max())
sim_norm  = mcolors.Normalize(vmin=0, vmax=1)
cmap_var  = cm.get_cmap(CMAP_VAR)
cmap_sim  = cm.get_cmap(CMAP_SIM)

available_diffs = [d for d in DIFF_ORDER if d in df["type_"].values]
n_cols = len(available_diffs)

# ── figure layout ─────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(6 * n_cols, 12))
gs  = GridSpec(
    2, n_cols,
    figure=fig,
    hspace=0.45, wspace=0.28,
    top=0.91, bottom=0.07,
    left=0.07, right=0.93,
)

axes_top = [fig.add_subplot(gs[0, c]) for c in range(n_cols)]
axes_bot = [fig.add_subplot(gs[1, c]) for c in range(n_cols)]

# ─────────────────────────────────────────────────────────────────────────────
# ROW 0 — Per-question consistency (mean vs std)
# ─────────────────────────────────────────────────────────────────────────────
for col, diff in enumerate(available_diffs):
    ax  = axes_top[col]
    sub = df[df["type_"] == diff].copy().sort_values("composite").reset_index(drop=True)

    colors = cmap_var(var_norm(sub["metric_std"].values))

    # scatter: x = composite mean, y = question index (rank)
    sc = ax.scatter(
        sub["composite"], sub.index,
        c=sub["metric_std"], cmap=CMAP_VAR,
        norm=var_norm,
        s=60, alpha=0.80, zorder=3, edgecolors="white", linewidths=0.4,
    )

    # horizontal error bars showing ±std
    ax.hlines(
        sub.index,
        sub["composite"] - sub["metric_std"],
        sub["composite"] + sub["metric_std"],
        colors=colors, alpha=0.35, linewidth=1.2, zorder=2,
    )

    # thin vertical guide lines
    ax.vlines(sub["composite"], sub.index - 0.3, sub.index + 0.3,
              colors=colors, alpha=0.20, linewidth=0.6, zorder=1)

    # highlight top/bottom 10 % most inconsistent
    thresh_hi = sub["metric_std"].quantile(0.90)
    hi = sub[sub["metric_std"] >= thresh_hi]
    ax.scatter(hi["composite"], hi.index,
               c=hi["metric_std"], cmap=CMAP_VAR, norm=var_norm,
               s=110, marker="D", edgecolors="black", linewidths=0.6, zorder=4)

    ax.set_xlim(-0.05, 1.05)
    ax.set_xlabel("Composite Score (mean of 3 metrics)", fontsize=9)
    ax.set_ylabel("Question rank (sorted by score)", fontsize=9) if col == 0 else None
    ax.yaxis.set_visible(col == 0)
    ax.grid(axis="x", alpha=0.25, linestyle="--")
    ax.set_title(
        f"{diff.capitalize()}  (n={len(sub)})",
        fontsize=11, fontweight="bold",
        color=DIFF_ACCENT[diff], pad=6,
    )

    # per-panel colourbar for variance
    cb = plt.colorbar(sc, ax=ax, fraction=0.035, pad=0.02)
    cb.set_label("Metric Std Dev", fontsize=8)
    cb.ax.tick_params(labelsize=7)

    # annotation: median std
    med_std = sub["metric_std"].median()
    ax.axvline(sub["composite"].median(), color="gray",
               linestyle=":", linewidth=1.0, alpha=0.7)
    ax.text(0.97, 0.02, f"median std = {med_std:.3f}",
            transform=ax.transAxes, ha="right", va="bottom",
            fontsize=8, color="dimgray",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="lightgray", alpha=0.8))

# ─────────────────────────────────────────────────────────────────────────────
# ROW 1 — Judge agreement scatter (Judge1 vs Judge2, colour = similarity)
# ─────────────────────────────────────────────────────────────────────────────
for col, diff in enumerate(available_diffs):
    ax  = axes_bot[col]
    sub = df[df["type_"] == diff].copy()

    sc = ax.scatter(
        sub["llm_as_judge_1"], sub["llm_as_judge_2"],
        c=sub["similarity"], cmap=CMAP_SIM, norm=sim_norm,
        s=55, alpha=0.70, edgecolors="white", linewidths=0.4, zorder=3,
    )

    # identity line y = x
    lims = [-0.05, 1.05]
    ax.plot(lims, lims, "--", color="black", linewidth=1.0, alpha=0.55,
            zorder=1, label="y = x")

    # regression line
    x_v = sub["llm_as_judge_1"].values
    y_v = sub["llm_as_judge_2"].values
    mask = ~np.isnan(x_v) & ~np.isnan(y_v)
    if mask.sum() > 2:
        slope, intercept, r, p, _ = stats.linregress(x_v[mask], y_v[mask])
        x_line = np.linspace(x_v[mask].min(), x_v[mask].max(), 200)
        ax.plot(x_line, slope * x_line + intercept,
                color=DIFF_ACCENT[diff], linewidth=1.8, zorder=2,
                label=f"Fit  r={r:.2f}")
        ax.text(0.03, 0.96,
                f"r = {r:.3f}\np = {p:.3f}\nn = {mask.sum()}",
                transform=ax.transAxes, ha="left", va="top",
                fontsize=8.5,
                bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="lightgray", alpha=0.85))

    ax.set_xlim(*lims)
    ax.set_ylim(*lims)
    ax.set_xlabel("LLM Judge 1", fontsize=9)
    ax.set_ylabel("LLM Judge 2", fontsize=9) if col == 0 else ax.set_ylabel("")
    ax.grid(alpha=0.25, linestyle="--")
    ax.legend(fontsize=7.5, loc="lower right")

    cb = plt.colorbar(sc, ax=ax, fraction=0.035, pad=0.02)
    cb.set_label("Similarity", fontsize=8)
    cb.ax.tick_params(labelsize=7)

# ── global titles / row labels ────────────────────────────────────────────────
fig.text(0.01, 0.73, "ROW 1\nPer-Question\nConsistency",
         va="center", ha="left", fontsize=9, style="italic", color="slategray",
         rotation=90)
fig.text(0.01, 0.30, "ROW 2\nJudge\nAgreement",
         va="center", ha="left", fontsize=9, style="italic", color="slategray",
         rotation=90)

fig.suptitle(
    "Metric Consistency & Judge Agreement  —  by Question Difficulty",
    fontsize=14, fontweight="bold", y=0.96,
)

path = os.path.join(OUTPUT_DIR, "fig10_consistency_and_judge_agreement.png")
plt.savefig(path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved → {path}")

# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 12 — Cross-File Comparisons
#
# TWO independent analyses on one canvas.
#
# ── TOP HALF: Difficulty × Modality — Mean + Spread ─────────────────────────
#
#   Replaces Fig 6's plain heatmap with a richer dual-layer view:
#
#   • 3 rows (easy / medium / hard), 5 columns (baseline + 4 single-cards)
#   • Each cell contains:
#       - A large circle whose FILL COLOUR encodes the mean composite score
#         (RdYlGn, same scale as Fig 6 so it is directly comparable)
#       - The circle RADIUS encodes the IQR (larger = more spread)
#       - A small text annotation: "mean ± std" written inside/below the circle
#   • A secondary mini strip chart to the right of the grid shows the raw
#     score distribution per modality (collapsed across difficulty) so you
#     can see the full shape, not just a summary number.
#
# ── BOTTOM HALF: Single-Card ↔ Leave-One-Out Symmetry (per question) ─────────
#
#   For each of the 4 cards (one column each):
#     x = composite when ONLY this card is present (leaveoneout3.csv)
#     y = composite when this card is REMOVED, all others present
#         (leaveoneout2.csv)
#
#   Quadrant logic:
#     top-right    (x high, y high)  → card alone good AND others good → redundant
#     bottom-right (x high, y low)   → card alone good, but others can't replace it
#                                       → unique & sufficient
#     top-left     (x low, y high)   → card alone weak, but context compensates
#                                       → synergistic / interaction effect
#     bottom-left  (x low, y low)    → card alone bad AND without it bad → essential
#
#   Each quadrant is labelled and lightly shaded.
#   Points coloured by difficulty; regression line + Pearson r annotated.
#   A marginal rug on both axes shows the marginal distributions.
# ═════════════════════════════════════════════════════════════════════════════

import os, warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import matplotlib.cm as cm
from matplotlib.lines import Line2D
from scipy import stats
import seaborn as sns

# ── config ────────────────────────────────────────────────────────────────────
FILE1      = "results/leaveoneout2.csv"
FILE2      = "results/leaveoneout3.csv"
OUTPUT_DIR = "./figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)

METRICS    = ["similarity", "llm_as_judge_1", "llm_as_judge_2"]
DIFF_ORDER = ["easy", "medium", "hard"]

CARD_KEYS  = ["baseline", "datacard", "finetuned", "pretrained", "workflow"]
CARD_LABELS = ["Baseline\n(all cards)", "DataCard\nonly",
               "Finetuning MC\nonly", "Pretraining MC\nonly",
               "Workflow Card\nonly"]
CARD_COLORS = {
    "DataCard":        "#4C72B0",
    "Finetuning MC":   "#DD8452",
    "Pretraining MC":  "#55A868",
    "Workflow Card":   "#C44E52",
}
CARD_MAP_F1 = {
    0: "DataCard",
    1: "Finetuning MC",
    2: "Pretraining MC",
    3: "Workflow Card",
}
CARD_SHORT  = {          # FILE2 key → display name (for symmetry row)
    "datacard":  "DataCard",
    "finetuned": "Finetuning MC",
    "pretrained":"Pretraining MC",
    "workflow":  "Workflow Card",
}
DIFF_COLORS = {"easy": "#2ca02c", "medium": "#e07b00", "hard": "#d62728"}
DIFF_LABELS = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}

SCORE_CMAP  = plt.get_cmap("RdYlGn")
SCORE_NORM  = mcolors.Normalize(vmin=0, vmax=1)

# ── helpers ───────────────────────────────────────────────────────────────────
def composite(df):
    return df[METRICS].mean(axis=1)

def savefig(name):
    path = os.path.join(OUTPUT_DIR, name)
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  saved → {path}")

# ═════════════════════════════════════════════════════════════════════════════
# 1. LOAD
# ═════════════════════════════════════════════════════════════════════════════
print("Loading …")
df1 = pd.read_csv(FILE1, sep=";")
df2 = pd.read_csv(FILE2, sep=";")

df1["card_removed"] = df1["without"].map(CARD_MAP_F1)
df1["composite"]    = composite(df1)
df2["composite"]    = composite(df2)
df2["without"]      = df2["without"].replace({"workflowcard": "workflow"})

available_diffs = [d for d in DIFF_ORDER if d in df2["type_"].values]

# ═════════════════════════════════════════════════════════════════════════════
# 2. BUBBLE GRID DATA  (difficulty × modality, mean + IQR + std)
# ═════════════════════════════════════════════════════════════════════════════
print("Building bubble grid data …")

grid_stats = {}
for diff in available_diffs:
    for key, label in zip(CARD_KEYS, CARD_LABELS):
        sub = df2[(df2["type_"] == diff) & (df2["without"] == key)]["composite"].dropna()
        if sub.empty:
            grid_stats[(diff, key)] = dict(mean=np.nan, std=np.nan, iqr=np.nan, n=0)
            continue
        q25, q75 = sub.quantile([0.25, 0.75])
        grid_stats[(diff, key)] = dict(
            mean=sub.mean(), std=sub.std(), iqr=q75 - q25, n=len(sub)
        )

# ═════════════════════════════════════════════════════════════════════════════
# 3. SYMMETRY DATA
# ═════════════════════════════════════════════════════════════════════════════
print("Building symmetry data …")

Q_COL = None
for c in ["question_id", "question", "q_id", "id", "answer"]:
    if c in df1.columns and c in df2.columns:
        Q_COL = c
        break

sym_data = {}
for sc_key, card_name in CARD_SHORT.items():
    sc = df2[df2["without"] == sc_key].copy()
    lo = df1[df1["card_removed"] == card_name].copy()

    if Q_COL:
        sc = sc[[Q_COL, "composite", "type_"]].rename(columns={"composite":"x","type_":"diff"})
        lo = lo[[Q_COL, "composite"]].rename(columns={"composite":"y"})
        merged = sc.merge(lo, on=Q_COL, how="inner")
    else:
        n = min(len(sc), len(lo))
        merged = pd.DataFrame({
            "x":    sc["composite"].values[:n],
            "y":    lo["composite"].values[:n],
            "diff": sc["type_"].values[:n] if "type_" in sc.columns else ["unknown"]*n,
        })
    sym_data[card_name] = merged

# ═════════════════════════════════════════════════════════════════════════════
# 4. FIGURE
# ═════════════════════════════════════════════════════════════════════════════
print("Rendering figure …")

fig = plt.figure(figsize=(20, 6))
# fig.patch.set_facecolor("#F7F7F7")

outer = gridspec.GridSpec(
    1, 1, figure=fig,
    # height_ratios=[1, 1],
    # hspace=0.52,
    # top=0.93, bottom=0.05, left=0.06, right=0.97,
)

# ─────────────────────────────────────────────────────────────────────────────
# TOP — Bubble grid + strip distributions
# ─────────────────────────────────────────────────────────────────────────────
# top_gs = gridspec.GridSpecFromSubplotSpec(
#     1, 2, subplot_spec=outer[0],
#     width_ratios=[3, 1], wspace=0.06,
# )
# ax_bubble = fig.add_subplot(top_gs[0])
# ax_strip  = fig.add_subplot(top_gs[1])

# n_cols = len(CARD_KEYS)
# n_rows = len(available_diffs)

# # grid coordinates: x = modality, y = difficulty
# xs = np.arange(n_cols)
# ys = np.arange(n_rows)

# # max IQR for radius normalisation
# max_iqr = max(
#     v["iqr"] for v in grid_stats.values()
#     if not np.isnan(v.get("iqr", np.nan))
# )
# MAX_R = 0.38   # max bubble radius in data units

# for ri, diff in enumerate(available_diffs):
#     for ci, key in enumerate(CARD_KEYS):
#         s = grid_stats[(diff, key)]
#         if np.isnan(s["mean"]):
#             continue

#         mean_val = s["mean"]
#         iqr_val  = s["iqr"] if not np.isnan(s["iqr"]) else 0
#         std_val  = s["std"] if not np.isnan(s["std"]) else 0

#         radius   = MAX_R * (iqr_val / max_iqr) if max_iqr > 0 else MAX_R * 0.3
#         face_col = SCORE_CMAP(SCORE_NORM(mean_val))

#         circle = mpatches.Circle(
#             (ci, ri), radius,
#             facecolor=face_col, edgecolor="white",
#             linewidth=1.8, zorder=3,
#         )
#         ax_bubble.add_patch(circle)

#         # mean text inside bubble
#         txt_col = "white" if mean_val < 0.45 or mean_val > 0.75 else "black"
#         ax_bubble.text(ci, ri + 0.04, f"{mean_val:.2f}",
#                        ha="center", va="center", fontsize=9,
#                        fontweight="bold", color=txt_col, zorder=4)
#         # std below
#         ax_bubble.text(ci, ri - radius - 0.08, f"±{std_val:.2f}",
#                        ha="center", va="top", fontsize=7.5,
#                        color="dimgray", zorder=4)

# # axis formatting
# ax_bubble.set_xlim(-0.7, n_cols - 0.3)
# ax_bubble.set_ylim(-0.72, n_rows - 0.28)
# ax_bubble.set_xticks(xs)
# ax_bubble.set_xticklabels(CARD_LABELS, fontsize=9.5)
# ax_bubble.set_yticks(ys)
# ax_bubble.set_yticklabels(
#     [DIFF_LABELS[d] for d in available_diffs],
#     fontsize=11, fontweight="bold",
# )
# for ri, diff in enumerate(available_diffs):
#     ax_bubble.get_yticklabels()[ri].set_color(DIFF_COLORS[diff])

# # subtle grid
# for ci in xs:
#     ax_bubble.axvline(ci, color="#DDDDDD", linewidth=0.7, zorder=0)
# for ri in ys:
#     ax_bubble.axhline(ri, color="#DDDDDD", linewidth=0.7, zorder=0)

# ax_bubble.set_facecolor("#FAFAFA")
# ax_bubble.spines[["top","right","bottom","left"]].set_visible(False)
# ax_bubble.tick_params(length=0)
# ax_bubble.set_title(
#     "Difficulty × Modality — Mean Score (colour) & Score Spread (bubble size = IQR,  ±std below)",
#     fontsize=11, fontweight="bold", pad=10,
# )

# # legend for bubble size
# legend_iqrs = [0.1, 0.2, 0.3]
# for liq in legend_iqrs:
#     r = MAX_R * (liq / max_iqr) if max_iqr > 0 else MAX_R * 0.3
#     ax_bubble.annotate(
#         "", xy=(0, -0.62), xytext=(0, -0.62),
#     )

# # size legend below grid
# for liq in [max_iqr * 0.25, max_iqr * 0.6, max_iqr]:
#     r  = MAX_R * (liq / max_iqr)
#     lc = mpatches.Circle((0, 0), r, fc="none", ec="gray", lw=1.2)
# fig.text(
#     0.08, 0.56,
#     f"Bubble size = IQR\n(max IQR = {max_iqr:.2f})",
#     fontsize=8, color="gray", va="top",
# )

# colourbar
# sm = cm.ScalarMappable(cmap=SCORE_CMAP, norm=SCORE_NORM)
# sm.set_array([])
# cb = plt.colorbar(sm, ax=ax_bubble, fraction=0.025, pad=0.02,
#                   orientation="vertical")
# cb.set_label("Mean Composite Score", fontsize=9)
# cb.ax.tick_params(labelsize=8)

# # RIGHT — strip / violin chart per modality
# ax_strip.set_facecolor("#FAFAFA")
# ax_strip.spines[["top","right","bottom","left"]].set_visible(False)

# strip_positions = np.arange(n_cols)
# for ci, key in enumerate(CARD_KEYS):
#     for ri, diff in enumerate(available_diffs):
#         sub = df2[(df2["type_"] == diff) & (df2["without"] == key)]["composite"].dropna()
#         if sub.empty:
#             continue
#         jitter = np.random.default_rng(ci * 10 + ri).uniform(-0.12, 0.12, len(sub))
#         ax_strip.scatter(
#             sub.values, np.full(len(sub), ci) + jitter,
#             color=DIFF_COLORS[diff], alpha=0.4, s=12, zorder=2,
#         )
#     # IQR bar
#     vals = df2[df2["without"] == key]["composite"].dropna()
#     if not vals.empty:
#         q25, q75 = vals.quantile([0.25, 0.75])
#         med = vals.median()
#         ax_strip.hlines(ci, q25, q75, color="black", linewidth=3.5,
#                         alpha=0.55, zorder=3)
#         ax_strip.scatter([med], [ci], color="black", s=40, zorder=4)

# ax_strip.set_ylim(-0.7, n_cols - 0.3)
# ax_strip.set_xlim(-0.05, 1.05)
# ax_strip.set_yticks(strip_positions)
# ax_strip.set_yticklabels(CARD_LABELS, fontsize=8.5)
# ax_strip.set_xlabel("Composite Score", fontsize=9)
# ax_strip.set_title("Score spread\n(collapsed across difficulty)", fontsize=9,
#                    fontweight="bold", pad=8)
# ax_strip.axvline(0.5, color="gray", linestyle=":", linewidth=0.8, alpha=0.6)
# ax_strip.grid(axis="x", alpha=0.2, linestyle="--")
# ax_strip.tick_params(length=0)

# ─────────────────────────────────────────────────────────────────────────────
# BOTTOM — Symmetry scatter, 4 cards
# ─────────────────────────────────────────────────────────────────────────────
bot_gs = gridspec.GridSpecFromSubplotSpec(
    1, 4, subplot_spec=outer[0], wspace=0.30,
)
axes_sym = [fig.add_subplot(bot_gs[c]) for c in range(4)]

QUADRANT_LABELS = [
    # (x_anchor, y_anchor, text, ha, va)
    (0.02, 0.98, "Synergy\n(context compensates)", "left",  "top",    "#3a86ff"),
    (0.98, 0.98, "Redundant\n(both good)",          "right", "top",    "#8338ec"),
    (0.02, 0.02, "Essential\n(both needed)",         "left",  "bottom", "#d62728"),
    (0.98, 0.02, "Unique\n(card alone sufficient)",  "right", "bottom", "#fb5607"),
]
QUADRANT_SHADES = [
    # (xmin, xmax, ymin, ymax, color)
    (0.0, 0.5, 0.5, 1.0, "#3a86ff"),   # top-left
    (0.5, 1.0, 0.5, 1.0, "#8338ec"),   # top-right
    (0.0, 0.5, 0.0, 0.5, "#d62728"),   # bottom-left
    (0.5, 1.0, 0.0, 0.5, "#fb5607"),   # bottom-right
]

for ax, card_name in zip(axes_sym, CARD_SHORT.values()):
    merged = sym_data[card_name]
    color  = CARD_COLORS[card_name]

    # shaded quadrants
    # for xlo, xhi, ylo, yhi, qcol in QUADRANT_SHADES:
    #     ax.axhspan(ylo, yhi, xmin=xlo, xmax=xhi,
    #                color=qcol, alpha=0.05, zorder=0)

    ax.axvline(0.5, color="lightgray", linewidth=0.8, linestyle="--", zorder=1)
    ax.axhline(0.5, color="lightgray", linewidth=0.8, linestyle="--", zorder=1)

    # identity line
    ax.plot([0, 1], [0, 1], "--", color="black",
            linewidth=0.9, alpha=0.4, zorder=1)

    # scatter per difficulty
    for diff in available_diffs:
        sub = merged[merged["diff"] == diff] if "diff" in merged.columns else merged
        if sub.empty:
            continue
        ax.scatter(sub["x"], sub["y"],
                   color=DIFF_COLORS[diff], alpha=0.35,
                   s=48, edgecolors="white", linewidths=0.4, zorder=3,
                   label=DIFF_LABELS[diff])

    # marginal rugs
    # for diff in available_diffs:
    #     sub = merged[merged["diff"] == diff] if "diff" in merged.columns else merged
    #     if sub.empty:
    #         continue
    #     ax.plot(sub["x"], np.full(len(sub), -0.03),
    #             "|", color=DIFF_COLORS[diff], alpha=0.35,
    #             markersize=4, markeredgewidth=0.7, zorder=2)
    #     ax.plot(np.full(len(sub), -0.03), sub["y"],
    #             "_", color=DIFF_COLORS[diff], alpha=0.35,
    #             markersize=4, markeredgewidth=0.7, zorder=2)

    # regression
    x_v  = merged["x"].values
    y_v  = merged["y"].values
    mask = ~np.isnan(x_v) & ~np.isnan(y_v)
    if mask.sum() > 2:
        slope, intercept, r, p, _ = stats.linregress(x_v[mask], y_v[mask])
        xl = np.linspace(0, 1, 200)
        ax.plot(xl, np.clip(slope * xl + intercept, -0.05, 1.05),
                color=color, linewidth=2.2, zorder=4)
        ax.text(0.50, 0.04,
                f"r={r:.2f}   slope={slope:.2f}",
                transform=ax.transAxes, ha="center", va="bottom",
                fontsize=8, color=color, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.25", fc="white",
                          ec=color, alpha=0.85, lw=1.0))

    # quadrant labels
    # for qx, qy, qtxt, qha, qva, qcol in QUADRANT_LABELS:
    #     ax.text(qx, qy, qtxt,
    #             transform=ax.transAxes, ha=qha, va=qva,
    #             fontsize=6.8, color=qcol, alpha=0.75, style="italic",
    #             linespacing=1.2)

    ax.set_xlim(-0.06, 1.06)
    ax.set_ylim(-0.06, 1.06)
    ax.set_xlabel("Score: only this card present", fontsize=8.5)
    if ax is axes_sym[0]:
        ax.set_ylabel("Score: all other cards present\n(card removed)", fontsize=8.5)
    ax.set_title(card_name, fontsize=10.5, fontweight="bold",
                 color=color, pad=6)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(alpha=0.18, linestyle="--")
    ax.spines[["top","right"]].set_alpha(0.3)
    ax.tick_params(labelsize=8)

# shared legend
diff_handles = [
    Line2D([0],[0], marker="o", color="w",
           markerfacecolor=DIFF_COLORS[d], markersize=8,
           label=DIFF_LABELS[d])
    for d in available_diffs
]
identity_handle = Line2D([0],[0], linestyle="--", color="black",
                          linewidth=0.9, alpha=0.5, label="y = x  (perfect symmetry)")
fig.legend(
    handles=diff_handles + [identity_handle],
    title="Difficulty", title_fontsize=9,
    loc="lower center", ncol=len(available_diffs) + 1,
    fontsize=9, bbox_to_anchor=(0.5, 0.01), frameon=True,
)

# ── section labels ────────────────────────────────────────────────────────────
fig.text(0.005, 0.75, "SPREAD\nANALYSIS", va="center", ha="left",
         fontsize=8, style="italic", color="slategray", rotation=90)
fig.text(0.005, 0.28, "SYMMETRY\nCHECK", va="center", ha="left",
         fontsize=8, style="italic", color="slategray", rotation=90)

fig.suptitle(
    "Cross-File Comparison: Difficulty × Modality Spread  &  Single-Card ↔ Leave-One-Out Symmetry",
    fontsize=13, fontweight="bold", y=0.97,
)

savefig("fig12_spread_and_symmetry.png")
print("Done.")