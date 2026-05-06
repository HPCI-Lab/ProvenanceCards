How many activities are present in the whole workflow?	There is one main activity in the workflow: fine-tuning the base model meta-llama/Llama-3.2-3B-Instruct using QLoRA with the ai4privacy/pii-masking-200k dataset.
What is the final status of the workflow?	The workflow completed successfully, resulting in a LoRA adapter for PII redaction on top of the base model.
What is the time to completion of the workflow?	The exact time to completion is not specified in the provided cards.
List all the parameters of the first activity of the workflow	Parameters include: 4-bit load with bitsandbytes, LoRA rank 16, alpha 32, dropout 0.05, sequence length 320 to 512, batch size 1 with gradient accumulation 16, learning rate 2e-4, cosine schedule, warmup 3 percent, loss computed only on the assistant span between <safe> and </safe>.
What hardware was used in the workflow?	The workflow was run on hardware compatible with bitsandbytes 4-bit quantization and supports torch.float16; attn_implementation="eager" is used for older GPUs, but specific hardware details are not provided.
Who is responsible for this workflow (person or username or entity)?	The responsible entity is the author of the repository, referenced as <your-username>/<your-repo-name> in the quick start instructions.
What was the specific execution order of the tasks?	The execution order: load base model, apply LoRA adapter, configure quantization, set training parameters, train on dataset, evaluate on test samples, and deploy for inference.
List all parameters for all activites in the workflow	Parameters: 4-bit load with bitsandbytes, LoRA rank 16, alpha 32, dropout 0.05, sequence length 320 to 512, batch size 1, gradient accumulation 16, learning rate 2e-4, cosine schedule, warmup 3 percent, loss on assistant span, attn_implementation="eager", torch.float16.
What was the peak RAM consumption during the workflow?	Peak RAM consumption is not specified in the provided cards.
Has the model been trained in a distributed setting?	There is no indication that the model was trained in a distributed setting; batch size 1 with gradient accumulation suggests single-node training.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Total power consumption in Watts is not specified in the provided cards.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts: meta-llama/Llama-3.2-3B-Instruct base model and ai4privacy/pii-masking-200k dataset (English subset).
What is the total energy use for completing the workflow?	Total energy use is not specified in the provided cards.
List all input files with size larger than 100Mb	The ai4privacy/pii-masking-200k dataset is likely larger than 100Mb, but exact file sizes are not specified.
List all different file types used as input	Input file types include model weights (likely .bin or .pt) and dataset files (likely .json, .csv, or similar).
Identify the largest output	The largest output is the LoRA adapter for the finetuned model.
What is the science domain of the dataset?	The science domain of the dataset is privacy and data protection, specifically PII masking in text.
Does the dataset have a predetermined train-test split?	Yes, the dataset was evaluated on 300 random test samples, indicating a train-test split.
How many samples are present in the whole dataset?	The dataset contains 200,000 samples, as indicated by its name ai4privacy/pii-masking-200k.
What is the data type of the ground truth (if present)?	The ground truth is text with PII spans replaced by placeholders.
What is the specific task for which the dataset was created?	The dataset was created for the task of PII redaction in English text.
What is the size in byte of one sample?	The size in bytes of one sample is not specified in the provided cards.
What is the total size of the whole dataset?	The total size of the dataset is not specified, but with 200,000 samples it is likely over 100Mb.
What are the designed uses for this model?	Designed uses: redacting PII in English text to placeholder labels for downstream processing or audit, keeping non-PII text unchanged.
How many epochs have been used in the finetuning?	The number of epochs used in finetuning is not specified in the provided cards.
How many model parameters (weights) does the model have?	The base model meta-llama/Llama-3.2-3B-Instruct has 3 billion parameters.
What is the science domain of the model?	The science domain of the model is privacy and data protection, specifically automated PII redaction in text.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves a sequence labeling and text generation task for PII redaction.
What is the intended use of this model?	Intended use: redacting PII in English text to placeholder labels for downstream processing or audit, keeping non-PII text unchanged.
What is the size of the final model in Mb?	The size of the final model is not specified, but the base model is 3B parameters and the LoRA adapter is smaller; likely several GB for the base and tens to hundreds of MB for the adapter.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using QLoRA (Quantized Low-Rank Adaptation) with LoRA rank 16.
What is the claimed performance of this model?	Claimed performance: Exact match ~0.67, Placeholder micro-F1 ~0.90 (Precision ~0.91, Recall ~0.90), Formatting errors ~0.00.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the finetuning specifically improved the model's ability to redact PII and map it to clear placeholder taxonomy, as measured by the reported metrics.