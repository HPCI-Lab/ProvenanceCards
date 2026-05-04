from flowcept.agents.flowcept_agent import FlowceptAgent
import json

agent = FlowceptAgent(buffer_path="flowcept_buffer.jsonl")
# Or load a list of messages directly
# agent = FlowceptAgent(buffer_messages=msgs)
agent.start()
resp = agent.query("how many tasks?")
print(resp)
print(json.loads(resp))
agent.stop()