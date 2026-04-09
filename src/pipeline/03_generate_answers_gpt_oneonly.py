
from pathlib import Path
from tqdm import tqdm
import os
import time
import pandas as pd
import requests

key = 'AqGqRAP5HKB4rqMcx6SuYd8IjQx8RLNLM0JDEgGJsUN7LBCWC7N1JQQJ99BGACYeBjFXJ3w3AAABACOGJ4nd'
endpoint = "https://aoai-eus-wrkflowecosystems.openai.azure.com/"
deployment_name = "gpt-4" # Change this to your working deployment name
api_version = "2023-05-15"

# 2. Construct the full URL
# Ensure there are no double slashes if the endpoint ends with /
url = f"{endpoint.rstrip('/')}/openai/deployments/{deployment_name}/chat/completions?api-version={api_version}"

# 3. Set the headers
headers = {
    "Content-Type": "application/json",
    "api-key": key
}


OUTPUTS_DIR = Path("dataset/answers")
os.makedirs(OUTPUTS_DIR, exist_ok=True)
INPUTS_DIR = Path("dataset/concat")

QUESTIONS = pd.read_csv("dataset/questions/Questions_Nicola.csv")["Question"]

def gemini_chat(messages: list) -> dict:
    # Payload
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": messages}
        ],
        "temperature": 0.0,
        "top_p": 1.0,
        "max_tokens": 800
    }

    # Send request
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
    return None

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
    FILES = [f for f in os.listdir(INPUTS_DIR) if "without" not in f]
    run_benchmark(FILES)
    FILES = os.listdir(Path("dataset/cards"))
    run_benchmark(FILES)
    print("\nBenchmark complete.")
