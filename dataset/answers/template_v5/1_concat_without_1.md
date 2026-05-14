How many activities are present in the whole workflow?	There are multiple activities in the workflow, including pretraining, supervised fine-tuning (SFT), reinforcement learning with human feedback (RLHF), quantization, and evaluation. The workflow also includes dataset preparation and model deployment steps.
What is the final status of the workflow?	The final status of the workflow is a static, released model, Llama-Doctor-3.2-3B-Instruct, trained and fine-tuned, available for deployment and use.
What is the time to completion of the workflow?	The total training time for the Llama 3.2 3B model was 460,000 GPU hours, with additional time for fine-tuning, quantization, and evaluation, but the exact end-to-end workflow duration is not specified.
List all the parameters of the first activity of the workflow	The first activity, pretraining, involves parameters such as model size (3.21B parameters), training data (up to 9T tokens), input modality (multilingual text), output modality (text and code), context length (128k), and use of Grouped-Query Attention (GQA).
What hardware was used in the workflow?	The workflow used Meta's custom built GPU cluster, specifically H100-80GB GPUs with a TDP of 700W.
Who is responsible for this workflow (person or username or entity)?	The workflow is managed and executed by Meta Platforms, Inc. and Meta Platforms Ireland Limited.
What was the specific execution order of the tasks?	The execution order is: dataset preparation → pretraining (with knowledge distillation) → supervised fine-tuning (SFT) → reinforcement learning with human feedback (RLHF) → quantization (SpinQuant, QLoRA) → evaluation → model release.
List all parameters for all activites in the workflow	Parameters include: model size (3.21B), training data (up to 9T tokens), context length (128k), GQA, quantization scheme (4-bit groupwise, 8-bit per-channel), hardware (H100-80GB GPUs), training time (460k GPU hours), power consumption (700W per GPU), dataset sources, and evaluation benchmarks.
What was the peak RAM consumption during the workflow?	Peak RAM consumption for inference on the 3B model was 7,419 MB (resident set size) in BF16 baseline, and 3,726 MB for SpinQuant quantized model.
Has the model been trained in a distributed setting?	Yes, the model was trained in a distributed setting using Meta's custom GPU cluster infrastructure.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Each GPU used had a power consumption of 700W; total power consumption depends on the number of GPUs and training hours, but per device is 700W.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts include the avaliev/chat_doctor dataset, HealthCareMagic-100k, icliniq-10k, and pretraining data (up to 9T tokens from public sources).
What is the total energy use for completing the workflow?	Estimated total location-based greenhouse gas emissions were 240 tons CO2eq for training, with net zero market-based emissions due to renewable energy use.
List all input files with size larger than 100Mb	tokenizer.json (17.2 MB), pytorch_model-00001-of-00002.bin (4.97 GB), pytorch_model-00002-of-00002.bin (1.46 GB); all are larger than 100MB.
List all different file types used as input	Files used include .json (config, tokenizer, special tokens), .bin (PyTorch model weights), and .md (README).
Identify the largest output	The largest output is the PyTorch model file pytorch_model-00001-of-00002.bin at 4.97 GB.
What is the science domain of the dataset?	The science domain of the dataset is medical/healthcare.
Does the dataset have a predetermined train-test split?	The dataset does not specify a predetermined train-test split; it is formed from real conversations and can be split as needed.
How many samples are present in the whole dataset?	The dataset contains 110,000 samples (100k from HealthCareMagic, 10k from icliniq).
What is the data type of the ground truth (if present)?	The ground truth is text, specifically doctor responses to patient queries.
What is the specific task for which the dataset was created?	The dataset was created for medical question-answering and conversational AI tasks.
What is the size in byte of one sample?	One sample is approximately 1-2 KB, based on the JSON structure of instruction, input, and output fields.
What is the total size of the whole dataset?	The total size of the dataset is estimated to be between 110 MB and 220 MB, depending on encoding and formatting.
What are the designed uses for this model?	Designed uses include conversational AI, medical consultation tools, content creation, and problem-solving assistants in instructional contexts.
How many epochs have been used in the finetuning?	The exact number of epochs used in fine-tuning is not specified in the provided cards.
How many model parameters (weights) does the model have?	The model has 3.21 billion parameters.
What is the science domain of the model?	The science domain of the model is medical/healthcare, with additional general instruction-following capabilities.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves question-answering and text generation tasks, which are classification and generative tasks.
What is the intended use of this model?	The intended use is for assistant-like chat, medical advice, knowledge retrieval, summarization, and agentic applications.
What is the size of the final model in Mb?	The final model size is approximately 6.43 GB (6,430 MB), combining both PyTorch model files.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) were used; quantization techniques include SpinQuant and QLoRA.
What is the claimed performance of this model?	The model claims improved performance in instruction following, medical question-answering, and multilingual benchmarks, outperforming many open and closed chat models on industry benchmarks.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, performance is improved in the instruction-tuned (finetuned) version compared to the pretrained base model, as shown in benchmark tables.