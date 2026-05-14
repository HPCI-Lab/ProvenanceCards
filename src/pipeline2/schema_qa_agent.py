from flowcept.agents.flowcept_agent import FlowceptAgent
import json
import time
import pandas as pd

datapath = "ProvenanceCards/pipeline2_output/jsons/flowcept_buffer.jsonl"

QUESTIONS = pd.read_csv("ProvenanceCards/dataset/questions/Questions_latest.csv")["Question"].tolist()
agent = FlowceptAgent(buffer_path=datapath)
agent.start()
time.sleep(2)  # Give Uvicorn a second to bind to the port

indices = range(28, 32)#[3, 7, 8, 16, 19, 26, 28, 29, 30]

for i, q in enumerate(QUESTIONS): 
    if i not in indices: continue
    
    resp = agent.query(f"Answer the following question in a short way, without making up information, and return all the results in string, even if the question asks you to list, return a string. \n - {QUESTIONS[i]}")

    with open(f"tmp_{i}.txt", "w") as f: 
        try: 
            f.write(resp.result["result_df"])
        except: 
            f.write(resp.result)

    with open(f"sum_{i}.txt", "w") as f: 
        try: 
            f.write(resp.result["summary"])
        except: 
            f.write(resp.result)

agent.stop()

