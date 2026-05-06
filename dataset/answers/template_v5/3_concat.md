How many activities are present in the whole workflow?	There are 3 activities present in the whole workflow: DataPreparation, ModelFinetuning, and ModelEvaluation.
What is the final status of the workflow?	The final status of the workflow is Completed, with all activities marked as success.
What is the time to completion of the workflow?	The exact time to completion is not specified in the cards; fields for started_at, ended_at, and duration are marked as ~.
List all the parameters of the first activity of the workflow	The first activity, DataPreparation, uses the parameter: filtering the ai4privacy/pii-masking-200k dataset to the English subset, formatting as instruction/assistant pairs with <safe>…</safe> output wrapper, and creating a train/test split with 300 random samples held out for evaluation.
What hardware was used in the workflow?	The specific hardware for the workflow is not detailed in the workflow card; fields for compute_hardware and hosts are marked as ~.
Who is responsible for this workflow (person or username or entity)?	The responsible entity is not specified; fields for user and entrypoint.repository are marked as ~.
What was the specific execution order of the tasks?	The execution order of the tasks is: 1. DataPreparation, 2. ModelFinetuning, 3. ModelEvaluation.
List all parameters for all activites in the workflow	Parameters for all activities: DataPreparation: English subset filtering, formatting, train/test split. ModelFinetuning: LoRA rank 16, LoRA alpha 32, LoRA dropout 0.05, quantisation 4-bit NF4, sequence length 320–512, batch size 1, gradient accumulation steps 16, learning rate 2e-4, scheduler cosine, warmup 3%, loss mask assistant span only. ModelEvaluation: evaluation on 300 held-out samples, metrics: exact match, placeholder micro-F1, formatting errors.
What was the peak RAM consumption during the workflow?	Peak RAM consumption is not specified in the workflow card; memory field is marked as ~.
Has the model been trained in a distributed setting?	There is no explicit mention of distributed training for the finetuning workflow; the cards do not specify distributed or multi-node training.
What was the total power consumption in Watts of the GPU(s) during the workflow?	The total power consumption in Watts is not specified for the finetuning workflow; the cards do not provide this information.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts are: meta-llama/Llama-3.2-3B-Instruct (pretrained base model) and ai4privacy/pii-masking-200k (English subset of the dataset).
What is the total energy use for completing the workflow?	Total energy use for the finetuning workflow is not specified; the cards do not provide this information.
List all input files with size larger than 100Mb	The input files larger than 100Mb are: meta-llama/Llama-3.2-3B-Instruct (model weights, ~6.43 GB) and ai4privacy/pii-masking-200k (dataset, ~13.6M text tokens, ~209k examples).
List all different file types used as input	Input file types used are: JSONL (for dataset), safetensors (for model weights), and text files (for documentation and Notice).
Identify the largest output	The largest output is the Llama-3.2-3B-PII-Redactor (LoRA adapter), which consists of PEFT LoRA adapter weights compatible with the 4-bit quantised base model.
What is the science domain of the dataset?	The science domain of the dataset is privacy, legal, business, psychology, and data anonymization.
Does the dataset have a predetermined train-test split?	Yes, the dataset has a predetermined train-test split, with 300 random samples held out for evaluation.
How many samples are present in the whole dataset?	The whole dataset contains approximately 209,000 examples.
What is the data type of the ground truth (if present)?	The ground truth data type is text, specifically the target_text field with PII replaced by placeholders.
What is the specific task for which the dataset was created?	The dataset was created for the task of PII redaction: detecting and replacing personally identifiable information spans in text with structured placeholders.
What is the size in byte of one sample?	The size in bytes of one sample is not specified, but typical JSONL samples with text and mask fields are likely to be between 1–5 KB each.
What is the total size of the whole dataset?	The total size of the dataset is not explicitly stated, but with ~209k examples and 13.6M text tokens, it is likely several hundred MB.
What are the designed uses for this model?	Designed uses for this model include redacting PII in English text to placeholder labels for downstream processing, audit, and privacy protection, while keeping non-PII text unchanged.
How many epochs have been used in the finetuning?	The number of epochs used in finetuning is not specified in the workflow card.
How many model parameters (weights) does the model have?	The model has 3.21 billion parameters (weights).
What is the science domain of the model?	The science domain of the model is privacy, legal, business, psychology, and data anonymization.
What is the task solved by this model (regression or classification or forecast etc.)?	The task solved by this model is classification (token classification and text generation for PII redaction).
What is the intended use of this model?	The intended use of this model is to redact PII in English text by replacing detected spans with placeholders, for privacy protection and downstream processing.
What is the size of the final model in Mb?	The final model size is not specified for the LoRA adapter alone, but the base model is ~6.43 GB; LoRA adapters are typically much smaller (tens to hundreds of MB).
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The technique used to fine-tune the model is QLoRA (4-bit quantisation with LoRA rank 16).
What is the claimed performance of this model?	The claimed performance is: exact match ~0.67, placeholder micro-F1 ~0.90 (precision ~0.91, recall ~0.90), formatting errors ~0.00 on 300 random test samples.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the finetuned model achieves specialized PII redaction performance (micro-F1 ~0.90, exact match ~0.67), which is improved compared to the generic pretrained base model.