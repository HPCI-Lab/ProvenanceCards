import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('results/leaveoneout2.csv', sep=';')
sns.set_theme(style="whitegrid")

# 1. Performance Metrics by Category
plt.figure(figsize=(10, 6))
cat_metrics = df.groupby('category')[['coverage_acc', 'coverage_F1', 'correctness']].mean().reset_index()
cat_metrics_melted = cat_metrics.melt(id_vars='category', var_name='Metric', value_name='Average Value')
sns.barplot(data=cat_metrics_melted, y='Metric', x='Average Value', hue='category')
plt.title('Average Performance Metrics by Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('metrics_by_category.png')

# 2. Impact of "Leave One Out" on Correctness (Heatmap)
plt.figure(figsize=(12, 6))
loo_impact = df.groupby(['without', 'category'])['correctness'].mean().unstack()
sns.heatmap(loo_impact, annot=True, cmap='RdYlGn', fmt=".2f")
plt.yticks([i +0.5 for i in range(4)], ["Without Datacard", "Finetuned Modelcard", "Pretrained Modelcard", "Without Workflowcard"], rotation=0)
plt.title('Correctness: Leaving One Component Out (rows) per Category')
plt.tight_layout()
plt.savefig('loo_impact_heatmap.png')

plt.figure(figsize=(12, 6))
loo_impact = df.groupby(['without', 'category'])['coverage_F1'].mean().unstack()
sns.heatmap(loo_impact, annot=True, cmap='RdYlGn', fmt=".2f")
plt.yticks([i +0.5 for i in range(4)], ["Without Datacard", "Without Finetuned Modelcard", "Without Pretrained Modelcard", "Without Workflowcard"], rotation=0)
plt.title('Keyword F1 Acc: Leaving One Component Out (rows) per Category')
plt.tight_layout()
plt.savefig('loo_coverage_f1_heatmap.png')

plt.figure(figsize=(12, 6))
loo_impact = df.groupby(['without', 'category'])['coverage_acc'].mean().unstack()
sns.heatmap(loo_impact, annot=True, cmap='RdYlGn', fmt=".2f")
plt.yticks([i +0.5 for i in range(4)], ["Without Datacard", "Finetuned Modelcard", "Pretrained Modelcard", "Without Workflowcard"], rotation=0)
plt.title('Keyword Accuracy: Leaving One Component Out (rows) per Category')
plt.tight_layout()
plt.savefig('loo_coverage_acc_heatmap.png')

# 3. Distribution of Correctness across Types
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='type_', y='correctness')
plt.title('Distribution of Correctness by Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('correctness_distribution_by_type.png')

# 4. Coverage vs Correctness (Scatter plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='coverage_acc', y='correctness', hue='category', alpha=0.6)
plt.title('Correlation: Coverage Accuracy vs Correctness')
plt.tight_layout()
plt.savefig('coverage_vs_correctness.png')