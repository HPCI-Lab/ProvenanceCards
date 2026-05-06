How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	~
List all the parameters of the first activity of the workflow	ai4privacy/pii-masking-200k (full): ~209k multilingual examples (English, French, German, Italian) with 54 PII classes across 229 discussion subjects; format: JSONL with source_text, target_text, privacy_mask, span_labels, mbert_bio_labels, mbert_text_tokens fields
What hardware was used in the workflow?	~
Who is responsible for this workflow (person or username or entity)?	~
What was the specific execution order of the tasks?	DataPreparation → ModelFinetuning → ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: ai4privacy/pii-masking-200k (full); ModelFinetuning: meta-llama/Llama-3.2-3B-Instruct, ai4privacy/pii-masking-200k (English subset); ModelEvaluation: Llama-3.2-3B-PII-Redactor (LoRA adapter), evaluation split
What was the peak RAM consumption during the workflow?	~
Has the model been trained in a distributed setting?	~
What was the total power consumption in Watts of the GPU(s) during the workflow?	~
What significant input artifacts are involved in the generation of the finetuned model?	meta-llama/Llama-3.2-3B-Instruct; ai4privacy/pii-masking-200k
What is the total energy use for completing the workflow?	~
List all input files with size larger than 100Mb	ai4privacy/pii-masking-200k (~13.6M text tokens); meta-llama/Llama-3.2-3B-Instruct (~6.43 GB)
List all different file types used as input	JSONL, safetensors (PyTorch BF16)
Identify the largest output	Llama-3.2-3B-PII-Redactor (LoRA adapter)
What is the science domain of the dataset?	Privacy, Natural Language Processing
Does the dataset have a predetermined train-test split?	Yes; train/test split with 300 random samples held out for evaluation
How many samples are present in the whole dataset?	~209,000
What is the data type of the ground truth (if present)?	Text (target_text with PII replaced by placeholders)
What is the specific task for which the dataset was created?	PII redaction: detecting and replacing personally identifiable information spans in text with structured placeholders
What is the size in byte of one sample?	~
What is the total size of the whole dataset?	~13.6M text tokens
What are the designed uses for this model?	Detecting and replacing PII spans in English text with structured placeholders, preserving non-PII content
How many epochs have been used in the finetuning?	~
How many model parameters (weights) does the model have?	3.21B parameters
What is the science domain of the model?	Natural Language Processing, Privacy
What is the task solved by this model (regression or classification or forecast etc.)?	PII redaction (sequence-to-sequence text transformation)
What is the intended use of this model?	PII redaction in English text, replacing detected PII with placeholders
What is the size of the final model in Mb?	~
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	QLoRA (4-bit quantisation, LoRA rank 16)
What is the claimed performance of this model?	Placeholder micro-F1: ~0.90 (precision ~0.91, recall ~0.90); exact match: ~0.67; formatting errors: ~0.00
Are the performance shown in the pretrained version improved in the finetuning?	~