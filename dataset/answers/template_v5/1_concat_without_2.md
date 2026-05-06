How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	Not specified
List all the parameters of the first activity of the workflow	Inputs: HealthCareMagic-100k (100,000 real patient–doctor conversations), iCliniq-10k (10,000 real patient–doctor conversations); Outputs: avaliev/chat_doctor (merged, deduplicated instruction-tuning dataset of 110,000 examples)
What hardware was used in the workflow?	H100-80GB GPU cluster was used for training (fine-tuning hardware not specified)
Who is responsible for this workflow (person or username or entity)?	Not specified
What was the specific execution order of the tasks?	1. DataPreparation 2. ModelFinetuning 3. ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: Inputs: HealthCareMagic-100k, iCliniq-10k; Output: avaliev/chat_doctor. ModelFinetuning: Inputs: meta-llama/Llama-3.2-3B-Instruct, avaliev/chat_doctor; Output: Llama-Doctor-3.2-3B-Instruct. ModelEvaluation: Input: Llama-Doctor-3.2-3B-Instruct; Output: evaluation_report.
What was the peak RAM consumption during the workflow?	Not specified
Has the model been trained in a distributed setting?	Not specified
What was the total power consumption in Watts of the GPU(s) during the workflow?	Not specified
What significant input artifacts are involved in the generation of the finetuned model?	meta-llama/Llama-3.2-3B-Instruct (pretrained base model), avaliev/chat_doctor (medical instruction-tuning dataset)
What is the total energy use for completing the workflow?	Not specified
List all input files with size larger than 100Mb	tokenizer.json (17.2 MB; does not exceed 100MB), model files: pytorch_model-00001-of-00002.bin (4.97 GB), pytorch_model-00002-of-00002.bin (1.46 GB)
List all different file types used as input	JSON (.json), binary model files (.bin), markdown (.md), Git attributes (.gitattributes)
Identify the largest output	pytorch_model-00001-of-00002.bin (4.97 GB)
What is the science domain of the dataset?	Medical
Does the dataset have a predetermined train-test split?	No, only merged and deduplicated for fine-tuning; train-test split not specified
How many samples are present in the whole dataset?	110,000
What is the data type of the ground truth (if present)?	Text (doctor's response)
What is the specific task for which the dataset was created?	Medical conversational question-answering (instruction-following)
What is the size in byte of one sample?	Not specified
What is the total size of the whole dataset?	Not specified
What are the designed uses for this model?	Chatbots for customer support or virtual assistants, medical consultation tools, content creation tools, problem-solving assistants
How many epochs have been used in the finetuning?	Not specified
How many model parameters (weights) does the model have?	3.21 billion
What is the science domain of the model?	Medical
What is the task solved by this model (regression or classification or forecast etc.)?	Question-answering (instruction-following, conversational text generation)
What is the intended use of this model?	Medical conversational QA, chatbot, advisory, content-generation applications
What is the size of the final model in Mb?	6.43 GB (6430 MB)
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Supervised fine-tuning (SFT)
What is the claimed performance of this model?	Qualitative assessment of instruction-following and medical response quality; quantitative benchmark results not published
Are the performance shown in the pretrained version improved in the finetuning?	Not specified