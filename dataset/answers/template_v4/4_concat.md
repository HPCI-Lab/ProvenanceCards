How many activities are present in the whole workflow?	1
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	20h 00m 00s
List all the parameters of the first activity of the workflow	batch: 64, len: 256k, precision: 4-bit, dropout: 0.05
What hardware was used in the workflow?	4x NVIDIA RTX 4090 (Consumer GPU Target)
Who is responsible for this workflow (person or username or entity)?	Empero AI
What was the specific execution order of the tasks?	base-weights, rl-dataset → qlora-adaptation → openNemo-weights-bin
List all the parameters for the whole workflow process	batch: 64, len: 256k, precision: 4-bit, dropout: 0.05
What was the peak RAM consumption during the workflow?	Not specified
Has the model been trained in a distributed setting?	Not specified
What was the real-time power consumption (in Watts) of the GPU during the workflow?	Not specified
Which inputs influenced the output in the workflow?	nvidia/Nemotron-Cascade-2-30B-A3B, nvidia/Nemotron-Cascade-2-RL-data
What is the total energy use for completing the workflow?	Not specified
List all input files with size larger than 100Mb	nvidia/Nemotron-Cascade-2-30B-A3B, nvidia/Nemotron-Cascade-2-RL-data
List all different file types used as input	Pretrained Hybrid Model, RL Training Mixture
Identify the largest output	openNemo-Cascade-2-30B-A3B
What is the science domain of the dataset?	Math, Science, General Chat, Instruction Following, Safety, Conversational Agent, Software Engineering Agent, Terminal Agent
Does the dataset have a predetermined train-test split?	No
How many samples are present in the whole dataset?	73,809 (RL), millions (SFT)
What is the data type of the ground truth (if present)?	Text
What is the specific task for which the dataset was created?	RL and instruction-following model training
What is the size in byte of one sample?	Not specified
What is the total size of the whole dataset?	~2.73 GB (RL), much larger for SFT
What are the designed uses for this model?	Reasoning, agentic capabilities, instruction following, math, code, chat, science, safety, SWE, terminal agent
How many epochs have been used in the final training?	1.5 (SFT stage)
How many model parameters (weights) does the model have?	30.87B
What is the science domain of the model?	Math, Science, Code, Reasoning, General-purpose
What is the task solved by this model (regression or classification or forecast etc.)?	Text generation
What is the intended use of this model?	Train and evaluate RL and instruction-following models; general-purpose reasoning and agentic tasks
What is the size of the final model in Mb?	~17,000 MB (4-bit quantized)
What technique was used to train the model?	4-bit Quantization & QLoRA Fine-tuning
What is the claimed performance of this model?	Gold medal in IMO 2025 (35 pts), IOI 2025 (439.3), strong results in math, code, knowledge, agentic, and instruction following benchmarks
Are the performance shown in the pretrained version improved in the finetuning?	Performance is consistent with base model; loss parity achieved