How many activities are present in the whole workflow?	Not specified in the model card.
What is the final status of the workflow?	Static model trained on an offline dataset; status: released.
What is the time to completion of the workflow?	Not specified in the model card.
List all the parameters of the first activity of the workflow	Not specified in the model card.
What hardware was used in the workflow?	Meta's custom built GPU cluster; H100-80GB GPUs.
Who is responsible for this workflow (person or username or entity)?	Meta Platforms, Inc. and Meta Platforms Ireland Limited.
What was the specific execution order of the tasks?	Pretraining → Knowledge distillation → Pruning → Alignment (SFT, RS, DPO) → Quantization.
List all the parameters for the whole workflow process	Not specified in the model card.
What was the peak RAM consumption during the workflow?	Not specified in the model card.
Has the model been trained in a distributed setting?	Yes, using Meta's custom GPU cluster.
What was the real-time power consumption (in Watts) of the GPU during the workflow?	700W per GPU.
Which inputs influenced the output in the workflow?	Publicly available online data (up to 9T tokens); logits from Llama 3.1 8B and 70B models.
What is the total energy use for completing the workflow?	916,000 GPU hours.
List all input files with size larger than 100Mb	Not specified in the model card.
List all different file types used as input	Not specified in the model card.
Identify the largest output	Final model checkpoint; for 3B model, PTE file size is 6129 MB (BF16 baseline).
What is the science domain of the dataset?	General natural language (multilingual text and code).
Does the dataset have a predetermined train-test split?	Not specified in the model card.
How many samples are present in the whole dataset?	Not specified in the model card.
What is the data type of the ground truth (if present)?	Not specified in the model card.
What is the specific task for which the dataset was created?	Pretraining and instruction tuning for generative language modeling.
What is the size in byte of one sample?	Not specified in the model card.
What is the total size of the whole dataset?	Not specified in the model card.
What are the designed uses for this model?	Commercial and research use; assistant-like chat, agentic retrieval, summarization, writing assistants, prompt rewriting.
How many epochs have been used in the final training?	Not specified in the model card.
How many model parameters (weights) does the model have?	1.23B (1B model); 3.21B (3B model).
What is the science domain of the model?	General natural language processing (multilingual).
What is the task solved by this model (regression or classification or forecast etc.)?	Generative language modeling (text generation, summarization, rewriting, instruction following).
What is the intended use of this model?	Commercial and research use in multiple languages; assistant-like chat and agentic applications.
What is the size of the final model in Mb?	1B BF16: 2358 MB; 3B BF16: 6129 MB; quantized versions are smaller.
What technique was used to train the model?	Pretraining, supervised fine-tuning (SFT), reinforcement learning with human feedback (RLHF), knowledge distillation, quantization.
What is the claimed performance of this model?	Outperforms many available open source and closed chat models on common industry benchmarks; see benchmark tables for details.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, instruction-tuned models show improved performance over base pretrained models.