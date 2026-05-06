How many activities are present in the whole workflow?	The workflow includes pretraining, knowledge distillation, pruning, supervised fine-tuning (SFT), rejection sampling (RS), direct preference optimization (DPO), quantization-aware training (QAT), LoRA adaptation, and evaluation. This totals at least 8 distinct activities.
What is the final status of the workflow?	The final status is a released, instruction-tuned, multilingual LLM (Llama 3.2) available for commercial and research use, with safety and performance benchmarks reported.
What is the time to completion of the workflow?	Training time for Llama 3.2 1B was 370,000 GPU hours and for 3B was 460,000 GPU hours. The total training time for all models was 833,000 GPU hours.
List all the parameters of the first activity of the workflow	The first activity, pretraining, used up to 9 trillion tokens of publicly available multilingual text, with model sizes of 1.23B and 3.21B parameters, context length up to 128k, and Grouped-Query Attention (GQA).
What hardware was used in the workflow?	Meta's custom-built GPU cluster was used, specifically H100-80GB GPUs (TDP of 700W), for both pretraining and fine-tuning.
Who is responsible for this workflow (person or username or entity)?	Meta Platforms, Inc. (or Meta Platforms Ireland Limited for EEA/Switzerland) is responsible for the workflow and model development.
What was the specific execution order of the tasks?	The order is: pretraining on public data, knowledge distillation with Llama 3.1 logits, pruning, supervised fine-tuning (SFT), rejection sampling (RS), direct preference optimization (DPO), quantization (SpinQuant, QLoRA), and evaluation.
List all parameters for all activites in the workflow	Pretraining: up to 9T tokens, 1.23B/3.21B params, GQA, 128k context; Distillation: Llama 3.1 8B/70B logits; Pruning: model size reduction; SFT: human/synthetic data; RS/DPO: alignment; Quantization: 4-bit/8-bit schemes, group size 32; Evaluation: benchmarks in multiple languages.
What was the peak RAM consumption during the workflow?	For inference, peak RSS was 3,185 MB (1B BF16) and 7,419 MB (3B BF16) on device. Training RAM is not specified.
Has the model been trained in a distributed setting?	Yes, training was performed on Meta’s custom GPU cluster, implying distributed training across many GPUs.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Each GPU used had a power consumption (TDP) of 700W during training.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts include up to 9 trillion tokens of multilingual public text, Llama 3.1 8B/70B logits for distillation, and human/synthetic data for alignment.
What is the total energy use for completing the workflow?	Total energy use is not given directly, but training used 833,000 GPU hours at 700W per GPU, resulting in approximately 582,100 kWh.
List all input files with size larger than 100Mb	Not specified, but the pretraining dataset (up to 9T tokens) and model checkpoints (1.23B/3.21B params) are each much larger than 100MB.
List all different file types used as input	Input file types include text (multilingual corpora), model checkpoints, and logit files from Llama 3.1 models.
Identify the largest output	The largest output is the Llama 3.2 3B model checkpoint, with a PTE file size of 6,129 MB (BF16 baseline).
What is the science domain of the dataset?	The dataset is in the domain of natural language processing (NLP), covering multilingual text and code.
Does the dataset have a predetermined train-test split?	No explicit mention of a predetermined train-test split; benchmarks are used for evaluation.
How many samples are present in the whole dataset?	Exact number of samples is not specified, but the dataset contains up to 9 trillion tokens.
What is the data type of the ground truth (if present)?	Ground truth data types include text (for language modeling), and token-level targets (from Llama 3.1 logits) for distillation.
What is the specific task for which the dataset was created?	The dataset was created for multilingual language modeling, instruction following, summarization, rewriting, and agentic tasks.
What is the size in byte of one sample?	Not specified; varies depending on tokenization and language, but typically a sample (sequence) is a few hundred bytes.
What is the total size of the whole dataset?	Not specified, but with up to 9 trillion tokens, the dataset size is likely multiple terabytes.
What are the designed uses for this model?	Designed uses include commercial and research applications in multilingual chat, agentic retrieval, summarization, writing assistants, and prompt rewriting.
How many epochs have been used in the finetuning?	Number of epochs is not specified; several rounds of SFT, RS, and DPO were performed in post-training.
How many model parameters (weights) does the model have?	Llama 3.2 1B has 1.23 billion parameters; Llama 3.2 3B has 3.21 billion parameters.
What is the science domain of the model?	The model is in the domain of natural language processing (NLP).
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves generative language modeling tasks, including text generation, summarization, rewriting, and instruction following.
What is the intended use of this model?	Intended use is for commercial and research applications in multilingual dialogue, agentic retrieval, summarization, and writing assistance.
What is the size of the final model in Mb?	The Llama 3.2 3B BF16 model is 6,129 MB; the 1B BF16 model is 2,358 MB. Quantized versions are smaller (e.g., 1B SpinQuant is 1,083 MB).
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Supervised fine-tuning (SFT), rejection sampling (RS), direct preference optimization (DPO), quantization-aware training (QAT), and LoRA adaptation were used.
What is the claimed performance of this model?	On MMLU (5-shot), Llama 3.2 3B achieves 63.4% accuracy (instruction-tuned, bf16); on GSM8K (CoT), 77.7%; on MGSM (CoT), 58.2%.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, instruction-tuned models outperform base pretrained models on benchmarks such as MMLU, GSM8K, and MGSM.