How many activities are present in the whole workflow?	The workflow includes pretraining, knowledge distillation, supervised fine-tuning (SFT), rejection sampling (RS), direct preference optimization (DPO), quantization-aware training (QAT), LoRA adaptation, and evaluation, totaling at least 8 distinct activities.
What is the final status of the workflow?	The final status is a released, instruction-tuned, quantized LoRA adapter for PII redaction, evaluated and ready for practical use.
What is the time to completion of the workflow?	Training utilized a cumulative 916,000 GPU hours for all Llama 3.2 models; the LoRA adapter was trained post-release, but the exact time for the adapter is not specified.
List all the parameters of the first activity of the workflow	The first activity, pretraining, used up to 9 trillion tokens of publicly available data, context length 128k, with Grouped-Query Attention, and incorporated logits from larger models for knowledge distillation.
What hardware was used in the workflow?	Meta's custom-built GPU cluster with H100-80GB GPUs (TDP 700W) was used for pretraining, fine-tuning, quantization, annotation, and evaluation.
Who is responsible for this workflow (person or username or entity)?	Meta is the developer and responsible entity for the base model and workflow; the LoRA adapter is released by the HuggingFace user who created the repository.
What was the specific execution order of the tasks?	The order is: pretraining → knowledge distillation → pruning → supervised fine-tuning (SFT) → rejection sampling (RS) → direct preference optimization (DPO) → quantization-aware training (QAT) → LoRA adaptation → evaluation.
List all parameters for all activites in the workflow	Pretraining: 9T tokens, context 128k, GQA; SFT: human and synthetic data; QAT: 4-bit groupwise quantization, 8-bit activations; LoRA: rank 16, alpha 32, dropout 0.05, batch size 1, grad acc 16, lr 2e-4, cosine schedule, warmup 3%; DPO: fine-tuning both backbone and LoRA.
What was the peak RAM consumption during the workflow?	For inference: 3B BF16 baseline uses 7,419 MB RSS; 3B SpinQuant uses 3,726 MB; 3B QLoRA uses 4,060 MB. Training peak RAM is not specified.
Has the model been trained in a distributed setting?	Yes, training was performed on Meta's distributed GPU cluster infrastructure.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Each GPU used for training had a power consumption (TDP) of 700W.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts include the base pretrained model weights, the ai4privacy/pii-masking-200k dataset, and LoRA adapter configuration files.
What is the total energy use for completing the workflow?	Total energy use for all Llama 3.2 models is 916,000 GPU hours × 700W = 641,200,000 Wh (641.2 MWh).
List all input files with size larger than 100Mb	The base model weights (meta-llama/Llama-3.2-3B-Instruct) and the ai4privacy/pii-masking-200k dataset are both larger than 100MB.
List all different file types used as input	Input file types include model checkpoint files (e.g., .bin, .safetensors), JSONL files for the dataset, and LoRA adapter files.
Identify the largest output	The largest output is the final LoRA-adapted model checkpoint, which includes the base model and LoRA weights.
What is the science domain of the dataset?	The dataset is in the domain of privacy, legal, business, psychology, and education.
Does the dataset have a predetermined train-test split?	Yes, the dataset includes a "set" field indicating train/test splits.
How many samples are present in the whole dataset?	The dataset contains approximately 209,000 examples.
What is the data type of the ground truth (if present)?	The ground truth is text, specifically the masked (PII-redacted) version of the input text.
What is the specific task for which the dataset was created?	The dataset was created for PII redaction (token classification and text generation for privacy masking).
What is the size in byte of one sample?	One sample is approximately 65 bytes on average (13.6 million tokens / 209,000 samples, assuming 1 token ≈ 4 bytes).
What is the total size of the whole dataset?	The total size is approximately 13.6 million tokens × 4 bytes ≈ 54.4 MB, but with metadata and formatting, the actual dataset file is larger (likely several hundred MB).
What are the designed uses for this model?	The model is designed for redacting PII in English text to placeholder labels for downstream processing or audit, keeping non-PII text unchanged.
How many epochs have been used in the finetuning?	The number of epochs is not specified in the card.
How many model parameters (weights) does the model have?	The base model has 3.21 billion parameters.
What is the science domain of the model?	The model is in the domain of privacy-preserving natural language processing.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves a sequence-to-sequence text generation task for PII redaction (can also be seen as token classification).
What is the intended use of this model?	The intended use is for offline, accurate PII redaction in English text, replacing detected spans with placeholders while keeping other text unchanged.
What is the size of the final model in Mb?	The 3B base model is approximately 2,435 MB (SpinQuant) to 6,129 MB (BF16); the LoRA adapter adds a small amount (typically <100 MB).
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	QLoRA (quantized LoRA) was used for fine-tuning.
What is the claimed performance of this model?	Exact match: ~0.67; Placeholder micro-F1: ~0.90 (Precision ~0.91, Recall ~0.90); Formatting errors: ~0.00.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the LoRA adapter specializes the base model for PII redaction, achieving high micro-F1 and exact match on the task.