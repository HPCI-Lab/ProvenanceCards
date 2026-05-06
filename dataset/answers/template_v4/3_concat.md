How many activities are present in the whole workflow?	2
What is the final status of the workflow?	Success
What is the time to completion of the workflow?	9h 45m 00s
List all the parameters of the first activity of the workflow	Rank: 16, Alpha: 32, LR: 2e-4, 4-bit loading
What hardware was used in the workflow?	2x NVIDIA RTX 4090 (24GB)
Who is responsible for this workflow (person or username or entity)?	AI4Privacy
What was the specific execution order of the tasks?	base-model, pii-dataset → qlora-finetuning → lora-adapter-weights
List all the parameters for the whole workflow process	Rank: 16, Alpha: 32, LR: 2e-4, 4-bit loading
What was the peak RAM consumption during the workflow?	Not specified
Has the model been trained in a distributed setting?	No explicit mention
What was the real-time power consumption (in Watts) of the GPU during the workflow?	700
Which inputs influenced the output in the workflow?	meta-llama/Llama-3.2-3B-Instruct, ai4privacy/pii-masking-200k
What is the total energy use for completing the workflow?	Not specified
List all input files with size larger than 100Mb	Not specified
List all different file types used as input	jsonl
Identify the largest output	Llama-3.2-3B PII Redactor (LoRA) adapter weights
What is the science domain of the dataset?	privacy, data anonymization
Does the dataset have a predetermined train-test split?	Yes
How many samples are present in the whole dataset?	~209,000
What is the data type of the ground truth (if present)?	string (masked_text), array (privacy_mask)
What is the specific task for which the dataset was created?	PII masking/redaction
What is the size in byte of one sample?	Not specified
What is the total size of the whole dataset?	Not specified
What are the designed uses for this model?	Redacting PII in English text to placeholder labels for downstream processing or audit
How many epochs have been used in the final training?	Not specified
How many model parameters (weights) does the model have?	3.21B
What is the science domain of the model?	privacy, data anonymization
What is the task solved by this model (regression or classification or forecast etc.)?	classification (token classification), text generation
What is the intended use of this model?	PII redaction in text
What is the size of the final model in Mb?	2529
What technique was used to train the model?	QLoRA fine-tuning
What is the claimed performance of this model?	Exact Match: 0.67, Micro-F1: 0.90, Precision: 0.91, Recall: 0.90
Are the performance shown in the pretrained version improved in the finetuning?	Yes