import os
import time
import pandas as pd
import requests
from pathlib import Path

# --- Configuration ---
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "nemotron-3-nano"  # or "gpt-oss-120b" if you have it loaded in Ollama

# Paths
OUTPUTS_DIR = Path(".")
os.makedirs(OUTPUTS_DIR, exist_ok=True)

# Define the specific card you want to query
SINGLE_CARD_PATH = Path("pipeline2_output/provenancecards/concat.md") 
QUESTIONS_PATH = "dataset/questions/Questions_latest.csv"

# Load questions
QUESTIONS = pd.read_csv(QUESTIONS_PATH)["Question"]

def ollama_chat(prompt: str) -> str:
    """Sends a request to the local Ollama API."""
    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "stream": False, # Set to False to get a single JSON response
        "options": {
            "temperature": 0.0,
            "top_p": 1.0
        }
    }

    try:
        response = requests.post(OLLAMA_URL, json=data)
        response.raise_for_status()
        result = response.json()
        return result['message']['content']
    except Exception as e:
        print(f"Error connecting to Ollama: {e}")
        return None

def process_single_card(card_path: Path):
    if not card_path.exists():
        print(f"Error: Card file not found at {card_path}")
        return

    print(f"Processing card: {card_path.name}")
    out_filepath = OUTPUTS_DIR / f"answer_{card_path.name}"

    # Read the card content
    with open(card_path, "r") as f:
        card_content = f.read()

    # Construct the prompt
    prompt = card_content
    prompt += (
        "\nWith reference to these cards and only these cards, without making up information, "
        "answer the following questions the least amount of words possible, and return a csv file "
        "containing in each row one of the answers, a column for the question and one for the answer, "
        "tab separated, and include no header and no initial phrase:\n"
    )
    prompt += "\n".join(QUESTIONS.tolist())

    # Query Ollama
    response = ollama_chat(prompt)

    if response:
        with open(out_filepath, "w") as f:
            f.write(response)
        print(f"Results saved to: {out_filepath}")

if __name__ == "__main__":
    process_single_card(SINGLE_CARD_PATH)
    print("\nTask complete.")