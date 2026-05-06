
import pandas as pd
from pathlib import Path

USECASE = 1
TYPE = "concat_without_0"
ANSWERS = Path(f"dataset/answers/template_v5/{USECASE}_{TYPE}.md") # question, answer
QUESTIONS = Path("dataset/questions/Questions_latest.csv") # question
GTS = Path(f"dataset/gt/{USECASE}_answers.csv") # "q";"a";"reasoning"
SCORES_LEAVEONEOUT = Path("results/leaveoneout2.csv") # type_;category;answer;usecase;without;similarity;llm_as_judge_1;llm_as_judge_2
SCORES_ONEONLY = Path("results/leaveoneout3.csv") # type_;category;answer;usecase;without;similarity;llm_as_judge_1;llm_as_judge_2

answers = pd.read_csv(ANSWERS, sep="\t", header=None)
answers.columns = ["question", "answer"]
questions = pd.read_csv(QUESTIONS)
gts = pd.read_csv(GTS, sep=";")
if "without" in TYPE: 
    scores = pd.read_csv(SCORES_LEAVEONEOUT, sep=";")
    without = int(TYPE.split("_")[-1])
else: 
    scores = pd.read_csv(SCORES_ONEONLY, sep=";")
# 1. Filter scores first
filtered_scores = scores[
    (scores['usecase'] == USECASE) & 
    (scores['without'] == without)
].copy()

# 2. Map the indices to the actual content
# We use .iloc or .loc based on how your indices are stored.
# If 'answer' in scores is the integer index of the row in the answers df:
filtered_scores['question_text'] = filtered_scores['answer'].apply(lambda x: answers.iloc[x]['question'])
filtered_scores['answer_text'] = filtered_scores['answer'].apply(lambda x: answers.iloc[x]['answer'])

filtered_scores['gt_answer'] = filtered_scores['answer'].apply(lambda x: gts.iloc[x]['a'])
# Optional: if you also need the reasoning from GT
filtered_scores['gt_reasoning'] = filtered_scores['answer'].apply(lambda x: gts.iloc[x]['reasoning'])

# 3. If you need extra metadata from the original QUESTIONS file:
# This assumes the 'question' index in your logic maps to the QUESTIONS csv
result = filtered_scores.merge(
    questions, 
    left_on='answer', # or whichever column holds the Q index
    right_index=True, 
    how='inner'
)

# 4. Final Selection
filtered_scores.to_csv(f"{USECASE}_{TYPE}.csv", sep=";", columns=["llm_as_judge_1","llm_as_judge_2","answer_text","gt_answer","question_text","type_","category","answer","usecase","without","similarity","gt_reasoning"])