How many activities are present in the whole workflow?	1	The workflow consists of a single activity: fine-tuning the base model meta-llama/Llama-3.2-3B-Instruct using QLoRA with the ai4privacy/pii-masking-200k dataset.
What is the final status of the workflow?	Completed	The workflow was successfully completed, resulting in a LoRA adapter for PII redaction.
What is the time to completion of the workflow?	Not specified	The cards do not provide information about the total time taken to complete the workflow.
List all the parameters of the first activity of the workflow	LoRA rank 16, alpha 32, dropout 0.05, sequence length 320 to 512, batch size 1, gradient accumulation 16, learning rate 2e-4, cosine schedule, warmup 3 percent, loss computed only on assistant span between <safe> and </safe>	These are the parameters used for the fine-tuning activity.
What hardware was used in the workflow?	Not specified	The cards do not mention the specific hardware used for training or inference.
Who is responsible for this workflow (person or username or entity)?	Not specified	The responsible person, username, or entity is not provided in the cards.
What was the specific execution order of the tasks?	Fine-tuning base model with QLoRA → Evaluation on test samples → Sharing adapter	The workflow started with fine-tuning, followed by evaluation, and then sharing the adapter.
List all parameters for all activites in the workflow	LoRA rank 16, alpha 32, dropout 0.05, sequence length 320 to 512, batch size 1, gradient accumulation 16, learning rate 2e-4, cosine schedule, warmup 3 percent, loss computed only on assistant span between <safe> and </safe>	All parameters pertain to the single fine-tuning activity.
What was the peak RAM consumption during the workflow?	Not specified	Peak RAM consumption is not mentioned in the cards.
Has the model been trained in a distributed setting?	Not specified	There is no information about distributed training in the cards.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Not specified	Total GPU power consumption is not provided.
What significant input artifacts are involved in the generation of the finetuned model?	meta-llama/Llama-3.2-3B-Instruct, ai4privacy/pii-masking-200k dataset	The base model and the dataset are the main input artifacts.
What is the total energy use for completing the workflow?	Not specified	Total energy use is not reported.
List all input files with size larger than 100Mb	Not specified	The cards do not list input files or their sizes.
List all different file types used as input	Not specified	The cards do not specify file types used as input.
Identify the largest output	LoRA adapter	The largest output is the LoRA adapter for PII redaction.
What is the science domain of the dataset?	Privacy, Natural Language Processing	The dataset is focused on privacy and NLP, specifically PII masking.
Does the dataset have a predetermined train-test split?	Yes	The dataset was evaluated on 300 random test samples, indicating a train-test split.
How many samples are present in the whole dataset?	200,000	The ai4privacy/pii-masking-200k dataset contains 200,000 samples (English subset).
What is the data type of the ground truth (if present)?	Text with PII spans replaced by placeholders	The ground truth consists of text where PII spans are replaced by placeholders.
What is the specific task for which the dataset was created?	PII redaction in English text	The dataset was created for the task of redacting PII in English text.
What is the size in byte of one sample?	Not specified	The cards do not provide the size in bytes of a single sample.
What is the total size of the whole dataset?	Not specified	The total dataset size is not mentioned.
What are the designed uses for this model?	Redacting PII in English text to placeholder labels for downstream processing or audit; keeping non-PII text unchanged	The model is intended for practical PII redaction in English text.
How many epochs have been used in the finetuning?	Not specified	The number of epochs used for finetuning is not provided.
How many model parameters (weights) does the model have?	3 billion	The base model meta-llama/Llama-3.2-3B-Instruct has 3 billion parameters.
What is the science domain of the model?	Privacy, Natural Language Processing	The model is designed for privacy and NLP applications.
What is the task solved by this model (regression or classification or forecast etc.)?	Classification (span detection and replacement)	The model performs classification by detecting and replacing PII spans.
What is the intended use of this model?	Redacting PII in English text to placeholder labels for downstream processing or audit	The model is intended for PII redaction in English text.
What is the size of the final model in Mb?	Not specified	The cards do not specify the size of the final model in megabytes.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	QLoRA (LoRA rank 16)	The model was fine-tuned using QLoRA with LoRA rank 16.
What is the claimed performance of this model?	Exact match: ~0.67; Placeholder micro-F1: ~0.90 (P~0.91, R~0.90); Formatting errors: ~0.00	The model achieves high micro-F1 and precision/recall, with low formatting errors.
Are the performance shown in the pretrained version improved in the finetuning?	Yes	The finetuned model achieves high micro-F1 and exact match scores for PII redaction, indicating improved performance for the specific task.