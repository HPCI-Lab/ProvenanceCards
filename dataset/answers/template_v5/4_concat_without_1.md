How many activities are present in the whole workflow?	3 activities are present in the workflow: DataPreparation, ModelFinetuning, and ModelEvaluation.
What is the final status of the workflow?	Completed.
What is the time to completion of the workflow?	44 hours, 35 minutes, and 44 seconds.
List all the parameters of the first activity of the workflow	The first activity, DataPreparation, uses as parameters: nvidia/Nemotron-Cascade-2-SFT-Data (multi-domain SFT blend covering Math, Science, General Chat, Instruction Following, Safety, Conversational Agent, SWE, Terminal Agent) and nvidia/Nemotron-Cascade-2-RL-data (curated RL blend of IF-RL, multi-domain-RL, MOPD, and SWE-RL). The output is prepared SFT sequences packed to 256K tokens and RL training splits, ready for fine-tuning ingestion.
What hardware was used in the workflow?	4× NVIDIA L40S-48GB GPUs, AMD EPYC 9R14 CPU, 384 GB RAM, running on AWS EC2 g6.12xlarge with Ubuntu 22.04.4 LTS.
Who is responsible for this workflow (person or username or entity)?	empero-ai
What was the specific execution order of the tasks?	1. DataPreparation, 2. ModelFinetuning, 3. ModelEvaluation.
List all parameters for all activites in the workflow	DataPreparation: nvidia/Nemotron-Cascade-2-SFT-Data, nvidia/Nemotron-Cascade-2-RL-data. ModelFinetuning: nvidia/Nemotron-Cascade-2-30B-A3B, prepared SFT and RL datasets, custom pure-PyTorch modeling code, QLoRA rank: 64, LoRA alpha: 32, LoRA dropout: 0.05, target modules: q_proj / k_proj / v_proj / o_proj / up_proj / down_proj, quantisation: 4-bit NF4 + double quant, HF_DEACTIVATE_ASYNC_LOAD: 1. ModelEvaluation: openNemo-Cascade-2-30B-A3B, standard public benchmarks (IMO 2025, IOI 2025, AIME 2025/2026, HMMT Feb25, LiveCodeBench v6, ArenaHard v2, MMLU-Pro, GPQA-Diamond, SWE Verified, ICPC World Finals 2025).
What was the peak RAM consumption during the workflow?	Peak RAM usage was 214 GB (concurrent SFT + RL dataset streaming with packed 256K-token sequences; model shards distributed across 4 GPUs).
Has the model been trained in a distributed setting?	Yes, the model was trained in a distributed setting with model shards distributed across 4 GPUs.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Not specified in the provided cards.
What significant input artifacts are involved in the generation of the finetuned model?	nvidia/Nemotron-Cascade-2-30B-A3B (base model weights), nvidia/Nemotron-Cascade-2-SFT-Data (SFT dataset), nvidia/Nemotron-Cascade-2-RL-data (RL dataset).
What is the total energy use for completing the workflow?	Not specified in the provided cards.
List all input files with size larger than 100Mb	nvidia/Nemotron-Cascade-2-30B-A3B (model weights, ~60 GB), nvidia/Nemotron-Cascade-2-SFT-Data (dataset, size not explicitly stated but covers ~24.8M samples, likely >100MB), nvidia/Nemotron-Cascade-2-RL-data (~2.73 GB).
List all different file types used as input	JSONL (for datasets), PyTorch model weights (BF16), and possibly packed sequence files.
Identify the largest output	openNemo-Cascade-2-30B-A3B — fine-tuned model, size: ~60 GB (model weights).
What is the science domain of the dataset?	Math, Science, General Chat, Instruction Following, Safety, Conversational Agent, Software Engineering, Terminal Agent.
Does the dataset have a predetermined train-test split?	No, only training splits are mentioned for each subset; no explicit test split is described.
How many samples are present in the whole dataset?	73,809 samples in the RL dataset; SFT dataset contains ~24.8M samples.
What is the data type of the ground truth (if present)?	Text (for responses, prompts, and ground_truth fields in some subsets).
What is the specific task for which the dataset was created?	Training and evaluating RL and instruction-following models, including reasoning, instruction following, and software engineering tasks.
What is the size in byte of one sample?	Not specified in the provided cards.
What is the total size of the whole dataset?	~2.73 GB for the RL dataset; SFT dataset size not explicitly stated but likely much larger.
What are the designed uses for this model?	Downstream tasks including reasoning, instruction following, and software engineering; general-purpose reasoning, instruction following, and agentic tasks.
How many epochs have been used in the finetuning?	Approximately 1.5 epochs for SFT (empirically optimal performance after ~1.5 epochs).
How many model parameters (weights) does the model have?	30.87 billion total parameters (~3B active per token).
What is the science domain of the model?	General-purpose reasoning, including Math, Science, Software Engineering, Instruction Following, Conversational Agent, and related domains.
What is the task solved by this model (regression or classification or forecast etc.)?	Language modeling and text generation (causal language modeling, instruction following, reasoning, code generation).
What is the intended use of this model?	General-purpose reasoning, instruction following, software engineering, and agentic tasks; open-source, consumer-GPU-compatible LLM for downstream applications.
What is the size of the final model in Mb?	~60,000 MB (60 GB).
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	QLoRA (Quantized Low-Rank Adapter) fine-tuning with LoRA adapters (r=64, alpha=32, dropout=0.05).
What is the claimed performance of this model?	IMO 2025: 35 pts (Gold Medal); IOI 2025: 439.3 (Gold Medal); AIME 2025: 92.4 (98.6 with TIR); AIME 2026: 90.9 (95.0 with TIR); HMMT Feb25: 94.6; LiveCodeBench v6: 87.2 (88.4 with TIR); ICPC World Finals 2025: 10/12 (Gold Medal); ArenaHard v2: 83.5; SWE Verified: 50.2; MMLU-Pro: 79.8; GPQA-Diamond: 76.1.
Are the performance shown in the pretrained version improved in the finetuning?	Not explicitly stated; the workflow produces a fine-tuned model with the same weights as the base, but with CUDA kernel dependencies removed. Performance is reported as matching the original NVIDIA model (gold medal on IMO/IOI 2025), but no explicit comparison of pre- vs post-finetuning performance is given.