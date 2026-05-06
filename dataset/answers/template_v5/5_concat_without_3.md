How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	~
List all the parameters of the first activity of the workflow	No explicit parameters are listed for DataPreparation; only input and output datasets are described.
What hardware was used in the workflow?	~
Who is responsible for this workflow (person or username or entity)?	~
What was the specific execution order of the tasks?	1. DataPreparation  2. ModelFinetuning  3. ModelEvaluation
List all parameters for all activites in the workflow	epochs: 3, max_length: 512, truncation: True (for ModelFinetuning); no explicit parameters for DataPreparation or ModelEvaluation.
What was the peak RAM consumption during the workflow?	~
Has the model been trained in a distributed setting?	Not specified.
What was the total power consumption in Watts of the GPU(s) during the workflow?	~
What significant input artifacts are involved in the generation of the finetuned model?	distilbert/distilbert-base-uncased (~67M parameters, PyTorch model weights); cybersectony/PhishingEmailDetectionv2.0 (200,000 entries, Parquet format)
What is the total energy use for completing the workflow?	~
List all input files with size larger than 100Mb	None; the largest input file is ~67.2 MB.
List all different file types used as input	Parquet, PyTorch model weights
Identify the largest output	phishing-email-detection-distilbert_v2.4.1 (fine-tuned DistilBERT model)
What is the science domain of the dataset?	Cybersecurity (Phishing detection)
Does the dataset have a predetermined train-test split?	Yes (train: 120,000; validation: 20,000; test: 60,000)
How many samples are present in the whole dataset?	200,000
What is the data type of the ground truth (if present)?	Integer label (0–3)
What is the specific task for which the dataset was created?	Multiclass classification (legitimate_email, phishing_email, legitimate_url, phishing_url)
What is the size in byte of one sample?	Approximately 561 bytes (67.2 MB / 120,000 train + 20,000 validation + 60,000 test = 200,000 samples)
What is the total size of the whole dataset?	~67.2 MB
What are the designed uses for this model?	Phishing email and URL detection (sequence classification)
How many epochs have been used in the finetuning?	3
How many model parameters (weights) does the model have?	~67 million
What is the science domain of the model?	Cybersecurity / Natural Language Processing
What is the task solved by this model (regression or classification or forecast etc.)?	Classification (4-class sequence classification)
What is the intended use of this model?	Detecting phishing and legitimate emails and URLs
What is the size of the final model in Mb?	Not explicitly stated; base model is ~256 MB, fine-tuned model is likely similar.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Hugging Face Trainer API (standard supervised fine-tuning)
What is the claimed performance of this model?	Accuracy: 99.58%; F1-score: 99.579%; Precision: 99.583%; Recall: 99.58%
Are the performance shown in the pretrained version improved in the finetuning?	Yes; the fine-tuned model achieves high accuracy and F1 on phishing detection, which is a downstream task not present in the base model.