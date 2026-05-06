How many activities are present in the whole workflow?	run-pii-redactor-qlora-20241027 contains 1 activity block (qlora-finetuning)
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	9h 45m 00s
List all the parameters of the first activity of the workflow	Rank: 16, Alpha: 32, LR: 2e-4, 4-bit loading
What hardware was used in the workflow?	2x NVIDIA RTX 4090 (24GB)
Who is responsible for this workflow (person or username or entity)?	AI4Privacy
What was the specific execution order of the tasks?	qlora-finetuning (pii-redaction-training) was performed after inputs (base-model, pii-dataset) were provided, producing lora-adapter-weights
List all the parameters for the whole workflow process	Rank: 16, Alpha: 32, LR: 2e-4, 4-bit loading
What was the peak RAM consumption during the workflow?	answer not found
Has the model been trained in a distributed setting?	answer not found
What was the real-time power consumption (in Watts) of the GPU during the workflow?	answer not found
Which inputs influenced the output in the workflow?	meta-llama/Llama-3.2-3B-Instruct, ai4privacy/pii-masking-200k
What is the total energy use for completing the workflow?	answer not found
List all input files with size larger than 100Mb	answer not found
List all different file types used as input	Pretrained Large Language Model, Privacy Masking Dataset
Identify the largest output	Llama-3.2-3B PII Redactor (LoRA) adapter weights
What is the science domain of the dataset?	Privacy, Data Protection, Natural Language Processing
Does the dataset have a predetermined train-test split?	answer not found
How many samples are present in the whole dataset?	200k samples (English subset used)
What is the data type of the ground truth (if present)?	answer not found
What is the specific task for which the dataset was created?	Privacy Masking / PII Redaction
What is the size in byte of one sample?	answer not found
What is the total size of the whole dataset?	answer not found
What are the designed uses for this model?	Redacting PII in English text to placeholder labels for downstream processing or audit; keep the non-PII text unchanged as much as possible
How many epochs have been used in the final training?	answer not found
How many model parameters (weights) does the model have?	3.21B
What is the science domain of the model?	Natural Language Processing, Privacy
What is the task solved by this model (regression or classification or forecast etc.)?	PII Redaction (span classification and replacement)
What is the intended use of this model?	Redacting PII in English text to placeholder labels for downstream processing or audit; keep the non-PII text unchanged as much as possible
What is the size of the final model in Mb?	answer not found
What technique was used to train the model?	QLoRA Fine-tuning
What is the claimed performance of this model?	Exact Match: 0.67, Micro-F1: 0.90, Precision: 0.91, Recall: 0.90
Are the performance shown in the pretrained version improved in the finetuning?	answer not found