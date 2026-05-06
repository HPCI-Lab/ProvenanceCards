How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	~
List all the parameters of the first activity of the workflow	ai4privacy/pii-masking-200k (full): ~209k multilingual examples (English, French, German, Italian) with 54 PII classes across 229 discussion subjects; format: JSONL with source_text, target_text, privacy_mask, span_labels, mbert_bio_labels, mbert_text_tokens fields
What hardware was used in the workflow?	~
Who is responsible for this workflow (person or username or entity)?	~
What was the specific execution order of the tasks?	DataPreparation → ModelFinetuning → ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: ai4privacy/pii-masking-200k (full); ModelFinetuning: meta-llama/Llama-3.2-3B-Instruct, ai4privacy/pii-masking-200k (English subset), LoRA rank: 16, LoRA alpha: 32, LoRA dropout: 0.05, quantisation: 4-bit NF4, sequence length: 320–512, batch size: 1, gradient accumulation steps: 16, learning rate: 2e-4, scheduler: cosine, warmup: 3%, loss mask: assistant span only; ModelEvaluation: Llama-3.2-3B-PII-Redactor (LoRA adapter), evaluation split (300 held-out samples)
What was the peak RAM consumption during the workflow?	~
Has the model been trained in a distributed setting?	Not specified in the workflow card; likely single-node for fine-tuning, distributed for pretraining (Meta's infrastructure), but not explicitly stated for this workflow.
What was the total power consumption in Watts of the GPU(s) during the workflow?	~
What significant input artifacts are involved in the generation of the finetuned model?	meta-llama/Llama-3.2-3B-Instruct (pretrained model weights, ~6.43 GB), ai4privacy/pii-masking-200k (dataset, ~209k examples, 13.6M text tokens)
What is the total energy use for completing the workflow?	~
List all input files with size larger than 100Mb	meta-llama/Llama-3.2-3B-Instruct (~6.43 GB), ai4privacy/pii-masking-200k (~209k examples, 13.6M text tokens)
List all different file types used as input	JSONL (dataset), safetensors (model weights)
Identify the largest output	Llama-3.2-3B-PII-Redactor (LoRA adapter)
What is the science domain of the dataset?	Privacy, legal, business, psychology
Does the dataset have a predetermined train-test split?	Yes; train/test split with 300 random samples held out for evaluation
How many samples are present in the whole dataset?	~209,000
What is the data type of the ground truth (if present)?	Text (target_text with PII replaced by placeholders)
What is the specific task for which the dataset was created?	PII redaction (token classification and text generation)
What is the size in byte of one sample?	Not specified; estimated to be a few hundred bytes per sample (text + metadata)
What is the total size of the whole dataset?	13.6M text tokens; file size not explicitly stated, but likely >100MB
What are the designed uses for this model?	PII redaction in English text; detection and replacement of PII spans with structured placeholders for privacy masking in chatbots, customer support, email filtering, data anonymization, content moderation, etc.
How many epochs have been used in the finetuning?	Not specified
How many model parameters (weights) does the model have?	3.21B (Llama-3.2-3B-Instruct base)
What is the science domain of the model?	Privacy, legal, business, psychology, NLP
What is the task solved by this model (regression or classification or forecast etc.)?	Token classification and text generation (PII redaction)
What is the intended use of this model?	Commercial and research use for privacy masking and PII redaction in English text
What is the size of the final model in Mb?	LoRA adapter size not specified; base model is ~6.43 GB, LoRA adapter is typically much smaller (tens to hundreds of MB)
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	QLoRA (4-bit quantisation, LoRA rank 16)
What is the claimed performance of this model?	Placeholder micro-F1: ~0.90 (precision ~0.91, recall ~0.90); exact match: ~0.67; formatting errors: ~0.00
Are the performance shown in the pretrained version improved in the finetuning?	Yes; the finetuned LoRA adapter achieves high placeholder micro-F1 and exact match scores for PII redaction, which are not present in the base pretrained model.