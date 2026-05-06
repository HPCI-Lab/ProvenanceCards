How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	Not specified in the cards ("~" for started_at, ended_at, duration)
List all the parameters of the first activity of the workflow	Inputs: HealthCareMagic-100k (100,000 real patient–doctor conversations, instruction/input/output JSON triples), iCliniq-10k (10,000 real patient–doctor conversations, instruction/input/output JSON triples); Output: avaliev/chat_doctor (merged, deduplicated instruction-tuning dataset of 110,000 examples)
What hardware was used in the workflow?	H100-80GB GPU cluster (Meta's production infrastructure for base model pretraining; fine-tuning hardware not specified)
Who is responsible for this workflow (person or username or entity)?	Not specified; user field is "~"; model developer is Meta; entrypoint.repository is https://huggingface.co/prithivMLmods/Llama-Doctor-3.2-3B-Instruct
What was the specific execution order of the tasks?	1. DataPreparation 2. ModelFinetuning 3. ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: Inputs: HealthCareMagic-100k, iCliniq-10k; Output: avaliev/chat_doctor. ModelFinetuning: Inputs: meta-llama/Llama-3.2-3B-Instruct, avaliev/chat_doctor; Output: Llama-Doctor-3.2-3B-Instruct. ModelEvaluation: Input: Llama-Doctor-3.2-3B-Instruct; Output: evaluation_report
What was the peak RAM consumption during the workflow?	Not specified in the cards ("~" for memory)
Has the model been trained in a distributed setting?	Yes, base model pretraining used Meta's custom built GPU cluster; fine-tuning hardware not specified
What was the total power consumption in Watts of the GPU(s) during the workflow?	700W per H100-80GB GPU (for pretraining); fine-tuning power consumption not specified
What significant input artifacts are involved in the generation of the finetuned model?	meta-llama/Llama-3.2-3B-Instruct (pretrained base model), avaliev/chat_doctor (medical instruction-tuning dataset)
What is the total energy use for completing the workflow?	Not specified for fine-tuning; pretraining used 460k GPU hours for 3B model, but fine-tuning energy use not given
List all input files with size larger than 100Mb	tokenizer.json (17.2 MB), pytorch_model-00001-of-00002.bin (4.97 GB), pytorch_model-00002-of-00002.bin (1.46 GB); avaliev/chat_doctor dataset size not specified but likely >100MB
List all different file types used as input	JSON (instruction/input/output triples), safetensors (model weights), GGUF (model variant), bin (PyTorch model file), tokenizer files
Identify the largest output	Llama-Doctor-3.2-3B-Instruct (fine-tuned model weights; BF16 safetensors two shards: 4.97 GB + 1.46 GB; GGUF variant)
What is the science domain of the dataset?	Medical
Does the dataset have a predetermined train-test split?	No explicit train-test split; dataset is merged and deduplicated for instruction tuning
How many samples are present in the whole dataset?	110,000 (100k HealthCareMagic + 10k iCliniq)
What is the data type of the ground truth (if present)?	Text (doctor's response to patient query)
What is the specific task for which the dataset was created?	Medical conversational question-answering (instruction-following)
What is the size in byte of one sample?	Not specified; typical JSON triple (instruction/input/output) likely ~1-2 KB
What is the total size of the whole dataset?	Not specified; estimated >100MB (110,000 samples, each ~1-2 KB)
What are the designed uses for this model?	Conversational AI, medical consultation tools, content creation, problem-solving assistants (instructional contexts)
How many epochs have been used in the finetuning?	Not specified in the cards
How many model parameters (weights) does the model have?	3.21 billion (3B)
What is the science domain of the model?	Medical (specialised for medical conversational QA)
What is the task solved by this model (regression or classification or forecast etc.)?	Text generation (instruction-following, conversational question-answering)
What is the intended use of this model?	Chatbots, medical consultation, content generation, problem-solving assistants
What is the size of the final model in Mb?	6.43 GB (two shards: 4.97 GB + 1.46 GB) = 6,430 MB
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Supervised fine-tuning (SFT) on instruction-tuning dataset
What is the claimed performance of this model?	Qualitative assessment: improved instruction-following and medical response quality; quantitative benchmark results not published
Are the performance shown in the pretrained version improved in the finetuning?	Qualitative improvement in instruction-following and medical response quality; quantitative benchmarks not published for the fine-tuned model