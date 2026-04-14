
from pathlib import Path
from tqdm import tqdm
import os
import time
from google import genai
import pandas as pd
client = genai.Client(api_key=open(".gkey").read())

OUTPUTS_DIR = Path("dataset/answers")
os.makedirs(OUTPUTS_DIR, exist_ok=True)
INPUTS_DIR = Path("dataset/concat")

QUESTIONS = pd.read_csv("dataset/questions/Questions_Nicola.csv")["Question"]

print("List of models that support generateContent:\n")
for m in client.models.list():
    for action in m.supported_actions:
        if action == "generateContent":
            print(m.name)

def gemini_chat(messages: list) -> dict:
    response = client.models.generate_content(
        model="models/gemini-2.0-flash-lite", contents=messages
    )
    return response.text

def run_benchmark(files_to_describe: list[str] | str):
    if isinstance(files_to_describe, str):
        files_to_describe = [files_to_describe]

    for filepath in tqdm(files_to_describe):
        inp_filepath = INPUTS_DIR / filepath
        out_filepath = OUTPUTS_DIR / filepath
        
        if os.path.exists(out_filepath): 
            continue

        prompt = open(inp_filepath, "r").read()

        prompt += "\nWith reference to these cards and only these cards, without making up information, answer the following questions with max 200 words for each, and return a csv file containing in each row one of the answers, a column for the question and one for the answer, tab separated, and include no header and no initial phrase:\n"
        prompt += "\n".join(QUESTIONS.tolist())

        response = gemini_chat(messages=prompt)

        with open(out_filepath, "w") as f:
            f.write(response) 
        
        time.sleep(7)


if __name__ == "__main__":
    FILES = os.listdir(INPUTS_DIR)
    run_benchmark(FILES)
    print("\nBenchmark complete.")
