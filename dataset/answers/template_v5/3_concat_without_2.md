How many activities are present in the whole workflow?	There are three activities present in the whole workflow: DataPreparation, ModelFinetuning, and ModelEvaluation.
What is the final status of the workflow?	The final status of the workflow is Completed, with all activities marked as success.
What is the time to completion of the workflow?	The exact time to completion is not specified in the card; fields for started_at, ended_at, and duration are marked as ~.
List all the parameters of the first activity of the workflow	The first activity, DataPreparation, uses the parameter: filtering the ai4privacy/pii-masking-200k dataset to the English subset, formatting as instruction/assistant pairs with <safe>…</safe> output wrapper, and creating a train/test split with 300 random samples held out for evaluation.
What hardware was used in the workflow?	The specific hardware used for the workflow is not detailed in the workflow card; fields for compute_hardware and hosts are marked as ~.
Who is responsible for this workflow (person or username or entity)?	The responsible user or entity is not specified; the field for user is marked as ~.
What was the specific execution order of the tasks?	The execution order of the tasks is: 1. DataPreparation, 2. ModelFinetuning, 3. ModelEvaluation.
List all parameters for all activites in the workflow	DataPreparation: English subset filtering, formatting as instruction/assistant pairs, train/test split. ModelFinetuning: LoRA rank 16, LoRA alpha 32, LoRA dropout 0.05, quantisation 4-bit NF4, sequence length 320–512, batch size 1, gradient accumulation steps 16, learning rate 2e-4, scheduler cosine, warmup 3%, loss mask assistant span only. ModelEvaluation: evaluation on 300 held-out samples, metrics exact match, placeholder micro-F1, formatting errors.
What was the peak RAM consumption during the workflow?	Peak RAM consumption is not specified in the workflow card; the field for memory is marked as ~.
Has the model been trained in a distributed setting?	The workflow card does not specify whether distributed training was used; this information is not available.
What was the total power consumption in Watts of the GPU(s) during the workflow?	The workflow card does not specify the total power consumption in Watts for the GPU(s) used in the workflow.
What significant input artifacts are involved in the generation of the finetuned model?	The significant input artifacts are meta-llama/Llama-3.2-3B-Instruct (pretrained base model) and ai4privacy/pii-masking-200k (English subset of the dataset).
What is the total energy use for completing the workflow?	The total energy use for completing the workflow is not specified in the workflow card.
List all input files with size larger than 100Mb	The input files larger than 100Mb are meta-llama/Llama-3.2-3B-Instruct (model weights, ~6.43 GB) and ai4privacy/pii-masking-200k (dataset, ~13.6M text tokens, ~209k examples).
List all different file types used as input	The input file types are JSONL (for the dataset) and safetensors (for the model weights).
Identify the largest output	The largest output is the Llama-3.2-3B-PII-Redactor (LoRA adapter), which is a PEFT LoRA adapter compatible with the 4-bit quantised base model.
What is the science domain of the dataset?	The science domain of the dataset is privacy and natural language processing, specifically PII detection and redaction.
Does the dataset have a predetermined train-test split?	Yes, the dataset has a predetermined train-test split, with 300 random samples held out for evaluation.
How many samples are present in the whole dataset?	The whole dataset contains approximately 209,000 examples.
What is the data type of the ground truth (if present)?	The ground truth data type is text, specifically target_text with PII replaced by bracketed placeholders.
What is the specific task for which the dataset was created?	The dataset was created for the task of PII redaction in text, replacing detected PII spans with structured placeholders.
What is the size in byte of one sample?	The size in bytes of one sample is not specified in the workflow card.
What is the total size of the whole dataset?	The total size of the dataset is not specified in bytes, but it contains ~13.6M text tokens and ~209k examples.
What are the designed uses for this model?	The designed uses for this model are redacting PII in English text to placeholder labels for downstream processing or audit, while keeping non-PII text unchanged.
How many epochs have been used in the finetuning?	The number of epochs used in finetuning is not specified in the workflow card.
How many model parameters (weights) does the model have?	The model has 3.21 billion parameters (weights).
What is the science domain of the model?	The science domain of the model is natural language processing, specifically privacy-preserving text generation and PII redaction.
What is the task solved by this model (regression or classification or forecast etc.)?	The task solved by this model is sequence-to-sequence text generation for PII redaction (structured text rewriting).
What is the intended use of this model?	The intended use of this model is to redact PII in English text by replacing detected spans with placeholders, preserving all non-PII content.
What is the size of the final model in Mb?	The final model size is not specified for the LoRA adapter alone, but the base model is ~6.43 GB; LoRA adapters are typically much smaller.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The technique used to fine-tune the model is QLoRA (4-bit quantisation with LoRA rank 16).
What is the claimed performance of this model?	The claimed performance is exact match ~0.67, placeholder micro-F1 ~0.90 (precision ~0.91, recall ~0.90), formatting errors ~0.00 on 300 random test samples.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the finetuned model achieves high placeholder micro-F1 and exact match scores for PII redaction, which are improvements over the base pretrained model for this specific task.