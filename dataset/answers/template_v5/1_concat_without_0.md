How many activities are present in the whole workflow?	The workflow contains 3 activities: DataPreparation, ModelFinetuning, and ModelEvaluation.
What is the final status of the workflow?	The final status of the workflow is "Completed".
What is the time to completion of the workflow?	The workflow took 18 hours, 32 minutes, and 47 seconds to complete.
List all the parameters of the first activity of the workflow	The first activity, DataPreparation, has the following parameters: name: DataPreparation; task_count: 1; started_at: 2024-03-12T08:14:22Z; ended_at: 2024-03-12T09:02:55Z; duration: 48m 33s; status: success: 1; hosts: ip-10-0-1-44.ec2.internal; inputs: HealthCareMagic-100k, iCliniq-10k; outputs: avaliev/chat_doctor.
What hardware was used in the workflow?	The workflow used 8× NVIDIA A100-SXM4-80GB GPUs (NVLink), Intel Xeon Platinum 8375C CPU, and 1.1 TB RAM, running on AWS EC2 p4d.24xlarge.
Who is responsible for this workflow (person or username or entity)?	The workflow was executed by the user "prithivMLmods".
What was the specific execution order of the tasks?	The execution order was: 1. DataPreparation, 2. ModelFinetuning, 3. ModelEvaluation.
List all parameters for all activites in the workflow	DataPreparation: name, task_count, started_at, ended_at, duration, status, hosts, inputs (HealthCareMagic-100k, iCliniq-10k), outputs (avaliev/chat_doctor). ModelFinetuning: name, task_count, started_at, ended_at, duration, status, hosts, inputs (meta-llama/Llama-3.2-3B-Instruct, avaliev/chat_doctor), outputs (Llama-Doctor-3.2-3B-Instruct). ModelEvaluation: name, task_count, started_at, ended_at, duration, status, hosts, inputs (Llama-Doctor-3.2-3B-Instruct), outputs (evaluation_report).
What was the peak RAM consumption during the workflow?	The peak RAM usage during the workflow was 187 GB.
Has the model been trained in a distributed setting?	Yes, the model was trained in a distributed setting, with model sharding across 8 GPUs.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Each GPU (NVIDIA A100-SXM4-80GB) has a TDP of 700W; with 8 GPUs, the total power consumption is 5600W during training.
What significant input artifacts are involved in the generation of the finetuned model?	The significant input artifacts are: meta-llama/Llama-3.2-3B-Instruct (pretrained model weights) and avaliev/chat_doctor (medical instruction-tuning dataset).
What is the total energy use for completing the workflow?	The total energy use for the workflow is not explicitly stated for the fine-tuning run; only pretraining energy use is detailed in the card.
List all input files with size larger than 100Mb	The input files larger than 100MB are: meta-llama/Llama-3.2-3B-Instruct (~6.43 GB) and avaliev/chat_doctor (dataset, ~14 GB cache).
List all different file types used as input	The input file types are: JSON (instruction/input/output triples), safetensors (model weights), and GGUF (model variant).
Identify the largest output	The largest output is Llama-Doctor-3.2-3B-Instruct, with a size of approximately 6.43 GB (BF16 safetensors, two shards).
What is the science domain of the dataset?	The science domain of the dataset is medical/healthcare.
Does the dataset have a predetermined train-test split?	The dataset does not have a predetermined train-test split; it is a merged, deduplicated instruction-tuning dataset.
How many samples are present in the whole dataset?	The dataset contains 110,000 samples (100,000 from HealthCareMagic and 10,000 from iCliniq).
What is the data type of the ground truth (if present)?	The ground truth data type is text (doctor's response in the output field).
What is the specific task for which the dataset was created?	The dataset was created for supervised fine-tuning of conversational medical question-answering models.
What is the size in byte of one sample?	Assuming 14 GB for 110,000 samples, one sample is approximately 130 KB (14,000,000 KB / 110,000).
What is the total size of the whole dataset?	The total size of the dataset is approximately 14 GB (as dataset cache).
What are the designed uses for this model?	The model is designed for chatbot, medical consultation, conversational QA, and content-generation applications in the medical domain.
How many epochs have been used in the finetuning?	The number of epochs used in fine-tuning is not specified in the provided cards.
How many model parameters (weights) does the model have?	The model has 3.21 billion parameters.
What is the science domain of the model?	The science domain of the model is medical/healthcare.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves a question-answering (QA) task, specifically conversational medical QA.
What is the intended use of this model?	The intended use is for commercial and research applications in multilingual conversational AI, especially medical chatbots and advisory systems.
What is the size of the final model in Mb?	The final model size is approximately 6,430 MB (6.43 GB).
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using supervised fine-tuning (SFT) on instruction-tuning data.
What is the claimed performance of this model?	The workflow card does not publish quantitative benchmark results for the fine-tuned model; only a qualitative assessment is mentioned.
Are the performance shown in the pretrained version improved in the finetuning?	The workflow card does not provide quantitative evidence of performance improvement after fine-tuning; only qualitative evaluation is reported.