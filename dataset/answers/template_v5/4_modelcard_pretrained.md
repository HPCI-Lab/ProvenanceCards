How many activities are present in the whole workflow?	No information is provided in the card about the number of activities in the workflow.
What is the final status of the workflow?	The card does not specify the final status of the workflow.
What is the time to completion of the workflow?	The time to completion of the workflow is not mentioned in the card.
List all the parameters of the first activity of the workflow	There is no information about the parameters of the first activity of the workflow in the card.
What hardware was used in the workflow?	The card does not specify the hardware used in the workflow.
Who is responsible for this workflow (person or username or entity)?	The responsible entity is NVIDIA, as indicated by the model and dataset authorship.
What was the specific execution order of the tasks?	The specific execution order of the tasks is not described in the card.
List all parameters for all activites in the workflow	No parameters for activities in the workflow are provided in the card.
What was the peak RAM consumption during the workflow?	Peak RAM consumption during the workflow is not mentioned in the card.
Has the model been trained in a distributed setting?	The card does not explicitly state if distributed training was used.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Total power consumption in Watts of the GPU(s) is not provided in the card.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts include the SFT dataset (nvidia/Nemotron-Cascade-2-SFT-Data) and RL dataset (nvidia/Nemotron-Cascade-2-RL-data).
What is the total energy use for completing the workflow?	Total energy use for completing the workflow is not specified in the card.
List all input files with size larger than 100Mb	The card does not list input files or their sizes.
List all different file types used as input	The card does not specify the file types used as input.
Identify the largest output	The largest output is the Nemotron-Cascade-2-30B-A3B model itself.
What is the science domain of the dataset?	The dataset is in the general-purpose language, reasoning, mathematics, and code reasoning domains.
Does the dataset have a predetermined train-test split?	The card does not mention if the dataset has a predetermined train-test split.
How many samples are present in the whole dataset?	The number of samples in the dataset is not specified in the card.
What is the data type of the ground truth (if present)?	The data type of the ground truth is not specified in the card.
What is the specific task for which the dataset was created?	The dataset was created for supervised fine-tuning (SFT) and reinforcement learning (RL) for language modeling, reasoning, and code reasoning tasks.
What is the size in byte of one sample?	The size in bytes of one sample is not provided in the card.
What is the total size of the whole dataset?	The total size of the dataset is not specified in the card.
What are the designed uses for this model?	The model is designed for strong reasoning, agentic capabilities, mathematics, code reasoning, general-purpose language tasks, and agentic coding/SWE tasks.
How many epochs have been used in the finetuning?	The number of epochs used in finetuning is not mentioned in the card.
How many model parameters (weights) does the model have?	The model is a 30B (30 billion) parameter MoE model with 3B activated parameters per inference.
What is the science domain of the model?	The model is in the general-purpose language, reasoning, mathematics, and code reasoning domains.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves text generation, reasoning, code generation, and instruction following tasks (not strictly regression/classification/forecast).
What is the intended use of this model?	The intended use is for general-purpose language modeling, reasoning, mathematics, code reasoning, and agentic tasks.
What is the size of the final model in Mb?	The size of the final model in MB is not specified in the card.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was post-trained using supervised fine-tuning (SFT) and reinforcement learning (RL), including Cascade RL and multi-domain on-policy distillation.
What is the claimed performance of this model?	The model achieves gold medal performance in the 2025 International Mathematical Olympiad (IMO) and International Olympiad in Informatics (IOI), and strong results on various math, code, and alignment benchmarks.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the finetuned Nemotron-Cascade-2-30B-A3B outperforms the base Nemotron-3-Nano-30B-A3B in multiple benchmarks, as shown in the results table.