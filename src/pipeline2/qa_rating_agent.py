from flowcept.agents.flowcept_agent import FlowceptAgent
import json
import time
import pandas as pd

datapath = "ProvenanceCards/pipeline2_output/jsons/flowcept_buffer.jsonl"

QUESTIONS = pd.read_csv("ProvenanceCards/dataset/answers/template_v5/tmp/nemotron-nano-3.csv")["Question"].tolist()
ANSWERS = pd.read_csv("ProvenanceCards/dataset/answers/template_v5/tmp/nemotron-nano-3.csv")["Answer"].tolist()
agent = FlowceptAgent(buffer_path=datapath)
agent.start()
time.sleep(2)  # Give Uvicorn a second to bind to the port

#indices = range(28, 32)#[3, 7, 8, 16, 19, 26, 28, 29, 30]

for i, (q, a) in enumerate(zip(QUESTIONS, ANSWERS)): 
    #if i not in indices: continue
    
    resp = agent.query(f"Rate the following answer based on the question given, on a scale from 0.0 to 1.0. \n - Question: {q}. \n Answer: {a}. \n Return just the single rating number in a pandas dataframe, nothing else.")

    with open(f"rnemotmp_{i}.txt", "w") as f: 
        try: 
            f.write(resp.result["result_df"])
        except: 
            f.write(resp.result)

    with open(f"rnemosum_{i}.txt", "w") as f: 
        try: 
            f.write(resp.result["summary"])
        except: 
            f.write(resp.result)

agent.stop()

