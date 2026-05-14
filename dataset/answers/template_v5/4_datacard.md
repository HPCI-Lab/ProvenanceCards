How many activities are present in the whole workflow?	There is no explicit mention of the number of activities in the workflow in the provided cards.
What is the final status of the workflow?	The final status of the workflow is not specified in the provided cards.
What is the time to completion of the workflow?	The time to completion of the workflow is not specified in the provided cards.
List all the parameters of the first activity of the workflow	The parameters of the first activity of the workflow are not specified in the provided cards.
What hardware was used in the workflow?	The hardware used in the workflow is not specified in the provided cards.
Who is responsible for this workflow (person or username or entity)?	The workflow is associated with NVIDIA, as indicated by dataset and license information.
What was the specific execution order of the tasks?	The specific execution order of the tasks is not specified in the provided cards.
List all parameters for all activites in the workflow	The parameters for all activities in the workflow are not specified in the provided cards.
What was the peak RAM consumption during the workflow?	The peak RAM consumption during the workflow is not specified in the provided cards.
Has the model been trained in a distributed setting?	The cards do not specify whether the model was trained in a distributed setting.
What was the total power consumption in Watts of the GPU(s) during the workflow?	The total power consumption in Watts of the GPU(s) during the workflow is not specified in the provided cards.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts include the Nemotron-Cascade-2-SFT-Data and Nemotron-Cascade-2-RL dataset, which are composed of multiple domain-specific datasets in JSONL format.
What is the total energy use for completing the workflow?	The total energy use for completing the workflow is not specified in the provided cards.
List all input files with size larger than 100Mb	The cards do not list individual input files or their sizes, but the total dataset size is ~2.73 GB, implying some files may exceed 100Mb.
List all different file types used as input	Input files are in JSONL format (text modality).
Identify the largest output	The largest output is the Nemotron-Cascade-2-30B-A3B model, but its exact size is not specified.
What is the science domain of the dataset?	The dataset covers multiple domains: math, science (physics, chemistry, biology), general chat, instruction following, safety, conversational agent, software engineering, and terminal agent.
Does the dataset have a predetermined train-test split?	The dataset is described as containing only training samples; no explicit train-test split is mentioned.
How many samples are present in the whole dataset?	The Nemotron-Cascade-2-RL dataset contains 73,809 samples; the SFT dataset contains millions of samples (e.g., Math: 5,226,364; General Chat: 13,972,873).
What is the data type of the ground truth (if present)?	The ground truth, if present, is in text format.
What is the specific task for which the dataset was created?	The dataset was created for training and evaluating RL and instruction-following models, including multi-domain tasks and software engineering workflows.
What is the size in byte of one sample?	The size in byte of one sample is not specified in the provided cards.
What is the total size of the whole dataset?	The Nemotron-Cascade-2-RL dataset is ~2.73 GB; the SFT dataset size is not specified.
What are the designed uses for this model?	The model is designed for instruction-following, reinforcement learning, multi-domain tasks, agentic workflows, and software engineering applications.
How many epochs have been used in the finetuning?	Approximately 1.5 epochs were used for SFT training.
How many model parameters (weights) does the model have?	The Nemotron-Cascade-2-30B-A3B model has 30 billion parameters.
What is the science domain of the model?	The model covers multiple domains: math, science, general chat, instruction following, safety, conversational agent, software engineering, and terminal agent.
What is the task solved by this model (regression or classification or forecast etc.)?	The model is designed for instruction-following, RL, multi-domain question answering, agentic workflows, and code-related tasks; it is not limited to regression or classification.
What is the intended use of this model?	The intended use is to train and evaluate RL and instruction-following models for commercial and research purposes.
What is the size of the final model in Mb?	The size of the final model in Mb is not specified in the provided cards.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using supervised fine-tuning (SFT) and reinforcement learning (RL), including multi-domain on-policy distillation.
What is the claimed performance of this model?	The cards do not specify quantitative performance claims for the model.
Are the performance shown in the pretrained version improved in the finetuning?	The cards do not provide a direct comparison of performance between pretrained and finetuned versions.