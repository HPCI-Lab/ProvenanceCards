How many activities are present in the whole workflow?	The workflow contains 3 activities: DataPreparation, ModelFinetuning, and ModelEvaluation.
What is the final status of the workflow?	The final status of the workflow is Completed.
What is the time to completion of the workflow?	The workflow took 12 hours, 33 minutes, and 33 seconds to complete.
List all the parameters of the first activity of the workflow	The first activity, DataPreparation, uses the following parameters: input dataset ai4privacy/pii-masking-200k (full), filters for English-only subset, formats as instruction/assistant pairs with <safe>…</safe> output wrapper, and creates a train/test split with 300 random samples held out for evaluation.
What hardware was used in the workflow?	The workflow used 1× NVIDIA A10G-24GB GPU, AMD EPYC 7R32 CPU, and 64 GB RAM on an AWS EC2 g5.4xlarge instance.
Who is responsible for this workflow (person or username or entity)?	The workflow was executed by the ml-privacy-team.
What was the specific execution order of the tasks?	The execution order was: 1. DataPreparation, 2. ModelFinetuning, 3. ModelEvaluation.
List all parameters for all activites in the workflow	DataPreparation: input dataset ai4privacy/pii-masking-200k (full), English-only filter, instruction/assistant formatting, train/test split. ModelFinetuning: base model meta-llama/Llama-3.2-3B-Instruct, quantisation 4-bit NF4, LoRA rank 16, LoRA alpha 32, LoRA dropout 0.05, sequence length 320–512, batch size 1, gradient accumulation steps 16, learning rate 2e-4, scheduler cosine, warmup 3%, loss mask assistant span only. ModelEvaluation: input LoRA adapter, 300-sample evaluation split.
What was the peak RAM consumption during the workflow?	Peak RAM usage was 31 GB.
Has the model been trained in a distributed setting?	No, the model was trained on a single node with 1 GPU.
What was the total power consumption in Watts of the GPU(s) during the workflow?	The NVIDIA A10G-24GB GPU has a TDP of 300W; for 12.5 hours, total power consumption is approximately 3,750 Wh (3.75 kWh).
What significant input artifacts are involved in the generation of the finetuned model?	The significant input artifacts are meta-llama/Llama-3.2-3B-Instruct (pretrained base model) and ai4privacy/pii-masking-200k (English subset of the dataset).
What is the total energy use for completing the workflow?	Total energy use is approximately 3.75 kWh (12.5 hours × 300W GPU).
List all input files with size larger than 100Mb	The input files larger than 100MB are: meta-llama/Llama-3.2-3B-Instruct model weights (~6.43 GB) and ai4privacy/pii-masking-200k dataset (~11 GB for English subset).
List all different file types used as input	Input file types include: JSONL (dataset), safetensors (model weights), and possibly binary files for tokenised sequence cache.
Identify the largest output	The largest output is the Llama-3.2-3B-PII-Redactor (LoRA adapter), approximately 180 MB.
What is the science domain of the dataset?	The dataset is in the privacy and data anonymization domain, with applications in business, education, psychology, and legal fields.
Does the dataset have a predetermined train-test split?	Yes, the dataset was split with 300 random samples held out for evaluation.
How many samples are present in the whole dataset?	The dataset contains approximately 209,000 examples.
What is the data type of the ground truth (if present)?	The ground truth is text, specifically the target_text field with PII replaced by placeholders.
What is the specific task for which the dataset was created?	The dataset was created for PII redaction (token classification and text generation for privacy masking).
What is the size in byte of one sample?	Each sample is approximately 65 KB (13.6M tokens / 209k samples ≈ 65 tokens per sample; assuming 1 KB per sample for text and metadata).
What is the total size of the whole dataset?	The total size of the dataset is approximately 11 GB for the English subset.
What are the designed uses for this model?	The model is designed for PII redaction in English text, replacing detected PII spans with structured placeholders while preserving non-PII content.
How many epochs have been used in the finetuning?	The number of epochs is not explicitly stated in the card.
How many model parameters (weights) does the model have?	The base model has 3.21 billion parameters; the LoRA adapter adds a small number of trainable parameters (rank 16).
What is the science domain of the model?	The model is in the privacy, data anonymization, and natural language processing domain.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves a token classification and text generation (sequence-to-sequence) task for PII redaction.
What is the intended use of this model?	The intended use is to detect and redact PII in English text, replacing sensitive spans with placeholders for privacy protection.
What is the size of the final model in Mb?	The LoRA adapter is approximately 180 MB; the base model is ~6.43 GB.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using QLoRA (4-bit quantisation with LoRA rank 16).
What is the claimed performance of this model?	The model achieves placeholder micro-F1 of ~0.90 (precision ~0.91, recall ~0.90) and exact match of ~0.67 on a 300-sample held-out test set.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the finetuned model is specialized for PII redaction, a task not covered by the base pretrained model, resulting in improved performance for this use case.