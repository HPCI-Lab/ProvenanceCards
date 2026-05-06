How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	~
List all the parameters of the first activity of the workflow	No explicit parameters are listed for DataPreparation; the activity uses the input dataset (200,000 entries, two columns: content and label) and outputs train/validation/test splits.
What hardware was used in the workflow?	~
Who is responsible for this workflow (person or username or entity)?	~
What was the specific execution order of the tasks?	DataPreparation → ModelFinetuning → ModelEvaluation
List all parameters for all activites in the workflow	epochs: 3, max_length: 512, truncation: True (applies to ModelFinetuning); no explicit parameters for DataPreparation or ModelEvaluation.
What was the peak RAM consumption during the workflow?	~
Has the model been trained in a distributed setting?	Not specified
What was the total power consumption in Watts of the GPU(s) during the workflow?	~
What significant input artifacts are involved in the generation of the finetuned model?	distilbert/distilbert-base-uncased; cybersectony/PhishingEmailDetectionv2.0 (train split)
What is the total energy use for completing the workflow?	~
List all input files with size larger than 100Mb	None; the largest input is ~67.2 MB
List all different file types used as input	Parquet (dataset), PyTorch model weights (pretrained model)
Identify the largest output	phishing-email-detection-distilbert_v2.4.1 (fine-tuned model)
What is the science domain of the dataset?	Cybersecurity (phishing detection)
Does the dataset have a predetermined train-test split?	Yes (train: 120,000; validation: 20,000; test: 60,000)
How many samples are present in the whole dataset?	200,000
What is the data type of the ground truth (if present)?	Integer (label: 0–3)
What is the specific task for which the dataset was created?	4-class sequence classification (legitimate email, phishing email, legitimate URL, phishing URL)
What is the size in byte of one sample?	~336 bytes (67.2 MB / 200,000)
What is the total size of the whole dataset?	~67.2 MB
What are the designed uses for this model?	Detecting and classifying emails and URLs as legitimate or phishing (4-class sequence classification)
How many epochs have been used in the finetuning?	3
How many model parameters (weights) does the model have?	~67M
What is the science domain of the model?	Cybersecurity (phishing detection)
What is the task solved by this model (regression or classification or forecast etc.)?	Classification (4-class sequence classification)
What is the intended use of this model?	Detecting and classifying emails and URLs as legitimate or phishing
What is the size of the final model in Mb?	Not explicitly stated; likely similar to input model (~67M parameters, typical size ~250 MB)
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Hugging Face Trainer API (standard supervised fine-tuning)
What is the claimed performance of this model?	Accuracy: 99.58%; F1-score (micro): 99.579%; precision: 99.583%; recall: 99.58%
Are the performance shown in the pretrained version improved in the finetuning?	Not specified; only fine-tuned model performance is reported