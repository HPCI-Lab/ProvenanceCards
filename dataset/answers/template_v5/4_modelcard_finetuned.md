How many activities are present in the whole workflow?	There is no explicit workflow or activity list provided in the cards, so the number of activities in the workflow cannot be determined from the available information.
What is the final status of the workflow?	The final status of the workflow is not specified in the provided cards.
What is the time to completion of the workflow?	The time to completion of the workflow is not mentioned in the provided information.
List all the parameters of the first activity of the workflow	There is no explicit workflow or activity list, so the parameters of the first activity cannot be determined from the available information.
What hardware was used in the workflow?	The model is designed to run on consumer GPUs and mentions VRAM requirements (e.g., 17 GB for 4-bit quantization), but specific hardware models are not listed.
Who is responsible for this workflow (person or username or entity)?	The responsible entity for the openNemo Cascade port is Empero AI, as stated in the card.
What was the specific execution order of the tasks?	The specific execution order of tasks in the workflow is not provided in the cards.
List all parameters for all activites in the workflow	There is no explicit workflow or activity list, so parameters for all activities cannot be determined from the available information.
What was the peak RAM consumption during the workflow?	Peak RAM (VRAM) usage is given for model loading: ~65 GB for bf16, ~17 GB for 4-bit quantization, and ~19 GB for 4-bit + QLoRA (r=64).
Has the model been trained in a distributed setting?	The cards do not specify whether the model was trained in a distributed setting.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Total power consumption in Watts is not provided in the available information.
What significant input artifacts are involved in the generation of the finetuned model?	The significant input artifacts are the datasets: nvidia/Nemotron-Cascade-2-SFT-Data and nvidia/Nemotron-Cascade-2-RL-data.
What is the total energy use for completing the workflow?	Total energy use for completing the workflow is not specified in the cards.
List all input files with size larger than 100Mb	Input file sizes are not provided, so files larger than 100Mb cannot be identified from the available information.
List all different file types used as input	The input file types are not explicitly listed, but likely include text datasets (possibly in JSON, TXT, or similar formats) as per standard practice.
Identify the largest output	The largest output is the final model weights file, which is approximately 30B parameters and requires ~17 GB VRAM in 4-bit quantization.
What is the science domain of the dataset?	The science domain of the dataset is natural language processing (NLP), with a focus on reasoning, mathematics, and code.
Does the dataset have a predetermined train-test split?	The cards do not specify whether the dataset has a predetermined train-test split.
How many samples are present in the whole dataset?	The number of samples in the datasets is not provided in the cards.
What is the data type of the ground truth (if present)?	The data type of the ground truth is not explicitly stated, but likely consists of text responses for supervised fine-tuning and reward signals for RL.
What is the specific task for which the dataset was created?	The datasets were created for supervised fine-tuning and reinforcement learning to improve reasoning and code generation abilities.
What is the size in byte of one sample?	The size in bytes of one sample is not specified in the cards.
What is the total size of the whole dataset?	The total size of the datasets is not provided in the available information.
What are the designed uses for this model?	The model is designed for advanced reasoning, mathematics, code generation, and general text generation tasks.
How many epochs have been used in the finetuning?	The number of epochs used in fine-tuning is not specified in the cards.
How many model parameters (weights) does the model have?	The model has 30.87 billion total parameters, with approximately 3 billion active per token.
What is the science domain of the model?	The science domain of the model is natural language processing (NLP), with emphasis on reasoning, mathematics, and code.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves generative tasks, specifically text generation, reasoning, and code generation.
What is the intended use of this model?	The intended use is for advanced reasoning, mathematics, code generation, and general text generation.
What is the size of the final model in Mb?	The final model size is not given in megabytes, but in 4-bit quantization it requires approximately 17 GB of VRAM, which is about 17,000 MB.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model supports QLoRA fine-tuning and is compatible with LoRA/QLoRA techniques.
What is the claimed performance of this model?	The model achieves gold medal performance on IMO 2025 (35 pts), IOI 2025 (439.3), and high scores on other benchmarks such as AIME, HMMT, LiveCodeBench, and MMLU-Pro.
Are the performance shown in the pretrained version improved in the finetuning?	The cards do not provide a direct comparison between pretrained and finetuned performance, so this cannot be determined from the available information.