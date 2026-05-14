How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	18h 32m 47s
List all the parameters of the first activity of the workflow	Inputs: HealthCareMagic-100k (100,000 real patient–doctor conversations, instruction/input/output JSON triples), iCliniq-10k (10,000 real patient–doctor conversations, instruction/input/output JSON triples); Output: avaliev/chat_doctor (merged, deduplicated instruction-tuning dataset of 110,000 examples)
What hardware was used in the workflow?	8× NVIDIA A100-SXM4-80GB (NVLink), Intel Xeon Platinum 8375C, 1.1 TB RAM
Who is responsible for this workflow (person or username or entity)?	prithivMLmods
What was the specific execution order of the tasks?	1. DataPreparation 2. ModelFinetuning 3. ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: Inputs: HealthCareMagic-100k, iCliniq-10k; Output: avaliev/chat_doctor. ModelFinetuning: Inputs: meta-llama/Llama-3.2-3B-Instruct, avaliev/chat_doctor; Output: Llama-Doctor-3.2-3B-Instruct. ModelEvaluation: Input: Llama-Doctor-3.2-3B-Instruct; Output: evaluation_report.
What was the peak RAM consumption during the workflow?	187 GB
Has the model been trained in a distributed setting?	Yes, model sharding across 8 GPUs was used during training.
What was the total power consumption in Watts of the GPU(s) during the workflow?	700 W per GPU (8 GPUs used)
What significant input artifacts are involved in the generation of the finetuned model?	meta-llama/Llama-3.2-3B-Instruct (pretrained base model), avaliev/chat_doctor (medical instruction-tuning dataset)
What is the total energy use for completing the workflow?	Not specified for the workflow; for Llama 3.2 3B pretraining, 460k GPU hours at 700W per GPU, but fine-tuning energy use is not explicitly stated.
List all input files with size larger than 100Mb	tokenizer.json (17.2 MB), pytorch_model-00001-of-00002.bin (4.97 GB), pytorch_model-00002-of-00002.bin (1.46 GB)
List all different file types used as input	JSON, BIN, MD, GITATTRIBUTES, SAFETENSORS
Identify the largest output	Llama-Doctor-3.2-3B-Instruct model weights (BF16 safetensors, two shards: 4.97 GB + 1.46 GB)
What is the science domain of the dataset?	Medical
Does the dataset have a predetermined train-test split?	No, the dataset is merged and deduplicated for instruction tuning; no explicit train-test split is mentioned.
How many samples are present in the whole dataset?	110,000
What is the data type of the ground truth (if present)?	Text (output: doctor’s response)
What is the specific task for which the dataset was created?	Medical conversational question answering (instruction-following)
What is the size in byte of one sample?	Not explicitly stated; sample shown is a JSON object with instruction, input, and output fields, typically a few KB.
What is the total size of the whole dataset?	Not explicitly stated; dataset size is not given, but 110,000 samples of text-based JSON triples.
What are the designed uses for this model?	Conversational AI, medical consultation tools, content creation, problem-solving assistants
How many epochs have been used in the finetuning?	Not specified
How many model parameters (weights) does the model have?	3.21 billion
What is the science domain of the model?	Medical (specialized for medical conversational QA)
What is the task solved by this model (regression or classification or forecast etc.)?	Text generation (instruction-following, conversational question answering)
What is the intended use of this model?	Commercial and research use in multilingual conversational AI, medical QA, agentic applications
What is the size of the final model in Mb?	6.43 GB (6430 MB)
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Supervised fine-tuning (SFT)
What is the claimed performance of this model?	Qualitative assessment of instruction-following and medical response quality; quantitative benchmark results not published for the fine-tuned version
Are the performance shown in the pretrained version improved in the finetuning?	Not explicitly stated; qualitative assessment indicates improved instruction-following and medical response quality, but quantitative benchmarks are not published for the fine-tuned model