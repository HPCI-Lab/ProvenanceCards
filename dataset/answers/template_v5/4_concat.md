How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	44h 35m 44s
List all the parameters of the first activity of the workflow	Inputs: nvidia/Nemotron-Cascade-2-SFT-Data (multi-domain SFT blend), nvidia/Nemotron-Cascade-2-RL-data (curated RL blend); Outputs: Prepared SFT sequences packed to 256K tokens and RL training splits, ready for fine-tuning ingestion
What hardware was used in the workflow?	4× NVIDIA L40S-48GB GPUs, AMD EPYC 9R14 CPU, 384 GB RAM, hosted on AWS EC2 g6.12xlarge
Who is responsible for this workflow (person or username or entity)?	empero-ai
What was the specific execution order of the tasks?	1. DataPreparation 2. ModelFinetuning 3. ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: Inputs: nvidia/Nemotron-Cascade-2-SFT-Data, nvidia/Nemotron-Cascade-2-RL-data; Outputs: Prepared SFT and RL splits. ModelFinetuning: Inputs: nvidia/Nemotron-Cascade-2-30B-A3B, prepared SFT/RL datasets, custom PyTorch code; Outputs: openNemo-Cascade-2-30B-A3B. ModelEvaluation: Inputs: openNemo-Cascade-2-30B-A3B, public benchmarks; Outputs: evaluation_report.
What was the peak RAM consumption during the workflow?	214 GB
Has the model been trained in a distributed setting?	Yes, model shards distributed across 4 GPUs
What was the total power consumption in Watts of the GPU(s) during the workflow?	Not specified in the cards
What significant input artifacts are involved in the generation of the finetuned model?	nvidia/Nemotron-Cascade-2-30B-A3B (base model), nvidia/Nemotron-Cascade-2-SFT-Data (SFT dataset), nvidia/Nemotron-Cascade-2-RL-data (RL dataset)
What is the total energy use for completing the workflow?	Not specified in the cards
List all input files with size larger than 100Mb	nvidia/Nemotron-Cascade-2-30B-A3B (model weights, ~60 GB), nvidia/Nemotron-Cascade-2-SFT-Data (~380 GB dataset cache)
List all different file types used as input	JSONL (datasets), PyTorch model weights (BF16), packed sequences, possibly .bin or .pt for weights
Identify the largest output	openNemo-Cascade-2-30B-A3B (fine-tuned model, ~60 GB)
What is the science domain of the dataset?	Math, Science, General Chat, Instruction Following, Safety, Conversational Agent, Software Engineering, Terminal Agent
Does the dataset have a predetermined train-test split?	No explicit mention of a train-test split; described as training samples
How many samples are present in the whole dataset?	SFT: ~24.8M samples; RL: 73,809 samples; total: ~24,873,809 samples
What is the data type of the ground truth (if present)?	Text (for responses, prompts, and ground truth fields)
What is the specific task for which the dataset was created?	Training and evaluating RL and instruction-following models (reasoning, instruction following, software engineering, agentic tasks)
What is the size in byte of one sample?	Not specified in the cards
What is the total size of the whole dataset?	SFT: ~380 GB (cache), RL: ~2.73 GB; total >380 GB
What are the designed uses for this model?	Reasoning, instruction following, software engineering, agentic tasks, text generation, downstream QLoRA fine-tuning
How many epochs have been used in the finetuning?	Approximately 1.5 epochs (for SFT stage, as per SFT data card)
How many model parameters (weights) does the model have?	30.87B total parameters (~3B active per token)
What is the science domain of the model?	General-purpose reasoning, Math, Science, Software Engineering, Conversational AI
What is the task solved by this model (regression or classification or forecast etc.)?	Text generation (causal language modeling, reasoning, instruction following)
What is the intended use of this model?	General-purpose reasoning, instruction following, software engineering, agentic tasks, text generation
What is the size of the final model in Mb?	~60,000 MB (60 GB)
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	QLoRA (4-bit quantization, LoRA rank 64, LoRA alpha 32, LoRA dropout 0.05)
What is the claimed performance of this model?	IMO 2025: 35 pts (Gold Medal); IOI 2025: 439.3 (Gold Medal); AIME 2025: 92.4 (98.6 with TIR); AIME 2026: 90.9 (95.0 with TIR); HMMT Feb25: 94.6; LiveCodeBench v6: 87.2 (88.4 with TIR); ICPC World Finals 2025: 10/12 (Gold Medal); ArenaHard v2: 83.5; SWE Verified: 50.2; MMLU-Pro: 79.8; GPQA-Diamond: 76.1
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the workflow describes fine-tuning on SFT and RL data to produce a model with strong reasoning and agentic capabilities, achieving gold medal performance on IMO 2025 and IOI 2025.