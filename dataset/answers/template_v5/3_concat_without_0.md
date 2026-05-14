How many activities are present in the whole workflow?	How many activities are present in the whole workflow?	3
What is the final status of the workflow?	What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	What is the time to completion of the workflow?	12h 33m 33s
List all the parameters of the first activity of the workflow	List all the parameters of the first activity of the workflow	ai4privacy/pii-masking-200k (full): ~209k multilingual examples (English, French, German, Italian) with 54 PII classes across 229 discussion subjects; format: JSONL with source_text, target_text, privacy_mask, span_labels, mbert_bio_labels, mbert_text_tokens fields
What hardware was used in the workflow?	What hardware was used in the workflow?	1× NVIDIA A10G-24GB GPU, AMD EPYC 7R32 CPU, 64 GB RAM, Ubuntu 22.04.4 LTS
Who is responsible for this workflow (person or username or entity)?	Who is responsible for this workflow (person or username or entity)?	ml-privacy-team
What was the specific execution order of the tasks?	What was the specific execution order of the tasks?	DataPreparation → ModelFinetuning → ModelEvaluation
List all parameters for all activites in the workflow	List all parameters for all activites in the workflow	LoRA rank: 16, LoRA alpha: 32, LoRA dropout: 0.05, quantisation: 4-bit NF4 (bitsandbytes), sequence length: 320–512, batch size: 1, gradient accumulation steps: 16, learning rate: 2e-4, scheduler: cosine, warmup: 3%, loss mask: assistant span only (between <safe> and </safe>), ai4privacy/pii-masking-200k (full), meta-llama/Llama-3.2-3B-Instruct, English subset filtering, train/test split, evaluation split of 300 samples
What was the peak RAM consumption during the workflow?	What was the peak RAM consumption during the workflow?	31 GB
Has the model been trained in a distributed setting?	Has the model been trained in a distributed setting?	No, single GPU (1× NVIDIA A10G-24GB)
What was the total power consumption in Watts of the GPU(s) during the workflow?	What was the total power consumption in Watts of the GPU(s) during the workflow?	Not specified in the cards
What significant input artifacts are involved in the generation of the finetuned model?	What significant input artifacts are involved in the generation of the finetuned model?	meta-llama/Llama-3.2-3B-Instruct (6.43 GB), ai4privacy/pii-masking-200k (English subset, ~11 GB)
What is the total energy use for completing the workflow?	What is the total energy use for completing the workflow?	Not specified in the cards
List all input files with size larger than 100Mb	List all input files with size larger than 100Mb	meta-llama/Llama-3.2-3B-Instruct (6.43 GB), ai4privacy/pii-masking-200k (English subset, ~11 GB)
List all different file types used as input	List all different file types used as input	safetensors (model weights), JSONL (dataset)
Identify the largest output	Identify the largest output	Llama-3.2-3B-PII-Redactor (LoRA adapter) (~180 MB)
What is the science domain of the dataset?	What is the science domain of the dataset?	Privacy, Data Anonymization, AI, NLP
Does the dataset have a predetermined train-test split?	Does the dataset have a predetermined train-test split?	Yes, with 300 random samples held out for evaluation
How many samples are present in the whole dataset?	How many samples are present in the whole dataset?	~209,000
What is the data type of the ground truth (if present)?	What is the data type of the ground truth (if present)?	Text (PII-masked target_text), privacy_mask (structured JSON)
What is the specific task for which the dataset was created?	What is the specific task for which the dataset was created?	PII redaction (classification and token replacement in text)
What is the size in byte of one sample?	What is the size in byte of one sample?	Not specified; estimated average ~65 KB per sample (based on total dataset size and sample count)
What is the total size of the whole dataset?	What is the total size of the whole dataset?	~13.6 million text tokens, ~11 GB (English subset)
What are the designed uses for this model?	What are the designed uses for this model?	Redacting PII in English text to placeholder labels for downstream processing or audit; keeping non-PII text unchanged
How many epochs have been used in the finetuning?	How many epochs have been used in the finetuning?	Not specified in the cards
How many model parameters (weights) does the model have?	How many model parameters (weights) does the model have?	3.21 billion (base model)
What is the science domain of the model?	What is the science domain of the model?	Privacy, Data Anonymization, NLP, AI
What is the task solved by this model (regression or classification or forecast etc.)?	What is the task solved by this model (regression or classification or forecast etc.)?	Token classification and text generation (PII redaction)
What is the intended use of this model?	What is the intended use of this model?	Redacting PII in English text to placeholder labels for privacy and downstream processing
What is the size of the final model in Mb?	What is the size of the final model in Mb?	LoRA adapter: ~180 MB; base model: 6,430 MB (6.43 GB)
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	QLoRA (4-bit quantisation, LoRA rank 16)
What is the claimed performance of this model?	What is the claimed performance of this model?	Exact match: ~0.67; Placeholder micro-F1: ~0.90 (Precision ~0.91, Recall ~0.90); Formatting errors: ~0.00
Are the performance shown in the pretrained version improved in the finetuning?	Are the performance shown in the pretrained version improved in the finetuning?	Yes, the finetuned model achieves high placeholder micro-F1 and exact match for PII redaction, which is not present in the pretrained base model