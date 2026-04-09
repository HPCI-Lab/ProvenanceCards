How many activities are present in the whole workflow?	1
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	9h 45m 00s
List all the parameters of the first activity of the workflow	Rank: 16, Alpha: 32, LR: 2e-4, 4-bit loading
What hardware was used in the workflow?	2x NVIDIA RTX 4090 (24GB)
Who is responsible for this workflow (person or username or entity)?	AI4Privacy
What was the specific execution order of the tasks?	pii-redaction-training
List all the parameters for the whole workflow process	Rank: 16, Alpha: 32, LR: 2e-4, 4-bit loading
What was the peak RAM consumption during the workflow?	
Has the model been trained in a distributed setting?	
What was the real-time power consumption (in Watts) of the GPU during the workflow?	
Which inputs influenced the output in the workflow?	base-model, pii-dataset
What is the total energy use for completing the workflow?	
List all input files with size larger than 100Mb	
List all different file types used as input	Pretrained Large Language Model, Privacy Masking Dataset
Identify the largest output	Llama-3.2-3B PII Redactor (LoRA)
What is the science domain of the dataset?	Privacy / Data Protection
Does the dataset have a predetermined train-test split?	
How many samples are present in the whole dataset?	200k
What is the data type of the ground truth (if present)?	
What is the specific task for which the dataset was created?	PII masking/redaction
What is the size in byte of one sample?	
What is the total size of the whole dataset?	
What are the designed uses for this model?	Replacing PII with placeholders like [FIRSTNAME], [EMAIL]
How many epochs have been used in the final training?	
How many model parameters (weights) does the model have?	
What is the science domain of the model?	Privacy / Data Protection
What is the task solved by this model (regression or classification or forecast etc.)?	PII redaction (sequence labeling / masking)
What is the intended use of this model?	PII redaction in text
What is the size of the final model in Mb?	
What technique was used to train the model?	QLoRA Fine-tuning
What is the claimed performance of this model?	Exact Match: 0.67, Micro-F1: 0.90, Precision: 0.91, Recall: 0.90
Are the performance shown in the pretrained version improved in the finetuning?