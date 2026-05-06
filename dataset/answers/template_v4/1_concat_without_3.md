How many activities are present in the whole workflow?	answer not found
What is the final status of the workflow?	answer not found
What is the time to completion of the workflow?	answer not found
List all the parameters of the first activity of the workflow	answer not found
What hardware was used in the workflow?	Meta's custom built GPU cluster, H100-80GB GPUs
Who is responsible for this workflow (person or username or entity)?	Meta
What was the specific execution order of the tasks?	answer not found
List all the parameters for the whole workflow process	answer not found
What was the peak RAM consumption during the workflow?	7,419 MB (for 3B BF16 baseline, as per inference table)
Has the model been trained in a distributed setting?	answer not found
What was the real-time power consumption (in Watts) of the GPU during the workflow?	700 W
Which inputs influenced the output in the workflow?	Publicly available online data, avaliev/chat_doctor dataset, Llama 3.1 8B and 70B logits
What is the total energy use for completing the workflow?	916,000 GPU hours (training), 240 tons CO2eq (location-based greenhouse gas emissions)
List all input files with size larger than 100Mb	tokenizer.json (17.2 MB), pytorch_model-00001-of-00002.bin (4.97 GB), pytorch_model-00002-of-00002.bin (1.46 GB) [Note: Only .bin files >100MB]
List all different file types used as input	.gitattributes, .md, .json, .bin
Identify the largest output	pytorch_model-00001-of-00002.bin (4.97 GB)
What is the science domain of the dataset?	Medical
Does the dataset have a predetermined train-test split?	answer not found
How many samples are present in the whole dataset?	110,000 (100k + 10k real conversations)
What is the data type of the ground truth (if present)?	Text (doctor's response)
What is the specific task for which the dataset was created?	Medical question-answering (conversational AI)
What is the size in byte of one sample?	answer not found
What is the total size of the whole dataset?	answer not found
What are the designed uses for this model?	Conversational AI, Text Generation, Instruction Following, Chatbots, Medical Consultation Tools, Content Creation, Problem-solving Assistants
How many epochs have been used in the final training?	answer not found
How many model parameters (weights) does the model have?	3.21 billion (3B)
What is the science domain of the model?	Medical, Multilingual Text Generation
What is the task solved by this model (regression or classification or forecast etc.)?	Text generation, question-answering, instruction following
What is the intended use of this model?	Commercial and research use in multiple languages, assistant-like chat, agentic applications, knowledge retrieval, summarization, mobile AI powered writing assistants, query and prompt rewriting
What is the size of the final model in Mb?	4.97 GB + 1.46 GB = 6.43 GB (6,430 MB)
What technique was used to train the model?	Supervised Fine-Tuning (SFT), Reinforcement Learning with Human Feedback (RLHF), Knowledge Distillation, Rejection Sampling, Direct Preference Optimization (DPO), Quantization (SpinQuant, QLoRA)
What is the claimed performance of this model?	63.4 MMLU (3B bf16), 77.7 GSM8K (CoT), 78.6 ARC-C, 69.8 Hellaswag, 77.4 IFEval, 19.0 TLDR9+ (test)
Are the performance shown in the pretrained version improved in the finetuning?	answer not found