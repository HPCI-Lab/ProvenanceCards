How many activities are present in the whole workflow?	1
What is the final status of the workflow?	Success
What is the time to completion of the workflow?	20h 00m 00s
List all the parameters of the first activity of the workflow	batch: 64, len: 256k, precision: 4-bit, dropout: 0.05
What hardware was used in the workflow?	4x NVIDIA RTX 4090 (Consumer GPU Target)
Who is responsible for this workflow (person or username or entity)?	Empero AI
What was the specific execution order of the tasks?	qlora-adaptation
List all the parameters for the whole workflow process	batch: 64, len: 256k, precision: 4-bit, dropout: 0.05
What was the peak RAM consumption during the workflow?	answer not found
Has the model been trained in a distributed setting?	answer not found
What was the real-time power consumption (in Watts) of the GPU during the workflow?	answer not found
Which inputs influenced the output in the workflow?	base-weights, rl-dataset
What is the total energy use for completing the workflow?	answer not found
List all input files with size larger than 100Mb	answer not found
List all different file types used as input	Pretrained Hybrid Model (Mamba2/MoE/Attention), RL Training Mixture
Identify the largest output	openNemo-Cascade-2-30B-A3B
What is the science domain of the dataset?	Math, Science, General Chat, Instruction Following, Safety, Conversational Agent, Software Engineering Agent, Terminal Agent
Does the dataset have a predetermined train-test split?	No (only train split is specified)
How many samples are present in the whole dataset?	73,809
What is the data type of the ground truth (if present)?	Text
What is the specific task for which the dataset was created?	Train and evaluate RL and instruction-following models
What is the size in byte of one sample?	answer not found
What is the total size of the whole dataset?	~2.73 GB
What are the designed uses for this model?	Reasoning, agentic capabilities, instruction following, math, code reasoning, knowledge, STEM, alignment, long context, agentic tasks, multilingual tasks
How many epochs have been used in the final training?	1.5
How many model parameters (weights) does the model have?	30B total / 3B active parameters
What is the science domain of the model?	Math, Code Reasoning, Knowledge, STEM, Alignment, Long Context, Agentic, Multilingual
What is the task solved by this model (regression or classification or forecast etc.)?	Text generation, reasoning, instruction following
What is the intended use of this model?	General-purpose reasoning, agentic tasks, instruction following, math, code reasoning, knowledge, STEM, alignment, long context, agentic, multilingual
What is the size of the final model in Mb?	answer not found
What technique was used to train the model?	4-bit Quantization & QLoRA Fine-tuning
What is the claimed performance of this model?	Gold medal performance in IMO 2025 (35 pts), IOI 2025 (439.3), strong scores in math, code reasoning, knowledge, STEM, alignment, agentic, and multilingual benchmarks
Are the performance shown in the pretrained version improved in the finetuning?	Yes