How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	3h 33m 28s
List all the parameters of the first activity of the workflow	inputs: cybersectony/PhishingEmailDetectionv2.0 (raw) — 200,000 entries combining email messages (22,644) and URLs (177,356); two columns: content (string) and label (integer 0–3: legitimate_email, phishing_email, legitimate_url, phishing_url); format: Parquet; language: English
What hardware was used in the workflow?	1× NVIDIA T4-16GB, Intel Xeon Platinum 8259CL, 32 GB RAM
Who is responsible for this workflow (person or username or entity)?	cybersectony
What was the specific execution order of the tasks?	1. DataPreparation 2. ModelFinetuning 3. ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: inputs: cybersectony/PhishingEmailDetectionv2.0 (raw); outputs: split dataset. ModelFinetuning: inputs: distilbert/distilbert-base-uncased, cybersectony/PhishingEmailDetectionv2.0 (train split); outputs: phishing-email-detection-distilbert_v2.4.1. ModelEvaluation: inputs: phishing-email-detection-distilbert_v2.4.1, cybersectony/PhishingEmailDetectionv2.0 (validation / test split); outputs: evaluation_report.
What was the peak RAM consumption during the workflow?	18.4 GB
Has the model been trained in a distributed setting?	No information is provided about distributed training; only one host and one GPU are mentioned.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Not specified in the cards.
What significant input artifacts are involved in the generation of the finetuned model?	distilbert/distilbert-base-uncased and cybersectony/PhishingEmailDetectionv2.0
What is the total energy use for completing the workflow?	Not specified in the cards.
List all input files with size larger than 100Mb	None; the largest input file is the dataset at ~67.2 MB and the base model at ~67 MB.
List all different file types used as input	Parquet (dataset), PyTorch model weights (base model)
Identify the largest output	phishing-email-detection-distilbert_v2.4.1 (fine-tuned model checkpoint, ~260 MB)
What is the science domain of the dataset?	Cybersecurity (Phishing detection)
Does the dataset have a predetermined train-test split?	Yes; train (120,000), validation (20,000), test (60,000)
How many samples are present in the whole dataset?	200,000
What is the data type of the ground truth (if present)?	Integer class label (0–3)
What is the specific task for which the dataset was created?	Multi-class classification (legitimate email, phishing email, legitimate URL, phishing URL)
What is the size in byte of one sample?	~336 bytes (67,150,692 bytes / 200,000 samples)
What is the total size of the whole dataset?	~67.2 MB (67,150,692 bytes)
What are the designed uses for this model?	Phishing detection for emails and URLs; distinguishing legitimate and phishing content
How many epochs have been used in the finetuning?	3
How many model parameters (weights) does the model have?	~67M parameters
What is the science domain of the model?	Cybersecurity (Phishing detection)
What is the task solved by this model (regression or classification or forecast etc.)?	Classification (multi-class)
What is the intended use of this model?	Detecting phishing and legitimate emails and URLs
What is the size of the final model in Mb?	~260 MB (fine-tuned model checkpoint)
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Hugging Face Trainer API (standard fine-tuning)
What is the claimed performance of this model?	Accuracy: 99.58%; F1-score: 99.579%; Precision: 99.583%; Recall: 99.58%
Are the performance shown in the pretrained version improved in the finetuning?	Not specified; only fine-tuned model performance is reported.