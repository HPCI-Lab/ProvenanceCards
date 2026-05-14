How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	18h 32m 47s
List all the parameters of the first activity of the workflow	HealthCareMagic-100k: 100,000 real patient–doctor conversations from HealthCareMagic.com; format: instruction/input/output JSON triples; iCliniq-10k: 10,000 real patient–doctor conversations from iCliniq.com; format: instruction/input/output JSON triples
What hardware was used in the workflow?	8× NVIDIA A100-SXM4-80GB (NVLink), Intel Xeon Platinum 8375C, 1.1 TB RAM
Who is responsible for this workflow (person or username or entity)?	prithivMLmods
What was the specific execution order of the tasks?	DataPreparation → ModelFinetuning → ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: HealthCareMagic-100k, iCliniq-10k; ModelFinetuning: meta-llama/Llama-3.2-3B-Instruct, avaliev/chat_doctor; ModelEvaluation: Llama-Doctor-3.2-3B-Instruct
What was the peak RAM consumption during the workflow?	187 GB
Has the model been trained in a distributed setting?	Yes, model sharding across 8 GPUs was used during training.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Not specified in the cards.
What significant input artifacts are involved in the generation of the finetuned model?	meta-llama/Llama-3.2-3B-Instruct (pretrained base model), avaliev/chat_doctor (medical instruction-tuning dataset)
What is the total energy use for completing the workflow?	Not specified in the cards.
List all input files with size larger than 100Mb	tokenizer.json (17.2 MB, not >100MB); pytorch_model-00001-of-00002.bin (4.97 GB); pytorch_model-00002-of-00002.bin (1.46 GB)
List all different file types used as input	JSON, safetensors, bin, GGUF
Identify the largest output	Llama-Doctor-3.2-3B-Instruct model weights: pytorch_model-00001-of-00002.bin (4.97 GB)
What is the science domain of the dataset?	Medical
Does the dataset have a predetermined train-test split?	No, only merged and deduplicated for supervised fine-tuning; no explicit train-test split mentioned.
How many samples are present in the whole dataset?	110,000
What is the data type of the ground truth (if present)?	Text (output: doctor’s answer)
What is the specific task for which the dataset was created?	Medical question-answering in a conversational, instruction-following style
What is the size in byte of one sample?	Not specified; typical JSON triple (instruction/input/output) likely ~1–2 KB
What is the total size of the whole dataset?	~14 GB dataset cache (as per resource usage)
What are the designed uses for this model?	Chatbots for customer support or virtual assistants; medical consultation tools; content creation; problem-solving assistants in instructional contexts
How many epochs have been used in the finetuning?	Not specified in the cards.
How many model parameters (weights) does the model have?	3.21 billion
What is the science domain of the model?	Medical
What is the task solved by this model (regression or classification or forecast etc.)?	Question-answering (text generation)
What is the intended use of this model?	Medical conversational QA, chatbot, advisory, and content-generation applications
What is the size of the final model in Mb?	6.43 GB = 6430 MB
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Supervised fine-tuning (SFT)
What is the claimed performance of this model?	Qualitative assessment of instruction-following and medical response quality; quantitative benchmark results not published
Are the performance shown in the pretrained version improved in the finetuning?	Qualitative assessment suggests improved instruction-following and medical response quality, but no quantitative benchmarks are published.