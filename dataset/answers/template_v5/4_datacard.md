How many activities are present in the whole workflow?	There is no explicit workflow or activity list provided in the cards. The cards describe dataset creation, curation, and model training, but do not enumerate activities or steps as discrete workflow items.
What is the final status of the workflow?	The cards do not specify a workflow status. They describe the release of datasets and the completion of model training, implying the workflow is complete, but no explicit status is given.
What is the time to completion of the workflow?	No information about the total time to completion of the workflow is provided in the cards.
List all the parameters of the first activity of the workflow	No explicit activities or their parameters are listed in the cards, so this information is not available.
What hardware was used in the workflow?	The cards do not mention any specific hardware used for dataset creation or model training.
Who is responsible for this workflow (person or username or entity)?	NVIDIA is the entity responsible for the dataset and model development, as indicated in the dataset description and license information.
What was the specific execution order of the tasks?	The cards do not provide a specific execution order of tasks; they only describe data collection, curation, and model training in general terms.
List all parameters for all activites in the workflow	No explicit activities or their parameters are listed in the cards, so this information is not available.
What was the peak RAM consumption during the workflow?	Peak RAM consumption is not reported in the cards.
Has the model been trained in a distributed setting?	The cards do not explicitly state whether distributed training was used, but the global batch size and packed sequence length suggest large-scale training, likely on multiple GPUs, though this is not directly confirmed.
What was the total power consumption in Watts of the GPU(s) during the workflow?	No information about GPU power consumption is provided in the cards.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts include the Nemotron-Cascade-2-RL dataset and the Nemotron-Cascade-2-SFT-Data, which are used for model training and fine-tuning.
What is the total energy use for completing the workflow?	No information about total energy use is provided in the cards.
List all input files with size larger than 100Mb	The cards do not list individual input files or their sizes, but the total dataset size is ~2.73 GB, implying some files may exceed 100Mb.
List all different file types used as input	Input files are in JSONL format, as specified in the dataset description.
Identify the largest output	The largest output is the Nemotron-Cascade-2-30B-A3B model, but its exact size is not specified in the cards.
What is the science domain of the dataset?	The dataset covers multiple domains: math, science (physics, chemistry, biology), general chat, instruction following, safety, conversational agent, software engineering, and terminal agent.
Does the dataset have a predetermined train-test split?	The cards only mention training splits; there is no explicit mention of a train-test split.
How many samples are present in the whole dataset?	The Nemotron-Cascade-2-RL dataset contains 73,809 samples; the SFT dataset contains millions of samples across domains.
What is the data type of the ground truth (if present)?	Ground truth data type is text, as the dataset modality is text and structure is text + metadata.
What is the specific task for which the dataset was created?	The dataset was created for training and evaluating reinforcement learning (RL) and instruction-following models.
What is the size in byte of one sample?	The cards do not specify the size in bytes of one sample.
What is the total size of the whole dataset?	The Nemotron-Cascade-2-RL dataset is approximately 2.73 GB in total disk size.
What are the designed uses for this model?	The model is designed for instruction-following, RL, multi-domain tasks, agentic workflows, software engineering, and conversational agent tasks.
How many epochs have been used in the finetuning?	Approximately 1.5 epochs were used for SFT model training, as stated in the training section.
How many model parameters (weights) does the model have?	The model has 30 billion parameters, as indicated by the model name Nemotron-Cascade-2-30B-A3B.
What is the science domain of the model?	The model covers multiple domains: math, science, general chat, instruction following, safety, conversational agent, software engineering, and terminal agent.
What is the task solved by this model (regression or classification or forecast etc.)?	The model is designed for instruction-following, RL, multi-domain agentic tasks, and conversational tasks; it is not limited to regression or classification.
What is the intended use of this model?	The intended use is to train and evaluate RL and instruction-following models for commercial and research purposes.
What is the size of the final model in Mb?	The cards do not specify the exact size in MB of the final model.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using supervised fine-tuning (SFT) and reinforcement learning (RL), including multi-domain on-policy distillation.
What is the claimed performance of this model?	The cards do not provide specific performance metrics or claims.
Are the performance shown in the pretrained version improved in the finetuning?	The cards do not provide comparative performance data between pretrained and finetuned versions.