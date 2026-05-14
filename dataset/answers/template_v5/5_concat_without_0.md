How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	3h 33m 28s
List all the parameters of the first activity of the workflow	Inputs: cybersectony/PhishingEmailDetectionv2.0 (raw) — 200,000 entries combining email messages (22,644) and URLs (177,356); two columns: content (string) and label (integer 0–3: legitimate_email, phishing_email, legitimate_url, phishing_url); format: Parquet; language: English. Outputs: train (120,000 examples, ~47.2 MB), validation (20,000 examples, ~5.1 MB), test (60,000 examples, ~14.9 MB); total dataset size: ~67.2 MB.
What hardware was used in the workflow?	1× NVIDIA T4-16GB GPU, Intel Xeon Platinum 8259CL CPU, 32 GB RAM, AWS EC2 g4dn.2xlarge, Ubuntu 22.04.3 LTS
Who is responsible for this workflow (person or username or entity)?	cybersectony
What was the specific execution order of the tasks?	1. DataPreparation 2. ModelFinetuning 3. ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: Inputs: cybersectony/PhishingEmailDetectionv2.0 (raw); Outputs: train/validation/test splits. ModelFinetuning: Inputs: distilbert/distilbert-base-uncased, train split; Outputs: phishing-email-detection-distilbert_v2.4.1. ModelEvaluation: Inputs: fine-tuned model, validation/test splits; Outputs: evaluation_report.
What was the peak RAM consumption during the workflow?	18.4 GB
Has the model been trained in a distributed setting?	No evidence of distributed training; single GPU (NVIDIA T4-16GB) was used.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Not specified in the cards.
What significant input artifacts are involved in the generation of the finetuned model?	distilbert/distilbert-base-uncased (pretrained model weights), cybersectony/PhishingEmailDetectionv2.0 (dataset)
What is the total energy use for completing the workflow?	Not specified in the cards.
List all input files with size larger than 100Mb	None; largest input is the dataset (~67.2 MB) and base model weights (~67 MB).
List all different file types used as input	Parquet (dataset), PyTorch model weights (base model)
Identify the largest output	phishing-email-detection-distilbert_v2.4.1 (fine-tuned model checkpoint, ~260 MB)
What is the science domain of the dataset?	Cybersecurity (phishing detection)
Does the dataset have a predetermined train-test split?	Yes; train (120,000), validation (20,000), test (60,000)
How many samples are present in the whole dataset?	200,000
What is the data type of the ground truth (if present)?	Integer (0–3), ClassLabel (multi-class)
What is the specific task for which the dataset was created?	Multi-class classification (phishing detection: legitimate email, phishing email, legitimate URL, phishing URL)
What is the size in byte of one sample?	Approx. 335 bytes (67,150,692 bytes / 200,000 samples)
What is the total size of the whole dataset?	67,150,692 bytes (~67.2 MB)
What are the designed uses for this model?	Sequence classification for phishing detection (legitimate email, phishing email, legitimate URL, phishing URL); intended for downstream tasks such as email and URL classification.
How many epochs have been used in the finetuning?	3
How many model parameters (weights) does the model have?	~67 million
What is the science domain of the model?	Natural Language Processing (NLP), Cybersecurity
What is the task solved by this model (regression or classification or forecast etc.)?	Classification (multi-class sequence classification)
What is the intended use of this model?	Phishing detection in emails and URLs; sequence classification for cybersecurity applications.
What is the size of the final model in Mb?	~260 MB (fine-tuned model checkpoint)
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Hugging Face Trainer API (standard supervised fine-tuning)
What is the claimed performance of this model?	Accuracy: 99.58%; F1-score (micro): 99.579%; Precision: 99.583%; Recall: 99.58%
Are the performance shown in the pretrained version improved in the finetuning?	Yes; the fine-tuned model achieves high accuracy and F1 on phishing detection, which is a downstream task not covered by the pretrained GLUE scores.