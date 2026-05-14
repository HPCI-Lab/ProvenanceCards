How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	12h 33m 33s
List all the parameters of the first activity of the workflow	ai4privacy/pii-masking-200k (full): ~209k multilingual examples (English, French, German, Italian) with 54 PII classes across 229 discussion subjects; format: JSONL with source_text, target_text, privacy_mask, span_labels, mbert_bio_labels, mbert_text_tokens fields
What hardware was used in the workflow?	1× NVIDIA A10G-24GB GPU, AMD EPYC 7R32 CPU, 64 GB RAM, host OS Ubuntu 22.04.4 LTS
Who is responsible for this workflow (person or username or entity)?	ml-privacy-team
What was the specific execution order of the tasks?	DataPreparation → ModelFinetuning → ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: ai4privacy/pii-masking-200k (full); ModelFinetuning: meta-llama/Llama-3.2-3B-Instruct, ai4privacy/pii-masking-200k (English subset), LoRA rank: 16, LoRA alpha: 32, LoRA dropout: 0.05, quantisation: 4-bit NF4, sequence length: 320–512, batch size: 1, gradient accumulation steps: 16, learning rate: 2e-4, scheduler: cosine, warmup: 3%, loss mask: assistant span only; ModelEvaluation: Llama-3.2-3B-PII-Redactor (LoRA adapter), evaluation split (300 held-out samples)
What was the peak RAM consumption during the workflow?	31 GB
Has the model been trained in a distributed setting?	No evidence of distributed training; only one GPU (NVIDIA A10G-24GB) was used.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Not specified in the cards.
What significant input artifacts are involved in the generation of the finetuned model?	meta-llama/Llama-3.2-3B-Instruct and ai4privacy/pii-masking-200k (English subset)
What is the total energy use for completing the workflow?	Not specified in the cards.
List all input files with size larger than 100Mb	meta-llama/Llama-3.2-3B-Instruct (~6.43 GB), ai4privacy/pii-masking-200k (~11 GB English dataset cache)
List all different file types used as input	JSONL (dataset), safetensors (model weights), PyTorch BF16 (model weights)
Identify the largest output	Llama-3.2-3B-PII-Redactor (LoRA adapter): ~180 MB
What is the science domain of the dataset?	Privacy, Data Protection, Natural Language Processing
Does the dataset have a predetermined train-test split?	Yes; train/test split with 300 random samples held out for evaluation
How many samples are present in the whole dataset?	~209,000 examples
What is the data type of the ground truth (if present)?	Text with PII replaced by bracketed placeholders (target_text)
What is the specific task for which the dataset was created?	PII redaction: detecting and replacing personally identifiable information spans in text with structured placeholders
What is the size in byte of one sample?	Not specified; dataset size is ~11 GB for English subset, ~209k examples, so average sample size is ~55 KB
What is the total size of the whole dataset?	~11 GB (English subset cache); full dataset size not explicitly stated but likely larger
What are the designed uses for this model?	Detecting and replacing PII spans in English text with structured placeholders, preserving non-PII content
How many epochs have been used in the finetuning?	Not specified in the cards.
How many model parameters (weights) does the model have?	3.21 billion parameters
What is the science domain of the model?	Natural Language Processing, Privacy
What is the task solved by this model (regression or classification or forecast etc.)?	Classification (PII span detection and replacement)
What is the intended use of this model?	PII redaction in English text, replacing detected PII with structured placeholders
What is the size of the final model in Mb?	LoRA adapter: ~180 MB; base model: ~6.43 GB
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	QLoRA (4-bit quantisation, LoRA rank 16)
What is the claimed performance of this model?	Placeholder micro-F1: ~0.90 (precision ~0.91, recall ~0.90); exact match: ~0.67; formatting errors: ~0.00
Are the performance shown in the pretrained version improved in the finetuning?	Not specified; only finetuned model performance is reported.