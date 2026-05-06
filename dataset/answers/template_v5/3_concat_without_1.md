How many activities are present in the whole workflow?	There are three main activities in the workflow: pretraining, quantization-aware training (QAT) with LoRA, and direct preference optimization (DPO).
What is the final status of the workflow?	The workflow is completed, resulting in a static, instruction-tuned, quantized, and LoRA-adapted model ready for deployment.
What is the time to completion of the workflow?	The total training time for the 3B model is 460,000 GPU hours, with additional time for QLoRA (1,600 GPU hours) and SpinQuant (2.4 GPU hours).
List all the parameters of the first activity of the workflow	The first activity (pretraining) uses: model size (3.21B parameters), context length (128k), GQA enabled, shared embeddings, token count (up to 9T), and training data from publicly available sources.
What hardware was used in the workflow?	Meta's custom built GPU cluster using H100-80GB GPUs (TDP of 700W).
Who is responsible for this workflow (person or username or entity)?	Meta Platforms, Inc. and Meta Platforms Ireland Limited are responsible for the workflow.
What was the specific execution order of the tasks?	Pretraining → Quantization-aware training (QAT) with LoRA → Direct preference optimization (DPO) → Evaluation and benchmarking.
List all parameters for all activites in the workflow	Pretraining: model size, context length, GQA, shared embeddings, token count, training data. QAT with LoRA: LoRA rank 16, alpha 32, dropout 0.05, sequence length 320-512, batch size 1, gradient accumulation 16, learning rate 2e-4, cosine schedule, warmup 3%. DPO: fine-tuning both backbone and LoRA adaptors.
What was the peak RAM consumption during the workflow?	Peak memory usage for the 3B model during inference is 7,419 MB (BF16 baseline), reduced to 4,060 MB with QLoRA.
Has the model been trained in a distributed setting?	Yes, the model was trained on Meta's production infrastructure with distributed GPU clusters.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Each H100-80GB GPU used has a peak power consumption of 700W.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts include the pretraining dataset (up to 9T tokens), Llama 3.1 8B and 70B logits, and the ai4privacy/pii-masking-200k dataset for finetuning.
What is the total energy use for completing the workflow?	Estimated total location-based greenhouse gas emissions for training are 240 tons CO2eq; total GPU hours are 916,000.
List all input files with size larger than 100Mb	The pretraining dataset and model checkpoint files (e.g., PTE files for the 3B model, 2,529 MB for QLoRA) are larger than 100Mb.
List all different file types used as input	Input file types include text datasets (jsonl), model checkpoint files (PTE), and image files (PNG for token distribution graphs).
Identify the largest output	The largest output is the final model checkpoint for Llama-3.2-3B QLoRA, with a PTE file size of 2,529 MB.
What is the science domain of the dataset?	The science domain of the dataset is privacy and data anonymization in natural language processing.
Does the dataset have a predetermined train-test split?	Yes, the ai4privacy/pii-masking-200k dataset includes train and test splits.
How many samples are present in the whole dataset?	The dataset contains approximately 209,000 examples.
What is the data type of the ground truth (if present)?	The ground truth is text, specifically the masked_text (PII-free natural text).
What is the specific task for which the dataset was created?	The dataset was created for PII masking and redaction in text (token classification and text generation).
What is the size in byte of one sample?	One sample is approximately 65 bytes (based on average text length).
What is the total size of the whole dataset?	The total size of the dataset is approximately 13.6 million text tokens, or several hundred megabytes.
What are the designed uses for this model?	Designed uses include redacting PII in English text, privacy masking for chatbots, customer support, email filtering, data anonymization, content moderation, and research.
How many epochs have been used in the finetuning?	The exact number of epochs is not specified, but the finetuning used batch size 1 with gradient accumulation 16 and a cosine schedule with 3% warmup.
How many model parameters (weights) does the model have?	The model has 3.21 billion parameters.
What is the science domain of the model?	The science domain of the model is natural language processing, privacy, and data anonymization.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves token classification and text generation tasks (PII redaction).
What is the intended use of this model?	The intended use is for commercial and research applications in privacy masking, agentic chat, and text redaction.
What is the size of the final model in Mb?	The final model size is 2,529 MB (QLoRA version).
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using QLoRA (quantization-aware training with LoRA adapters).
What is the claimed performance of this model?	Claimed performance: Exact match ~0.67, Placeholder micro-F1 ~0.90 (Precision ~0.91, Recall ~0.90), Formatting errors ~0.00.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, finetuning with QLoRA and the ai4privacy/pii-masking-200k dataset improved performance for PII redaction tasks.