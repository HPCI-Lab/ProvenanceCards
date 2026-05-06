How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	Not specified in the cards ("~")
List all the parameters of the first activity of the workflow	Inputs: HealthCareMagic-100k (100,000 real patient–doctor conversations, instruction/input/output JSON triples), iCliniq-10k (10,000 real patient–doctor conversations, instruction/input/output JSON triples); Output: avaliev/chat_doctor (merged, deduplicated instruction-tuning dataset of 110,000 examples)
What hardware was used in the workflow?	Base model pretraining used H100-80GB GPU cluster (Meta's production infrastructure); fine-tuning hardware not specified.
Who is responsible for this workflow (person or username or entity)?	prithivMLmods (as model publisher on HuggingFace); dataset by avaliev; base model by Meta.
What was the specific execution order of the tasks?	1. DataPreparation 2. ModelFinetuning 3. ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: Inputs: HealthCareMagic-100k, iCliniq-10k; Output: avaliev/chat_doctor. ModelFinetuning: Inputs: meta-llama/Llama-3.2-3B-Instruct, avaliev/chat_doctor; Output: Llama-Doctor-3.2-3B-Instruct. ModelEvaluation: Input: Llama-Doctor-3.2-3B-Instruct; Output: evaluation_report.
What was the peak RAM consumption during the workflow?	Not specified in the cards ("~")
Has the model been trained in a distributed setting?	Base model pretraining used Meta's custom built GPU cluster (distributed); fine-tuning distribution not specified.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Base model pretraining: 700W per H100-80GB GPU; fine-tuning power not specified.
What significant input artifacts are involved in the generation of the finetuned model?	meta-llama/Llama-3.2-3B-Instruct (pretrained base model, 3.21B parameters, BF16 safetensors, ~6.43 GB); avaliev/chat_doctor (110,000-example instruction-tuning dataset, JSON)
What is the total energy use for completing the workflow?	Not specified for fine-tuning; base model pretraining: 833k GPU hours, 240 tons CO2eq (location-based), 0 tons CO2eq (market-based)
List all input files with size larger than 100Mb	meta-llama/Llama-3.2-3B-Instruct (~6.43 GB, BF16 safetensors)
List all different file types used as input	JSON (instruction/input/output triples), safetensors (PyTorch model weights)
Identify the largest output	Llama-Doctor-3.2-3B-Instruct (fine-tuned model weights; BF16 safetensors, ~6.43 GB)
What is the science domain of the dataset?	Medical / Healthcare
Does the dataset have a predetermined train-test split?	No explicit train-test split is mentioned; the dataset is used as a single instruction-tuning set.
How many samples are present in the whole dataset?	110,000 (100,000 HealthCareMagic + 10,000 iCliniq)
What is the data type of the ground truth (if present)?	Text (doctor's response to patient query)
What is the specific task for which the dataset was created?	Instruction-following medical question answering (conversational medical QA)
What is the size in byte of one sample?	Not specified; but each sample is a JSON triple (instruction/input/output), likely a few KB.
What is the total size of the whole dataset?	Not specified; but 110,000 samples of text, likely several hundred MB.
What are the designed uses for this model?	Medical conversational QA, chatbot, medical consultation, and content-generation applications.
How many epochs have been used in the finetuning?	Not specified in the cards.
How many model parameters (weights) does the model have?	3.21 billion parameters
What is the science domain of the model?	Medical / Healthcare
What is the task solved by this model (regression or classification or forecast etc.)?	Instruction-following text generation (conversational QA; generative)
What is the intended use of this model?	Medical dialogue assistant, chatbot, patient query answering, medical advisory applications.
What is the size of the final model in Mb?	~6,430 MB (6.43 GB)
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Supervised fine-tuning (SFT) on instruction-tuning dataset
What is the claimed performance of this model?	Qualitative assessment of instruction-following and medical response quality; quantitative benchmark results not published.
Are the performance shown in the pretrained version improved in the finetuning?	Not specified; only qualitative evaluation is mentioned for the fine-tuned model.