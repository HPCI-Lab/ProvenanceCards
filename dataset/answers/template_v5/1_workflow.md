How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	~
List all the parameters of the first activity of the workflow	Inputs: HealthCareMagic-100k (100,000 real patient–doctor conversations, instruction/input/output JSON triples), iCliniq-10k (10,000 real patient–doctor conversations, instruction/input/output JSON triples); Output: avaliev/chat_doctor (merged, deduplicated instruction-tuning dataset of 110,000 examples)
What hardware was used in the workflow?	Training utilised H100-80GB GPU cluster (Meta's production infrastructure for the base model pretraining; fine-tuning hardware not specified)
Who is responsible for this workflow (person or username or entity)?	~
What was the specific execution order of the tasks?	1. DataPreparation 2. ModelFinetuning 3. ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: Inputs: HealthCareMagic-100k, iCliniq-10k; Output: avaliev/chat_doctor. ModelFinetuning: Inputs: meta-llama/Llama-3.2-3B-Instruct, avaliev/chat_doctor; Output: Llama-Doctor-3.2-3B-Instruct. ModelEvaluation: Input: Llama-Doctor-3.2-3B-Instruct; Output: evaluation_report.
What was the peak RAM consumption during the workflow?	~
Has the model been trained in a distributed setting?	Not specified for fine-tuning; base model pretraining used Meta's production infrastructure, likely distributed.
What was the total power consumption in Watts of the GPU(s) during the workflow?	~
What significant input artifacts are involved in the generation of the finetuned model?	meta-llama/Llama-3.2-3B-Instruct (pretrained base model), avaliev/chat_doctor (medical instruction-tuning dataset)
What is the total energy use for completing the workflow?	~
List all input files with size larger than 100Mb	meta-llama/Llama-3.2-3B-Instruct (~6.43 GB, safetensors model weights)
List all different file types used as input	HuggingFace dataset (instruction-following JSON), safetensors model weights (PyTorch)
Identify the largest output	Llama-Doctor-3.2-3B-Instruct (fine-tuned model weights; ~6.43 GB)
What is the science domain of the dataset?	Medical/Healthcare
Does the dataset have a predetermined train-test split?	Not specified; dataset is merged and deduplicated for instruction-tuning
How many samples are present in the whole dataset?	110,000
What is the data type of the ground truth (if present)?	Doctor responses (text, output field in instruction/input/output JSON triples)
What is the specific task for which the dataset was created?	Medical conversational QA, chatbot, and advisory applications (instruction-following)
What is the size in byte of one sample?	Not specified
What is the total size of the whole dataset?	Not specified
What are the designed uses for this model?	Chatbot, medical consultation, and content-generation applications
How many epochs have been used in the finetuning?	Not specified
How many model parameters (weights) does the model have?	3.21B parameters
What is the science domain of the model?	Medical/Healthcare
What is the task solved by this model (regression or classification or forecast etc.)?	Conversational question answering (QA), instruction-following (text generation)
What is the intended use of this model?	Medical conversational QA, chatbot, advisory, and content-generation applications
What is the size of the final model in Mb?	~6,430 MB
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Supervised fine-tuning (SFT)
What is the claimed performance of this model?	Qualitative assessment of instruction-following and medical response quality; quantitative benchmark results not published
Are the performance shown in the pretrained version improved in the finetuning?	Not specified; only qualitative assessment provided, no quantitative comparison