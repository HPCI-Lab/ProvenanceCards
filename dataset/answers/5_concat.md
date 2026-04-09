How many activities are present in the whole workflow?	1
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	4h 30m 00s
List all the parameters of the first activity of the workflow	Epochs: 3, Max Length: 512, Task: Multilabel
What hardware was used in the workflow?	1x NVIDIA V100 (16GB)
Who is responsible for this workflow (person or username or entity)?	cybersectony
What was the specific execution order of the tasks?	phish-classifier-training
List all the parameters for the whole workflow process	Epochs: 3, Max Length: 512, Task: Multilabel
What was the peak RAM consumption during the workflow?	
Has the model been trained in a distributed setting?	
What was the real-time power consumption (in Watts) of the GPU during the workflow?	
Which inputs influenced the output in the workflow?	distilbert-base-uncased, PhishingEmailDetectionv2.0
What is the total energy use for completing the workflow?	
List all input files with size larger than 100Mb	data/train-*, data/test-*
List all different file types used as input	Pretrained Distilled BERT Model, Email and URL Classification Dataset
Identify the largest output	phishing-email-detection-distilbert_v2.4.1
What is the science domain of the dataset?	Cybersecurity
Does the dataset have a predetermined train-test split?	Yes
How many samples are present in the whole dataset?	200000
What is the data type of the ground truth (if present)?	int64
What is the specific task for which the dataset was created?	Multi-class Classification
What is the size in byte of one sample?	
What is the total size of the whole dataset?	67150692
What are the designed uses for this model?	Multilabel Classification of Emails and URLs as safe or phishing
How many epochs have been used in the final training?	3
How many model parameters (weights) does the model have?	
What is the science domain of the model?	Cybersecurity
What is the task solved by this model (regression or classification or forecast etc.)?	Classification
What is the intended use of this model?	Phishing Email and URL Detection
What is the size of the final model in Mb?	
What technique was used to train the model?	Supervised Fine-Tuning (SFT)
What is the claimed performance of this model?	Accuracy: 99.58, F1: 99.579, Precision: 99.583, Recall: 99.58
Are the performance shown in the pretrained version improved in the finetuning?	Yes