How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	~
List all the parameters of the first activity of the workflow	ai4privacy/pii-masking-200k (full): ~209k multilingual examples (English, French, German, Italian) with 54 PII classes across 229 discussion subjects; format: JSONL with source_text, target_text, privacy_mask, span_labels, mbert_bio_labels, mbert_text_tokens fields
What hardware was used in the workflow?	~
Who is responsible for this workflow (person or username or entity)?	~
What was the specific execution order of the tasks?	DataPreparation → ModelFinetuning → ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: ai4privacy/pii-masking-200k (full); ModelFinetuning: meta-llama/Llama-3.2-3B-Instruct, ai4privacy/pii-masking-200k (English subset), LoRA rank: 16, LoRA alpha: 32, LoRA dropout: 0.05, quantisation: 4-bit NF4, sequence length: 320–512, batch size: 1, gradient accumulation steps: 16, learning rate: 2e-4, scheduler: cosine, warmup: 3%, loss mask: assistant span only; ModelEvaluation: Llama-3.2-3B-PII-Redactor (LoRA adapter), evaluation split
What was the peak RAM consumption during the workflow?	~
Has the model been trained in a distributed setting?	~
What was the total power consumption in Watts of the GPU(s) during the workflow?	~
What significant input artifacts are involved in the generation of the finetuned model?	meta-llama/Llama-3.2-3B-Instruct, ai4privacy/pii-masking-200k
What is the total energy use for completing the workflow?	~
List all input files with size larger than 100Mb	meta-llama/Llama-3.2-3B-Instruct (6.43 GB), ai4privacy/pii-masking-200k (~209k examples, 13.6M text tokens)
List all different file types used as input	safetensors, jsonl
Identify the largest output	Llama-3.2-3B-PII-Redactor (LoRA adapter)
What is the science domain of the dataset?	privacy, legal, business, psychology
Does the dataset have a predetermined train-test split?	Yes, train/test split with 300 random samples held out for evaluation
How many samples are present in the whole dataset?	~209,000
What is the data type of the ground truth (if present)?	text (target_text with PII replaced by placeholders)
What is the specific task for which the dataset was created?	PII redaction (classification and text generation)
What is the size in byte of one sample?	~
What is the total size of the whole dataset?	~
What are the designed uses for this model?	Redacting PII in English text to placeholder labels for downstream processing or audit; keep the non-PII text unchanged as much as possible
How many epochs have been used in the finetuning?	~
How many model parameters (weights) does the model have?	3.21 billion (base model)
What is the science domain of the model?	privacy, legal, business, psychology
What is the task solved by this model (regression or classification or forecast etc.)?	classification (PII detection and replacement), text generation
What is the intended use of this model?	Redacting PII in English text to placeholder labels for downstream processing or audit
What is the size of the final model in Mb?	LoRA adapter: ~
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	QLoRA (4-bit quantisation, LoRA rank 16)
What is the claimed performance of this model?	Exact match: ~0.67; Placeholder micro-F1: ~0.90 (precision ~0.91, recall ~0.90); formatting errors: ~0.00
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the finetuned model is specialised for PII redaction and achieves high placeholder micro-F1 and exact match on the evaluation set