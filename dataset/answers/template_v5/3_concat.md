How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	12h 33m 33s
List all the parameters of the first activity of the workflow	ai4privacy/pii-masking-200k (full): ~209k multilingual examples (English, French, German, Italian) with 54 PII classes across 229 discussion subjects; format: JSONL with source_text, target_text, privacy_mask, span_labels, mbert_bio_labels, mbert_text_tokens fields
What hardware was used in the workflow?	1× NVIDIA A10G-24GB, AMD EPYC 7R32, 64 GB RAM
Who is responsible for this workflow (person or username or entity)?	ml-privacy-team
What was the specific execution order of the tasks?	DataPreparation → ModelFinetuning → ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: ai4privacy/pii-masking-200k (full); ModelFinetuning: meta-llama/Llama-3.2-3B-Instruct, ai4privacy/pii-masking-200k (English subset); ModelEvaluation: Llama-3.2-3B-PII-Redactor (LoRA adapter), evaluation split (300 samples)
What was the peak RAM consumption during the workflow?	31 GB
Has the model been trained in a distributed setting?	No, single GPU (1× NVIDIA A10G-24GB)
What was the total power consumption in Watts of the GPU(s) during the workflow?	700 W (peak, as per hardware spec)
What significant input artifacts are involved in the generation of the finetuned model?	meta-llama/Llama-3.2-3B-Instruct, ai4privacy/pii-masking-200k (English subset)
What is the total energy use for completing the workflow?	Not explicitly stated for this run; for Llama 3.2 3B, training power consumption is 700 W, but this workflow is a fine-tuning run, not full pretraining.
List all input files with size larger than 100Mb	meta-llama/Llama-3.2-3B-Instruct (~6.43 GB), ai4privacy/pii-masking-200k (~11 GB English dataset cache)
List all different file types used as input	JSONL (dataset), safetensors (model weights)
Identify the largest output	Llama-3.2-3B-PII-Redactor (LoRA adapter): ~180 MB
What is the science domain of the dataset?	Privacy, Data Anonymization, NLP
Does the dataset have a predetermined train-test split?	Yes (train/test split with 300 random samples held out for evaluation)
How many samples are present in the whole dataset?	~209,000
What is the data type of the ground truth (if present)?	Text (target_text with PII replaced by placeholders)
What is the specific task for which the dataset was created?	PII redaction (token classification and text generation for privacy masking)
What is the size in byte of one sample?	Not explicitly stated; estimated average ~65 KB per sample (based on 13.6M tokens / 209k samples)
What is the total size of the whole dataset?	~11 GB (English subset cache)
What are the designed uses for this model?	Redacting PII in English text to placeholder labels for downstream processing or audit; keeping non-PII text unchanged
How many epochs have been used in the finetuning?	Not explicitly stated
How many model parameters (weights) does the model have?	3.21B (base model); LoRA adapter adds a small number of trainable parameters (rank 16)
What is the science domain of the model?	Privacy, NLP, Data Anonymization
What is the task solved by this model (regression or classification or forecast etc.)?	Token classification and text generation (PII redaction)
What is the intended use of this model?	PII redaction in English text, replacing detected PII spans with placeholders while preserving all non-PII text
What is the size of the final model in Mb?	LoRA adapter: ~180 MB; base model: ~6.43 GB
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	QLoRA (4-bit quantisation, LoRA rank 16)
What is the claimed performance of this model?	Exact match: ~0.67; Placeholder micro-F1: ~0.90 (Precision ~0.91, Recall ~0.90); Formatting errors: ~0.00
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the LoRA adapter specializes the base model for PII redaction, achieving high placeholder micro-F1 and exact match on the task