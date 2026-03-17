
import time
import json
import subprocess
import requests
import pandas as pd
from pathlib import Path
from datetime import datetime
from tqdm import tqdm

OLLAMA_URL  = "http://localhost:11434/api/chat"
OUTPUTS_DIR = Path("outputs")
RESULTS_DIR = Path("results")

MODELS_TO_TEST = [
    # {"name": "Qwen2.5-Coder-7B", "model": "qwen2.5-coder:7b"},
    # {"name": "Llama-3.2-3B",     "model": "llama3.2:3b"},
    # {"name": "Phi-4-Mini",       "model": "phi4-mini"},
    {"name": "Mistral-7B-v0.3",  "model": "mistral:7b"},
]

def ollama_chat(model: str, messages: list, temperature: float = 0.1, num_predict: int = None) -> dict:
    payload = {
        "model":   model,
        "messages": messages,
        "stream":  False,
        "options": {"temperature": temperature},
    }
    if num_predict: 
        payload["num_predict"] = num_predict
    resp = requests.post(OLLAMA_URL, json=payload)
    resp.raise_for_status()
    return resp.json()


class FastLargeFileDescriber:
    def __init__(self, model: str):
        self.model = model

    def chunk_file(self, content: str, chunk_size: int = 3000) -> list[str]:
        return [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]

    def describe_large_file(self, filepath: str) -> dict:
        with open(filepath, "r") as f:
            source_text = f.read()

        chunks = self.chunk_file(source_text)
        chunk_summaries = []
        chunk_token_counts = []

        print(f"  📄 {len(chunks)} chunks — processing...")

        for i, chunk in enumerate(tqdm(chunks, desc="  chunks")):
            prompt   = f"Summarize the technical structure of this part ({i+1}/{len(chunks)}):\n\n{chunk}"
            response = ollama_chat(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                # num_predict=200,
            )
            chunk_summaries.append(response["message"]["content"])
            chunk_token_counts.append(response.get("eval_count", 0))

        final_prompt = ("Combine these partial descriptions into one master technical overview:\n\n" + "\n".join(chunk_summaries))
        final_response = ollama_chat(
            model=self.model,
            messages=[{"role": "user", "content": final_prompt}],
            # num_predict=200,
        )
        final_token_count   = final_response.get("eval_count", 0)
        total_tokens        = sum(chunk_token_counts) + final_token_count

        return {
            "final_description":   final_response["message"]["content"],
            "chunk_summaries":     chunk_summaries,
            "chunk_token_counts":  chunk_token_counts,
            "final_token_count":   final_token_count,
            "total_tokens":        total_tokens,
            "source_text":         source_text,
            "num_chunks":          len(chunks),
        }


class OllamaBenchmark:
    def __init__(self, models: list[dict], outputs_dir: Path = OUTPUTS_DIR):
        self.models = models
        self.results = []
        self.run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.outputs_dir = outputs_dir / self.run_id
        self.outputs_dir.mkdir(parents=True, exist_ok=True)
        print(f"📂 Saving outputs to: {self.outputs_dir}")

    def pull_model(self, model: str):
        print(f"  Checking/pulling '{model}' via Ollama...")
        subprocess.run(["ollama", "pull", model], check=True)

    def _save_model_output(self, model_name: str, filepath: str, result: dict, duration: float):
        safe_model = model_name.replace("/", "_").replace(":", "-")
        safe_file  = filepath.split("/")[-1]
        out_path   = self.outputs_dir / f"{safe_file}__{safe_model}.json"

        payload = {
            "run_id": self.run_id,
            "model_name": model_name,
            "input_file": str(filepath),
            "duration_sec": round(duration, 4),
            "total_tokens": result["total_tokens"],
            "tokens_per_sec": round(result["total_tokens"] / duration, 2) if duration > 0 else 0,
            "num_chunks": result["num_chunks"],
            "final_description": result["final_description"],
            "chunk_summaries": result["chunk_summaries"],
            "chunk_token_counts": result["chunk_token_counts"],
            "final_token_count": result["final_token_count"],
            "source_text": result["source_text"],
        }

        with open(out_path, "w") as f:
            json.dump(payload, f, indent=2)

        print(f"  💾 Saved → {out_path}")
        return out_path

    def run_benchmark(self, files_to_describe: list[str] | str):
        if isinstance(files_to_describe, str):
            files_to_describe = [files_to_describe]

        for filepath in files_to_describe:
            print(f"\n{'='*55}\n📁 File: {filepath}\n{'='*55}")
            for m_info in self.models:
                print(f"\n>>> Model: {m_info['name']}")
                self.pull_model(m_info["model"])

                describer = FastLargeFileDescriber(m_info["model"])

                start    = time.time()
                result   = describer.describe_large_file(filepath)
                duration = time.time() - start

                output_path = self._save_model_output(m_info["name"], filepath, result, duration)

                self.results.append({
                    "Model":            m_info["name"],
                    "File":             filepath,
                    "Tokens/Sec":       round(result["total_tokens"] / duration, 2) if duration > 0 else 0,
                    "Total Time (s)":   round(duration, 2),
                    "Tokens Generated": result["total_tokens"],
                    "Num Chunks":       result["num_chunks"],
                    "Output File":      str(output_path),
                })

    def save_results(self, outputs_dir=RESULTS_DIR):
        outputs_dir.mkdir(parents=True, exist_ok=True)

        df = pd.DataFrame(self.results)
        csv_path = outputs_dir / "benchmark_results.csv"
        df.to_csv(csv_path, index=False)
        print(f"\n📊 Results saved to {csv_path}")


if __name__ == "__main__":
    FILES = [
        # "jsons/nasa_F.jsonl",
        # "jsons/nasa_Y.json",
        # "jsons/train_test_splits_F.jsonl",
        # "jsons/train_test_splits_Y.json",
        # "jsons/turbolence_F.jsonl",
        # "jsons/turbolence_Y.json",
        # "jsons/example_F.jsonl",
        # "jsons/example_Y.json",
        # "jsons/fusion_F.jsonl",
        # "jsons/fusion_Y.json",
        "cards/nasa_F.md",
        "cards/nasa_Y.md",
        "cards/train_test_splits_F.md",
        "cards/train_test_splits_Y.md",
        "cards/turbolence_F.md",
        "cards/turbolence_Y.md",
        "cards/example_F.md",
        "cards/example_Y.md",
        "cards/fusion_F.md",
        "cards/fusion_Y.md",
    ]

    tester = OllamaBenchmark(MODELS_TO_TEST)
    tester.run_benchmark(FILES)
    tester.save_results()
    print("\nBenchmark complete.")
