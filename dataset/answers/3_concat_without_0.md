How many activities are present in the whole workflow?	2
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	9h 45m 00s
List all the parameters of the first activity of the workflow	Rank: 16, Alpha: 32, LR: 2e-4, 4-bit loading
What hardware was used in the workflow?	2x NVIDIA RTX 4090 (24GB)
Who is responsible for this workflow (person or username or entity)?	AI4Privacy
What was the specific execution order of the tasks?	pii-redaction-training (QLoRA Fine-tuning)
List all the parameters for the whole workflow process	Rank: 16, Alpha: 32, LR: 2e-4, 4-bit loading
What was the peak RAM consumption during the workflow?	answer not found
Has the model been trained in a distributed setting?	answer not found
What was the real-time power consumption (in Watts) of the GPU during the workflow?	answer not found
Which inputs influenced the output in the workflow?	meta-llama/Llama-3.2-3B-Instruct, ai4privacy/pii-masking-200k
What is the total energy use for completing the workflow?	answer not found
List all input files with size larger than 100Mb	answer not found
List all different file types used as input	Pretrained Large Language Model, Privacy Masking Dataset
Identify the largest output	Llama-3.2-3B PII Redactor (LoRA)
What is the science domain of the dataset?	privacy
Does the dataset have a predetermined train-test split?	Yes
How many samples are present in the whole dataset?	~209,000
What is the data type of the ground truth (if present)?	text (masked_text/target_text)
What is the specific task for which the dataset was created?	PII masking/redaction (token classification, text generation)
What is the size in byte of one sample?	answer not found
What is the total size of the whole dataset?	answer not found
What are the designed uses for this model?	assistant-like chat, agentic retrieval, summarization, privacy masking/redaction
How many epochs have been used in the final training?	answer not found
How many model parameters (weights) does the model have?	3.21B
What is the science domain of the model?	Multilingual Large Language Model (NLP)
What is the task solved by this model (regression or classification or forecast etc.)?	classification, text generation
What is the intended use of this model?	commercial and research use in multiple languages, privacy masking, assistant-like chat, summarization
What is the size of the final model in Mb?	2529 (QLoRA 3B)
What technique was used to train the model?	QLoRA Fine-tuning
What is the claimed performance of this model?	Exact Match: 0.67, Micro-F1: 0.90, Precision: 0.91, Recall: 0.90
Are the performance shown in the pretrained version improved in the finetuning?	Yes