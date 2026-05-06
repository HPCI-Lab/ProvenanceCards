How many activities are present in the whole workflow?	There are 3 activities present in the whole workflow: DataPreparation, ModelFinetuning, and ModelEvaluation.
What is the final status of the workflow?	The final status of the workflow is Completed, with all activities marked as success.
What is the time to completion of the workflow?	The exact time to completion is not specified in the cards; the fields for started_at, ended_at, and duration are marked as ~.
List all the parameters of the first activity of the workflow	The first activity, DataPreparation, uses as parameters the input datasets: nvidia/Nemotron-Cascade-2-SFT-Data and nvidia/Nemotron-Cascade-2-RL-data.
What hardware was used in the workflow?	Consumer GPU with ≥17 GB VRAM was used, supporting 4-bit NF4 quantisation; exact hardware is not specified.
Who is responsible for this workflow (person or username or entity)?	The workflow is associated with Empero AI, as indicated by the output artifact openNemo-Cascade-2-30B-A3B hosted at https://huggingface.co/empero-ai/openNemo-Cascade-2-30B-A3B.
What was the specific execution order of the tasks?	The execution order of the tasks is: 1. DataPreparation, 2. ModelFinetuning, 3. ModelEvaluation.
List all parameters for all activites in the workflow	DataPreparation: input datasets (nvidia/Nemotron-Cascade-2-SFT-Data, nvidia/Nemotron-Cascade-2-RL-data); ModelFinetuning: model (nvidia/Nemotron-Cascade-2-30B-A3B), prepared datasets, pure-PyTorch modeling code, QLoRA rank: 64, LoRA alpha: 32, LoRA dropout: 0.05, target modules: q_proj / k_proj / v_proj / o_proj / up_proj / down_proj, quantisation: 4-bit NF4 + double quant, HF_DEACTIVATE_ASYNC_LOAD: 1; ModelEvaluation: fine-tuned model, public benchmarks.
What was the peak RAM consumption during the workflow?	The peak RAM consumption is not specified in the cards.
Has the model been trained in a distributed setting?	There is no explicit mention of distributed training in the cards; the workflow is described as compatible with consumer GPUs.
What was the total power consumption in Watts of the GPU(s) during the workflow?	The total power consumption in Watts is not specified in the cards.
What significant input artifacts are involved in the generation of the finetuned model?	The significant input artifacts are: nvidia/Nemotron-Cascade-2-30B-A3B (base model), nvidia/Nemotron-Cascade-2-SFT-Data (SFT dataset), and nvidia/Nemotron-Cascade-2-RL-data (RL dataset).
What is the total energy use for completing the workflow?	The total energy use for completing the workflow is not specified in the cards.
List all input files with size larger than 100Mb	nvidia/Nemotron-Cascade-2-SFT-Data (~24.8M samples, packed sequences up to 256K tokens), nvidia/Nemotron-Cascade-2-RL-data (~2.73 GB), nvidia/Nemotron-Cascade-2-30B-A3B (model weights, 30.87B parameters).
List all different file types used as input	The input file types are JSONL (for datasets) and PyTorch model weights (for the model).
Identify the largest output	The largest output is openNemo-Cascade-2-30B-A3B, the pure-PyTorch fine-tuned model with 30.87B parameters.
What is the science domain of the dataset?	The dataset covers multiple science domains: Math, Science (physics, chemistry, biology), General Chat, Instruction Following, Safety, Conversational Agent, Software Engineering, and Terminal Agent.
Does the dataset have a predetermined train-test split?	The dataset is described as containing training samples; there is no mention of a predetermined train-test split.
How many samples are present in the whole dataset?	The total number of samples in the RL dataset is 73,809; the SFT dataset contains ~24.8M samples.
What is the data type of the ground truth (if present)?	The ground truth, if present, is in text format (modality: Text).
What is the specific task for which the dataset was created?	The dataset was created for training and evaluating RL and instruction-following models, including reasoning, agentic, and software engineering tasks.
What is the size in byte of one sample?	The size in byte of one sample is not specified in the cards.
What is the total size of the whole dataset?	The total disk size of the RL dataset is ~2.73 GB; the SFT dataset is not explicitly quantified but contains ~24.8M samples.
What are the designed uses for this model?	The model is designed for general-purpose reasoning, instruction following, agentic tasks, software engineering, and tool use.
How many epochs have been used in the finetuning?	The SFT model reaches optimal performance after approximately 1.5 epochs.
How many model parameters (weights) does the model have?	The model has 30.87 billion total parameters, with ~3 billion active per token.
What is the science domain of the model?	The model covers multiple domains: Math, Science, General Chat, Instruction Following, Safety, Conversational Agent, Software Engineering, Terminal Agent.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves general-purpose text generation, reasoning, instruction following, agentic coding, and tool use tasks; it is not limited to regression or classification.
What is the intended use of this model?	The intended use is for general-purpose reasoning, instruction following, agentic tasks, software engineering, and tool use.
What is the size of the final model in Mb?	The size of the final model is not specified in Mb, but the model has 30.87B parameters and requires ~17 GB VRAM at 4-bit quantisation.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using QLoRA (rank: 64, LoRA alpha: 32, LoRA dropout: 0.05) and bitsandbytes 4-bit NF4 quantisation.
What is the claimed performance of this model?	The model achieves gold medal performance on IMO 2025 (35 pts), IOI 2025 (439.3), AIME 2025 (92.4), AIME 2026 (90.9), HMMT Feb25 (94.6), LiveCodeBench v6 (87.2), ICPC World Finals 2025 (10/12), ArenaHard v2 (83.5), SWE Verified (50.2), MMLU-Pro (79.8), GPQA-Diamond (76.1).
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the performance shown in the fine-tuned version (Nemotron-Cascade-2-30B-A3B) is improved compared to the pretrained base (Nemotron-3-Nano-30B-A3B), as evidenced by higher scores in multiple benchmarks.