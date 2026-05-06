How many activities are present in the whole workflow?	Not specified in the provided cards.
What is the final status of the workflow?	Not specified in the provided cards.
What is the time to completion of the workflow?	Not specified in the provided cards.
List all the parameters of the first activity of the workflow	Not specified in the provided cards.
What hardware was used in the workflow?	Older GPUs (attn_implementation="eager" is friendly for older GPUs); 4-bit load with bitsandbytes.
Who is responsible for this workflow (person or username or entity)?	Not specified in the provided cards.
What was the specific execution order of the tasks?	Not specified in the provided cards.
List all the parameters for the whole workflow process	LoRA rank 16, alpha 32, dropout 0.05; Sequence length 320 to 512; Batch size 1 with gradient accumulation 16; Learning rate 2e-4, cosine schedule, warmup 3 percent; Loss computed only on the assistant span between <safe> and </safe>.
What was the peak RAM consumption during the workflow?	Not specified in the provided cards.
Has the model been trained in a distributed setting?	Not specified in the provided cards.
What was the real-time power consumption (in Watts) of the GPU during the workflow?	Not specified in the provided cards.
Which inputs influenced the output in the workflow?	English text input; ai4privacy/pii-masking-200k dataset (English subset).
What is the total energy use for completing the workflow?	Not specified in the provided cards.
List all input files with size larger than 100Mb	Not specified in the provided cards.
List all different file types used as input	Not specified in the provided cards.
Identify the largest output	Not specified in the provided cards.
What is the science domain of the dataset?	Privacy, data protection.
Does the dataset have a predetermined train-test split?	Yes, evaluated on 300 random test samples.
How many samples are present in the whole dataset?	200,000 (from ai4privacy/pii-masking-200k).
What is the data type of the ground truth (if present)?	Text with PII spans replaced by placeholders.
What is the specific task for which the dataset was created?	PII masking/redaction in English text.
What is the size in byte of one sample?	Not specified in the provided cards.
What is the total size of the whole dataset?	Not specified in the provided cards.
What are the designed uses for this model?	Redacting PII in English text to placeholder labels for downstream processing or audit; keep the non-PII text unchanged as much as possible.
How many epochs have been used in the final training?	Not specified in the provided cards.
How many model parameters (weights) does the model have?	3B (3 billion) parameters (from meta-llama/Llama-3.2-3B-Instruct).
What is the science domain of the model?	Privacy, data protection.
What is the task solved by this model (regression or classification or forecast etc.)?	PII redaction (text generation with placeholder replacement).
What is the intended use of this model?	Redacting PII in English text to placeholder labels for downstream processing or audit.
What is the size of the final model in Mb?	Not specified in the provided cards.
What technique was used to train the model?	QLoRA on a 4-bit base, LoRA rank 16.
What is the claimed performance of this model?	Exact match: ~0.67; Placeholder micro-F1: ~0.90 (P~0.91, R~0.90); Formatting errors: ~0.00.
Are the performance shown in the pretrained version improved in the finetuning?	Finet