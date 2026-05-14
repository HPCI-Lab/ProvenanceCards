How many activities are present in the whole workflow?	3 activities are present in the workflow: DataPreparation, ModelFinetuning, and ModelEvaluation.
What is the final status of the workflow?	The final status of the workflow is "Completed".
What is the time to completion of the workflow?	The workflow started at 2026-04-02T10:05:33Z and ended at 2026-04-04T06:41:17Z, with a total duration of 44 hours, 35 minutes, and 44 seconds.
List all the parameters of the first activity of the workflow	The first activity, DataPreparation, uses as parameters: nvidia/Nemotron-Cascade-2-SFT-Data (multi-domain SFT blend, JSONL, up to 256K tokens, ~24.8M samples) and nvidia/Nemotron-Cascade-2-RL-data (JSONL, 4 subsets, 73,809 samples).
What hardware was used in the workflow?	The workflow used 4× NVIDIA L40S-48GB GPUs, AMD EPYC 9R14 CPU, and 384 GB RAM, running on AWS EC2 g6.12xlarge instances.
Who is responsible for this workflow (person or username or entity)?	The user responsible for this workflow is "empero-ai".
What was the specific execution order of the tasks?	The execution order was: 1. DataPreparation, 2. ModelFinetuning, 3. ModelEvaluation.
List all parameters for all activites in the workflow	DataPreparation: nvidia/Nemotron-Cascade-2-SFT-Data, nvidia/Nemotron-Cascade-2-RL-data. ModelFinetuning: nvidia/Nemotron-Cascade-2-30B-A3B, prepared SFT and RL datasets, custom pure-PyTorch modeling code. ModelEvaluation: openNemo-Cascade-2-30B-A3B, standard public benchmarks.
What was the peak RAM consumption during the workflow?	Peak RAM usage was 214 GB during concurrent SFT + RL dataset streaming with packed 256K-token sequences.
Has the model been trained in a distributed setting?	Yes, model shards were distributed across 4 GPUs, indicating distributed training.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Not specified in the cards.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts: nvidia/Nemotron-Cascade-2-30B-A3B (base model), nvidia/Nemotron-Cascade-2-SFT-Data (SFT dataset), nvidia/Nemotron-Cascade-2-RL-data (RL dataset).
What is the total energy use for completing the workflow?	Not specified in the cards.
List all input files with size larger than 100Mb	nvidia/Nemotron-Cascade-2-30B-A3B model weights (~60 GB), nvidia/Nemotron-Cascade-2-SFT-Data (~380 GB dataset cache).
List all different file types used as input	JSONL (datasets), BF16 model weights (PyTorch), packed sequences.
Identify the largest output	The largest output is the fine-tuned model openNemo-Cascade-2-30B-A3B (~60 GB).
What is the science domain of the dataset?	The dataset covers Math, Science, General Chat, Instruction Following, Safety, Conversational Agent, Software Engineering, and Terminal Agent domains.
Does the dataset have a predetermined train-test split?	Not explicitly specified in the cards.
How many samples are present in the whole dataset?	Total samples: SFT ~24.8M, RL 73,809; combined total is approximately 24,873,809 samples.
What is the data type of the ground truth (if present)?	Not explicitly specified; datasets are in JSONL format with responses and related fields.
What is the specific task for which the dataset was created?	The datasets were created for supervised fine-tuning (SFT) and reinforcement learning (RL) for reasoning, instruction following, and software engineering tasks.
What is the size in byte of one sample?	Not specified in the cards.
What is the total size of the whole dataset?	Total dataset cache is approximately 380 GB.
What are the designed uses for this model?	Designed uses: reasoning, instruction following, software engineering, and downstream tasks requiring general-purpose reasoning.
How many epochs have been used in the finetuning?	Not specified in the cards.
How many model parameters (weights) does the model have?	The model has 30.87 billion total parameters, with approximately 3 billion active per token.
What is the science domain of the model?	The model is designed for general-purpose reasoning, including Math, Science, Instruction Following, and Software Engineering.
What is the task solved by this model (regression or classification or forecast etc.)?	The model is designed for generative tasks such as reasoning, instruction following, and code generation (not regression/classification/forecast).
What is the intended use of this model?	Intended use: general-purpose reasoning, instruction following, software engineering, and as a foundation for downstream fine-tuning.
What is the size of the final model in Mb?	The final model is approximately 60,000 MB (60 GB).
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using QLoRA (Quantized Low-Rank Adapter).
What is the claimed performance of this model?	Claimed performance: IMO 2025: 35 pts (Gold Medal); IOI 2025: 439.3 (Gold Medal); AIME 2025: 92.4 (98.6 with TIR); AIME 2026: 90.9 (95.0 with TIR); HMMT Feb25: 94.6; LiveCodeBench v6: 87.2 (88.4 with TIR); ICPC World Finals 2025: 10/12 (Gold Medal); ArenaHard v2: 83.5; SWE Verified: 50.2; MMLU-Pro: 79.8; GPQA-Diamond: 76.1.
Are the performance shown in the pretrained version improved in the finetuning?	Not directly specified; however, the evaluation report is for the fine-tuned model, and the workflow is designed to improve performance for downstream tasks.