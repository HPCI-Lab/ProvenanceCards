How many activities are present in the whole workflow?	There are 3 activities in the workflow: DataPreparation, ModelFinetuning, and ModelEvaluation.
What is the final status of the workflow?	The final status of the workflow is Completed.
What is the time to completion of the workflow?	The workflow started at 2024-03-12T08:14:22Z and ended at 2024-03-13T02:47:09Z, with a total duration of 18 hours, 32 minutes, and 47 seconds.
List all the parameters of the first activity of the workflow	The first activity, DataPreparation, takes as input: HealthCareMagic-100k (100,000 real patient–doctor conversations) and iCliniq-10k (10,000 real patient–doctor conversations), both formatted as instruction/input/output JSON triples.
What hardware was used in the workflow?	The workflow used 8× NVIDIA A100-SXM4-80GB GPUs (NVLink), Intel Xeon Platinum 8375C CPU, and 1.1 TB RAM, running on AWS EC2 p4d.24xlarge with Ubuntu 22.04.3 LTS.
Who is responsible for this workflow (person or username or entity)?	The workflow was executed by the user prithivMLmods.
What was the specific execution order of the tasks?	The execution order was: 1. DataPreparation, 2. ModelFinetuning, 3. ModelEvaluation.
List all parameters for all activites in the workflow	DataPreparation: HealthCareMagic-100k, iCliniq-10k; ModelFinetuning: meta-llama/Llama-3.2-3B-Instruct, avaliev/chat_doctor; ModelEvaluation: Llama-Doctor-3.2-3B-Instruct.
What was the peak RAM consumption during the workflow?	Peak RAM usage during the workflow was 187 GB (data loading and model sharding across 8 GPUs).
Has the model been trained in a distributed setting?	Yes, the model was trained in a distributed setting, utilizing 8 GPUs and sharding the model across them.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Each GPU has a TDP of 700W; with 8 GPUs, the total power consumption is 5600W during training.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts are meta-llama/Llama-3.2-3B-Instruct (pretrained model) and avaliev/chat_doctor (medical instruction-tuning dataset).
What is the total energy use for completing the workflow?	Training utilized a cumulative 460,000 GPU hours for the 3B model, with each GPU at 700W, but for the fine-tuning workflow specifically, the energy use is not explicitly stated; only pretraining energy is detailed.
List all input files with size larger than 100Mb	Files larger than 100MB: pytorch_model-00001-of-00002.bin (4.97 GB), pytorch_model-00002-of-00002.bin (1.46 GB), tokenizer.json (17.2 MB).
List all different file types used as input	Input file types include: .bin (model weights), .json (configuration, tokenizer, index), .gitattributes, .md (README).
Identify the largest output	The largest output is the fine-tuned model weights: Llama-Doctor-3.2-3B-Instruct, distributed as BF16 safetensors (two shards: 4.97 GB + 1.46 GB) and GGUF variant.
What is the science domain of the dataset?	The science domain of the dataset is medical/healthcare, specifically patient–doctor conversational QA.
Does the dataset have a predetermined train-test split?	The dataset does not have a predetermined train-test split; it is merged and deduplicated for instruction-tuning.
How many samples are present in the whole dataset?	The dataset contains 110,000 samples (100,000 from HealthCareMagic and 10,000 from iCliniq).
What is the data type of the ground truth (if present)?	The ground truth data type is text, specifically doctor responses in instruction/input/output JSON triples.
What is the specific task for which the dataset was created?	The dataset was created for medical conversational QA and instruction-following tasks.
What is the size in byte of one sample?	Exact size per sample is not specified, but with 110,000 samples and ~14 GB dataset cache, average sample size is approximately 130 KB.
What is the total size of the whole dataset?	The total size of the dataset cache is approximately 14 GB.
What are the designed uses for this model?	Designed uses include chatbots for customer support, medical consultation tools, content creation, and problem-solving assistants in instructional contexts.
How many epochs have been used in the finetuning?	The number of epochs used in fine-tuning is not specified in the workflow card.
How many model parameters (weights) does the model have?	The model has 3.21 billion parameters (weights).
What is the science domain of the model?	The science domain of the model is medical/healthcare, with conversational and instruction-following capabilities.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves text generation and instruction-following tasks, specifically conversational QA (neither regression nor classification).
What is the intended use of this model?	The intended use is for commercial and research applications in multilingual conversational AI, medical QA, content generation, and agentic systems.
What is the size of the final model in Mb?	The final model size is approximately 6.43 GB, which is 6430 MB.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using supervised fine-tuning (SFT) on the medical conversation dataset.
What is the claimed performance of this model?	The model is claimed to outperform many open source and closed chat models on common industry benchmarks, with improved instruction-following and medical response quality.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, performance is improved in the instruction-tuned (fine-tuned) version compared to the pretrained base model, especially in instruction-following and medical QA tasks.