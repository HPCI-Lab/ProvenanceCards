How many activities are present in the whole workflow?	The workflow contains 3 activities: DataPreparation, ModelFinetuning, and ModelEvaluation.
What is the final status of the workflow?	The final status of the workflow is "Completed" with all activities marked as "success" or "finished".
What is the time to completion of the workflow?	The exact time to completion is not specified in the cards ("~" is used for duration fields).
List all the parameters of the first activity of the workflow	The first activity, DataPreparation, uses as parameters the SFT dataset (nvidia/Nemotron-Cascade-2-SFT-Data) and the RL dataset (nvidia/Nemotron-Cascade-2-RL-data), both in JSONL format, with SFT sequences packed to 256K tokens and RL splits.
What hardware was used in the workflow?	Consumer GPU with at least 17 GB VRAM (for 4-bit quantisation); exact hardware model is not specified.
Who is responsible for this workflow (person or username or entity)?	The workflow is by Empero AI, as indicated in the model and workflow card.
What was the specific execution order of the tasks?	The execution order is: 1. DataPreparation, 2. ModelFinetuning, 3. ModelEvaluation.
List all parameters for all activites in the workflow	DataPreparation: SFT dataset (nvidia/Nemotron-Cascade-2-SFT-Data), RL dataset (nvidia/Nemotron-Cascade-2-RL-data). ModelFinetuning: base model (nvidia/Nemotron-Cascade-2-30B-A3B), prepared SFT and RL datasets, pure-PyTorch modeling code. ModelEvaluation: finetuned model (openNemo-Cascade-2-30B-A3B), standard public benchmarks.
What was the peak RAM consumption during the workflow?	Peak RAM (VRAM) usage is ~17 GB for 4-bit quantisation, ~19 GB with QLoRA (r=64), and ~65 GB at full BF16 precision; CPU RAM is not specified.
Has the model been trained in a distributed setting?	There is no explicit mention of distributed training in the cards.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Total power consumption in Watts is not specified in the cards.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts: nvidia/Nemotron-Cascade-2-30B-A3B (base model), nvidia/Nemotron-Cascade-2-SFT-Data (SFT dataset), nvidia/Nemotron-Cascade-2-RL-data (RL dataset).
What is the total energy use for completing the workflow?	Total energy use is not specified in the cards.
List all input files with size larger than 100Mb	nvidia/Nemotron-Cascade-2-SFT-Data (~24.8M samples, multi-GB), nvidia/Nemotron-Cascade-2-RL-data (~2.73 GB), nvidia/Nemotron-Cascade-2-30B-A3B (model weights, 30B parameters, multi-GB).
List all different file types used as input	Input file types: JSONL (datasets), PyTorch model weights (for nvidia/Nemotron-Cascade-2-30B-A3B).
Identify the largest output	The largest output is openNemo-Cascade-2-30B-A3B, the finetuned model with 30.87B parameters.
What is the science domain of the dataset?	The dataset covers multiple domains: Math, Science, General Chat, Instruction Following, Safety, Conversational Agent, Software Engineering, and Terminal Agent.
Does the dataset have a predetermined train-test split?	The dataset is described as containing only training splits; no explicit train-test split is mentioned.
How many samples are present in the whole dataset?	The SFT dataset contains ~24.8 million samples; the RL dataset contains 73,809 samples.
What is the data type of the ground truth (if present)?	The ground truth, where present, is in text format (e.g., "ground_truth" field in RL data).
What is the specific task for which the dataset was created?	The dataset was created for training and evaluating RL and instruction-following models, including reasoning, agentic, and software engineering tasks.
What is the size in byte of one sample?	The size per sample is not specified; only total dataset sizes are given.
What is the total size of the whole dataset?	The RL dataset is ~2.73 GB; the SFT dataset is multi-GB (exact size not specified, but with ~24.8M samples).
What are the designed uses for this model?	The model is designed for general-purpose reasoning, instruction following, agentic tasks, software engineering, and alignment.
How many epochs have been used in the finetuning?	The SFT model reaches optimal performance after approximately 1.5 epochs.
How many model parameters (weights) does the model have?	The model has 30.87 billion total parameters, with ~3 billion active per token.
What is the science domain of the model?	The model covers multiple domains: Math, Science, Reasoning, General Chat, Instruction Following, Safety, Conversational Agent, Software Engineering, and Terminal Agent.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves text generation tasks, including reasoning, instruction following, and agentic tasks (not regression/classification/forecast).
What is the intended use of this model?	The intended use is for general-purpose reasoning, instruction following, agentic tasks, and software engineering.
What is the size of the final model in Mb?	The model requires ~17 GB VRAM at 4-bit quantisation, which is approximately 17,000 MB; the full model is larger (~65 GB at BF16).
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using QLoRA (Quantized Low-Rank Adaptation) with LoRA rank 64, alpha 32, and LoRA dropout 0.05.
What is the claimed performance of this model?	The model achieves gold medal on IMO 2025 (35 pts), IOI 2025 (439.3), and strong results on AIME, HMMT, LiveCodeBench, ArenaHard, SWE Verified, MMLU-Pro, and GPQA-Diamond.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the finetuned model (Nemotron-Cascade-2-30B-A3B) shows improved performance over the base model (Nemotron-3-Nano-30B-A3B) on multiple benchmarks.