How many activities are present in the whole workflow?	The workflow includes pretraining, knowledge distillation, pruning, supervised fine-tuning (SFT), rejection sampling (RS), direct preference optimization (DPO), quantization-aware training (QAT), LoRA adaptation, and evaluation. This totals at least 8 distinct activities.
What is the final status of the workflow?	The final status is a released, instruction-tuned, quantized, and evaluated Llama 3.2 model, ready for deployment and use.
What is the time to completion of the workflow?	Training time for Llama 3.2 1B is 370,000 GPU hours and for 3B is 460,000 GPU hours. Additional time for fine-tuning and quantization is minimal in comparison.
List all the parameters of the first activity of the workflow	The first activity, pretraining, uses up to 9 trillion tokens of publicly available multilingual text, with model sizes of 1.23B and 3.21B parameters, context length up to 128k, and Grouped-Query Attention enabled.
What hardware was used in the workflow?	Custom-built GPU clusters using H100-80GB GPUs (TDP of 700W) were used for training, fine-tuning, quantization, annotation, and evaluation.
Who is responsible for this workflow (person or username or entity)?	Meta Platforms, Inc. (or Meta Platforms Ireland Limited for EEA/Switzerland) is responsible for the workflow.
What was the specific execution order of the tasks?	Pretraining → Knowledge distillation → Pruning → Supervised Fine-Tuning (SFT) → Rejection Sampling (RS) → Direct Preference Optimization (DPO) → Quantization (SpinQuant/QLoRA) → Evaluation.
List all parameters for all activites in the workflow	Pretraining: up to 9T tokens, 1.23B/3.21B params, context 128k; Knowledge distillation: Llama 3.1 8B/70B logits; Pruning: not specified; SFT: human/synthetic data; RS: not specified; DPO: not specified; Quantization: 4-bit groupwise, 8-bit activations, group size 32; QAT: LoRA adapters in BF16; Evaluation: standard benchmarks.
What was the peak RAM consumption during the workflow?	For inference: 3B model SpinQuant uses 3,726 MB RSS on device; training RAM is not specified.
Has the model been trained in a distributed setting?	Yes, training was performed on Meta’s custom-built GPU clusters, implying distributed training.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Each GPU used has a power consumption (TDP) of 700W.
What significant input artifacts are involved in the generation of the finetuned model?	Publicly available multilingual text data (up to 9T tokens), Llama 3.1 8B/70B logits, human and synthetic alignment data.
What is the total energy use for completing the workflow?	Total energy use is not directly stated, but training used 916,000 GPU hours at 700W per GPU.
List all input files with size larger than 100Mb	Pretraining data (up to 9T tokens) and model checkpoints (1.23B/3.21B parameters) are each much larger than 100MB.
List all different file types used as input	Text data files, model checkpoint files, and logit files from Llama 3.1 models.
Identify the largest output	The largest output is the Llama 3.2 3B model checkpoint, with a PTE file size of 6,129 MB (BF16 baseline).
What is the science domain of the dataset?	The dataset is in the domain of natural language processing (NLP), covering multilingual text and code.
Does the dataset have a predetermined train-test split?	Not specified; standard benchmarks are used for evaluation, but pretraining data split is not detailed.
How many samples are present in the whole dataset?	Not specified in terms of samples; the dataset contains up to 9 trillion tokens.
What is the data type of the ground truth (if present)?	Ground truth consists of text (for language modeling and instruction following), and token-level targets from Llama 3.1 logits.
What is the specific task for which the dataset was created?	The dataset is created for multilingual language modeling, instruction following, summarization, rewriting, and agentic tasks.
What is the size in byte of one sample?	Not specified; depends on tokenization, but typically a sample is a sequence of tokens (e.g., 1-2KB per sample).
What is the total size of the whole dataset?	Not specified, but with up to 9T tokens, the dataset is likely multiple terabytes in size.
What are the designed uses for this model?	Commercial and research use in multilingual dialogue, agentic retrieval, summarization, writing assistants, query/prompt rewriting, and on-device applications.
How many epochs have been used in the finetuning?	Not specified in the card.
How many model parameters (weights) does the model have?	Llama 3.2 1B: 1.23 billion parameters; Llama 3.2 3B: 3.21 billion parameters.
What is the science domain of the model?	Natural language processing (NLP), specifically multilingual language modeling and generation.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves generative language modeling tasks (text generation, summarization, rewriting, instruction following).
What is the intended use of this model?	Intended for assistant-like chat, agentic applications, knowledge retrieval, summarization, writing assistants, and prompt rewriting.
What is the size of the final model in Mb?	Llama 3.2 3B BF16 baseline: 6,129 MB; SpinQuant: 2,435 MB; QLoRA: 2,529 MB.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Supervised Fine-Tuning (SFT), Rejection Sampling (RS), Direct Preference Optimization (DPO), Quantization-Aware Training (QAT), LoRA adapters.
What is the claimed performance of this model?	On MMLU (5-shot): 1B: 49.3%, 3B: 63.4%; GSM8K (CoT): 1B: 44.4%, 3B: 77.7%; multilingual MMLU (French): 1B: 40.5%, 3B: 54.6%.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, instruction-tuned models outperform base pretrained models on benchmarks such as MMLU, GSM8K, and others.