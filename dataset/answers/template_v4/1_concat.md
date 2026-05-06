How many activities are present in the whole workflow?	2
What is the final status of the workflow?	Success
What is the time to completion of the workflow?	12h 15m 22s
List all the parameters of the first activity of the workflow	epochs: 3, lr: 2e-5, batch_size: 128, optim: adamw_torch
What hardware was used in the workflow?	8x H100-80GB GPUs
Who is responsible for this workflow (person or username or entity)?	AI Research Lab
What was the specific execution order of the tasks?	pretrained-base-model, training-dataset → supervised-fine-tuning → finetuned-model-weights
List all the parameters for the whole workflow process	epochs: 3, lr: 2e-5, batch_size: 128, optim: adamw_torch
What was the peak RAM consumption during the workflow?	Not specified
Has the model been trained in a distributed setting?	Not explicitly stated
What was the real-time power consumption (in Watts) of the GPU during the workflow?	700
Which inputs influenced the output in the workflow?	pretrained-base-model, training-dataset
What is the total energy use for completing the workflow?	Not specified for this run
List all input files with size larger than 100Mb	tokenizer.json (17.2 MB) [No input file >100MB listed]
List all different file types used as input	Pretrained Large Language Model, Medical Conversation Dataset
Identify the largest output	pytorch_model-00001-of-00002.bin (4.97 GB)
What is the science domain of the dataset?	Medical
Does the dataset have a predetermined train-test split?	Held-out 5% for validation
How many samples are present in the whole dataset?	110,000
What is the data type of the ground truth (if present)?	Text (medical conversation output)
What is the specific task for which the dataset was created?	Medical question-answering
What is the size in byte of one sample?	Not specified
What is the total size of the whole dataset?	Not specified
What are the designed uses for this model?	Conversational AI, Text Generation, Instruction Following, Medical Consultation Tools, Content Creation, Problem-solving Assistants
How many epochs have been used in the final training?	3
How many model parameters (weights) does the model have?	3.21B
What is the science domain of the model?	Medical
What is the task solved by this model (regression or classification or forecast etc.)?	Question-answering
What is the intended use of this model?	Medical question-answering, conversational AI, instruction following
What is the size of the final model in Mb?	6,430
What technique was used to train the model?	Supervised Fine-Tuning (SFT)
What is the claimed performance of this model?	Final Train Loss: 0.642; Eval Accuracy: 78.4%
Are the performance shown in the pretrained version improved in the finetuning?	Yes