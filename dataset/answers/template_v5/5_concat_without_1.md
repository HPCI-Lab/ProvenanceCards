How many activities are present in the whole workflow?	There are three activities in the workflow: DataPreparation, ModelFinetuning, and ModelEvaluation.
What is the final status of the workflow?	The final status of the workflow is "Completed".
What is the time to completion of the workflow?	The workflow started at 2024-05-09T14:10:00Z and ended at 2024-05-09T17:43:28Z, for a total duration of 3 hours, 33 minutes, and 28 seconds.
List all the parameters of the first activity of the workflow	The first activity, DataPreparation, uses the following parameters: input dataset cybersectony/PhishingEmailDetectionv2.0 (raw), 200,000 entries, two columns: content (string) and label (integer 0–3), format: Parquet, language: English. Output: split into train (120,000), validation (20,000), test (60,000).
What hardware was used in the workflow?	The workflow used 1× NVIDIA T4-16GB GPU, Intel Xeon Platinum 8259CL CPU, and 32 GB RAM, running on Ubuntu 22.04.3 LTS in an AWS EC2 g4dn.2xlarge instance.
Who is responsible for this workflow (person or username or entity)?	The responsible user is "cybersectony".
What was the specific execution order of the tasks?	The execution order is: 1. DataPreparation, 2. ModelFinetuning, 3. ModelEvaluation.
List all parameters for all activites in the workflow	DataPreparation: input dataset (cybersectony/PhishingEmailDetectionv2.0 raw), output split (train/validation/test). ModelFinetuning: base model (distilbert/distilbert-base-uncased), training data (train split), epochs=3, max_length=512, truncation=True. ModelEvaluation: fine-tuned model, validation/test split.
What was the peak RAM consumption during the workflow?	Peak RAM usage was 18.4 GB (tokenised dataset fully cached in memory plus DataLoader workers buffer).
Has the model been trained in a distributed setting?	No, the model was trained on a single machine (1 GPU, 1 host), not in a distributed setting.
What was the total power consumption in Watts of the GPU(s) during the workflow?	The cards do not provide information about the total power consumption in Watts of the GPU(s) during the workflow.
What significant input artifacts are involved in the generation of the finetuned model?	The significant input artifacts are: distilbert/distilbert-base-uncased (pretrained model weights, ~67M parameters) and cybersectony/PhishingEmailDetectionv2.0 (dataset, 200,000 entries, Parquet format).
What is the total energy use for completing the workflow?	The cards do not provide information about the total energy use for completing the workflow.
List all input files with size larger than 100Mb	None of the input files are larger than 100 MB; the largest input is the dataset at ~67.2 MB and the base model at ~67 MB.
List all different file types used as input	Input file types are Parquet (dataset) and PyTorch model weights (base model).
Identify the largest output	The largest output is the tokenised dataset cache at ~4 GB, but the main output artifact is the fine-tuned model checkpoint at ~260 MB.
What is the science domain of the dataset?	The dataset is in the cybersecurity domain, specifically phishing detection.
Does the dataset have a predetermined train-test split?	Yes, the dataset is split into train (120,000), validation (20,000), and test (60,000) sets.
How many samples are present in the whole dataset?	The dataset contains 200,000 samples in total.
What is the data type of the ground truth (if present)?	The ground truth is an integer label (0–3) indicating the class (legitimate_email, phishing_email, legitimate_url, phishing_url).
What is the specific task for which the dataset was created?	The dataset was created for 4-class phishing detection (legitimate email, phishing email, legitimate URL, phishing URL).
What is the size in byte of one sample?	With a total dataset size of ~67.2 MB for 200,000 samples, one sample is approximately 336 bytes.
What is the total size of the whole dataset?	The total size of the dataset is approximately 67.2 MB.
What are the designed uses for this model?	The model is designed for multilabel classification of emails and URLs as safe or potentially phishing (phishing detection).
How many epochs have been used in the finetuning?	The model was fine-tuned for 3 epochs.
How many model parameters (weights) does the model have?	The model has approximately 67 million parameters.
What is the science domain of the model?	The model is in the cybersecurity domain, specifically phishing detection.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves a classification task (4-class sequence classification).
What is the intended use of this model?	The intended use is to classify emails and URLs as legitimate or phishing for security applications.
What is the size of the final model in Mb?	The fine-tuned model checkpoint is approximately 260 MB.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using the Hugging Face Trainer API (standard supervised fine-tuning).
What is the claimed performance of this model?	The model achieves 99.58% accuracy, 99.579% F1-score, 99.583% precision, and 99.58% recall on the evaluation set.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the fine-tuned model achieves high accuracy (99.58%) on phishing detection, which is a downstream task not present in the pretrained version. The pretrained model's GLUE scores are lower for general tasks.