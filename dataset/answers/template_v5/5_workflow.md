How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	3h 33m 28s
List all the parameters of the first activity of the workflow	content (string), label (integer 0–3), format: Parquet, language: English
What hardware was used in the workflow?	1× NVIDIA T4-16GB GPU, Intel Xeon Platinum 8259CL CPU, 32 GB RAM, host OS: Ubuntu 22.04.3 LTS
Who is responsible for this workflow (person or username or entity)?	cybersectony
What was the specific execution order of the tasks?	DataPreparation → ModelFinetuning → ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: content (string), label (integer 0–3), format: Parquet, language: English; ModelFinetuning: epochs=3, max_length=512, truncation=True, num_labels=4; ModelEvaluation: evaluation on validation/test split, metrics: accuracy, F1-score, precision, recall
What was the peak RAM consumption during the workflow?	18.4 GB
Has the model been trained in a distributed setting?	No evidence of distributed training; single EC2 instance with 1 GPU used
What was the total power consumption in Watts of the GPU(s) during the workflow?	Not specified in the cards
What significant input artifacts are involved in the generation of the finetuned model?	distilbert/distilbert-base-uncased (pretrained model), cybersectony/PhishingEmailDetectionv2.0 (dataset)
What is the total energy use for completing the workflow?	Not specified in the cards
List all input files with size larger than 100Mb	None; all input files are below 100 MB (largest: dataset ~67.2 MB)
List all different file types used as input	Parquet (dataset), PyTorch model weights
Identify the largest output	phishing-email-detection-distilbert_v2.4.1 (fine-tuned model checkpoint, ~260 MB)
What is the science domain of the dataset?	Cybersecurity (phishing detection)
Does the dataset have a predetermined train-test split?	Yes; train (120,000), validation (20,000), test (60,000)
How many samples are present in the whole dataset?	200,000
What is the data type of the ground truth (if present)?	integer (0–3) label
What is the specific task for which the dataset was created?	Phishing detection (classification of emails and URLs as legitimate or phishing)
What is the size in byte of one sample?	Approximately 336 bytes (67.2 MB / 200,000 samples)
What is the total size of the whole dataset?	~67.2 MB
What are the designed uses for this model?	Detection and classification of legitimate/phishing emails and URLs
How many epochs have been used in the finetuning?	3
How many model parameters (weights) does the model have?	~67M parameters
What is the science domain of the model?	Cybersecurity (phishing detection)
What is the task solved by this model (regression or classification or forecast etc.)?	Classification (4-class sequence classification)
What is the intended use of this model?	Detecting and classifying phishing and legitimate emails and URLs
What is the size of the final model in Mb?	~260 MB (fine-tuned model checkpoint)
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Hugging Face Trainer API (standard supervised fine-tuning)
What is the claimed performance of this model?	Accuracy: 99.58%; F1-score (micro): 99.579%; Precision: 99.583%; Recall: 99.58%
Are the performance shown in the pretrained version improved in the finetuning?	Yes; the fine-tuned model achieves high accuracy and F1 on phishing detection, which is a domain-specific task not covered by the pretrained version