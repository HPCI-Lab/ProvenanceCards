How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	Not specified in the card ("duration: ~")
List all the parameters of the first activity of the workflow	Inputs: HealthCareMagic-100k (100,000 real patient–doctor conversations, instruction/input/output JSON triples), iCliniq-10k (10,000 real patient–doctor conversations, instruction/input/output JSON triples); Output: avaliev/chat_doctor (merged, deduplicated instruction-tuning dataset of 110,000 examples)
What hardware was used in the workflow?	H100-80GB GPU cluster (Meta's production infrastructure for base model pretraining; fine-tuning hardware not specified)
Who is responsible for this workflow (person or username or entity)?	Meta (for base model); fine-tuning user/entity not specified
What was the specific execution order of the tasks?	1. DataPreparation 2. ModelFinetuning 3. ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: Inputs: HealthCareMagic-100k, iCliniq-10k; Output: avaliev/chat_doctor. ModelFinetuning: Inputs: meta-llama/Llama-3.2-3B-Instruct, avaliev/chat_doctor; Output: Llama-Doctor-3.2-3B-Instruct. ModelEvaluation: Input: Llama-Doctor-3.2-3B-Instruct; Output: evaluation_report.
What was the peak RAM consumption during the workflow?	Not specified in the workflow card
Has the model been trained in a distributed setting?	Yes, base model pretraining used Meta's custom GPU cluster; fine-tuning hardware not specified
What was the total power consumption in Watts of the GPU(s) during the workflow?	700W per GPU for base model pretraining; fine-tuning power not specified
What significant input artifacts are involved in the generation of the finetuned model?	meta-llama/Llama-3.2-3B-Instruct (pretrained model), avaliev/chat_doctor (medical instruction-tuning dataset)
What is the total energy use for completing the workflow?	Not specified for fine-tuning; base model pretraining: 460k GPU hours (3B), 133 tons CO2eq, 700W per GPU
List all input files with size larger than 100Mb	meta-llama/Llama-3.2-3B-Instruct (model weights, ~6.43 GB), tokenizer.json (17.2 MB, below threshold), avaliev/chat_doctor (dataset, size not specified but likely >100MB)
List all different file types used as input	JSON (instruction/input/output triples), safetensors (model weights), GGUF (model variant)
Identify the largest output	Llama-Doctor-3.2-3B-Instruct (fine-tuned model weights, ~6.43 GB)
What is the science domain of the dataset?	Medical/Healthcare
Does the dataset have a predetermined train-test split?	No explicit train-test split; merged dataset for instruction tuning
How many samples are present in the whole dataset?	110,000 (100k HealthCareMagic + 10k iCliniq)
What is the data type of the ground truth (if present)?	Text (doctor responses in instruction/output format)
What is the specific task for which the dataset was created?	Medical conversational QA (instruction-following, patient–doctor dialogue)
What is the size in byte of one sample?	Not specified; typical JSON triple (instruction/input/output) likely several KB
What is the total size of the whole dataset?	Not specified; likely >100MB given 110,000 samples
What are the designed uses for this model?	Chatbots for medical consultation, medical QA, advisory responses, content generation in medical context
How many epochs have been used in the finetuning?	Not specified in the workflow card
How many model parameters (weights) does the model have?	3.21 billion (3B)
What is the science domain of the model?	Medical/Healthcare (via fine-tuning)
What is the task solved by this model (regression or classification or forecast etc.)?	Text generation (instruction-following, conversational QA)
What is the intended use of this model?	Medical conversational QA, chatbot, advisory, content generation
What is the size of the final model in Mb?	~6,430 MB (6.43 GB)
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Supervised fine-tuning (SFT) on instruction-tuning dataset
What is the claimed performance of this model?	Qualitative assessment of instruction-following and medical response quality; quantitative benchmark results not published
Are the performance shown in the pretrained version improved in the finetuning?	Not quantitatively reported; qualitative improvement for medical conversational QA claimed