How many activities are present in the whole workflow?	1
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	12h 15m 22s
List all the parameters of the first activity of the workflow	epochs: 3, lr: 2e-5, batch_size: 128, optim: adamw_torch
What hardware was used in the workflow?	8x H100-80GB GPUs
Who is responsible for this workflow (person or username or entity)?	AI Research Lab
What was the specific execution order of the tasks?	supervised-fine-tuning
List all the parameters for the whole workflow process	epochs: 3, lr: 2e-5, batch_size: 128, optim: adamw_torch
What was the peak RAM consumption during the workflow?	answer not found
Has the model been trained in a distributed setting?	answer not found
What was the real-time power consumption (in Watts) of the GPU during the workflow?	700
Which inputs influenced the output in the workflow?	pretrained-base-model, training-dataset
What is the total energy use for completing the workflow?	answer not found
List all input files with size larger than 100Mb	answer not found
List all different file types used as input	Pretrained Large Language Model, Medical Conversation Dataset
Identify the largest output	PyTorch model bins (6.43 GB total)
What is the science domain of the dataset?	Medical
Does the dataset have a predetermined train-test split?	Automated evaluation on held-out 5% of chat_doctor dataset.
How many samples are present in the whole dataset?	110k
What is the data type of the ground truth (if present)?	answer not found
What is the specific task for which the dataset was created?	Medical Conversation / Medical QA
What is the size in byte of one sample?	answer not found
What is the total size of the whole dataset?	answer not found
What are the designed uses for this model?	Conversational AI, Text Generation, Instruction Following, Medical Consultation Tools, Content Creation, Problem-solving Assistants
How many epochs have been used in the final training?	3
How many model parameters (weights) does the model have?	3.21B
What is the science domain of the model?	Medical / Multilingual Dialogue
What is the task solved by this model (regression or classification or forecast etc.)?	Text Generation / Instruction Following
What is the intended use of this model?	Conversational AI, Medical Consultation, Content Creation, Instruction Following
What is the size of the final model in Mb?	6430
What technique was used to train the model?	Supervised Fine-Tuning (SFT)
What is the claimed performance of this model?	Final Train Loss: 0.642; Eval Accuracy: 78.4%
Are the performance shown in the pretrained version improved in the finetuning?	answer not found