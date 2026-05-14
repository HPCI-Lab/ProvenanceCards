How many activities are present in the whole workflow?	3 activities are present: DataPreparation, ModelFinetuning, and ModelEvaluation.
What is the final status of the workflow?	The workflow status is Completed.
What is the time to completion of the workflow?	The workflow started at 2024-05-09T14:10:00Z and ended at 2024-05-09T17:43:28Z, for a total duration of 3 hours, 33 minutes, and 28 seconds.
List all the parameters of the first activity of the workflow	The first activity, DataPreparation, uses the following parameters: input dataset cybersectony/PhishingEmailDetectionv2.0 (raw), 200,000 entries, two columns: content (string) and label (integer 0–3), format: Parquet, language: English. Output: train (120,000), validation (20,000), test (60,000) splits.
What hardware was used in the workflow?	Hardware used: 1× NVIDIA T4-16GB GPU, Intel Xeon Platinum 8259CL CPU, 32 GB RAM, running Ubuntu 22.04.3 LTS on AWS EC2 g4dn.2xlarge.
Who is responsible for this workflow (person or username or entity)?	The responsible user is cybersectony.
What was the specific execution order of the tasks?	The execution order is: 1. DataPreparation, 2. ModelFinetuning, 3. ModelEvaluation.
List all parameters for all activites in the workflow	DataPreparation: input dataset (cybersectony/PhishingEmailDetectionv2.0), output splits (train/validation/test). ModelFinetuning: base model (distilbert/distilbert-base-uncased), training data (train split), epochs=3, max_length=512, truncation=True. ModelEvaluation: fine-tuned model, validation/test splits.
What was the peak RAM consumption during the workflow?	Peak RAM usage was 18.4 GB (tokenised dataset fully cached in memory plus DataLoader workers buffer).
Has the model been trained in a distributed setting?	No, the model was trained on a single machine with 1 GPU; no distributed training is mentioned.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Not specified in the cards; no information about total power consumption in Watts is provided.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts: distilbert/distilbert-base-uncased (base model, ~67M parameters), cybersectony/PhishingEmailDetectionv2.0 (dataset, 200,000 entries, Parquet format).
What is the total energy use for completing the workflow?	Not specified in the cards; no information about total energy use is provided.
List all input files with size larger than 100Mb	No input files larger than 100 MB are listed; the largest input is the dataset (~67.2 MB) and base model weights (~67 MB).
List all different file types used as input	Input file types: Parquet (dataset), PyTorch model weights (base model).
Identify the largest output	The largest output is the fine-tuned model checkpoint (phishing-email-detection-distilbert_v2.4.1), size ~260 MB.
What is the science domain of the dataset?	The dataset is in the cybersecurity domain, specifically phishing detection.
Does the dataset have a predetermined train-test split?	Yes, the dataset is split into train (120,000), validation (20,000), and test (60,000) sets.
How many samples are present in the whole dataset?	The dataset contains 200,000 samples.
What is the data type of the ground truth (if present)?	The ground truth is an integer class label (0–3).
What is the specific task for which the dataset was created?	The dataset was created for multi-class classification: distinguishing legitimate emails, phishing emails, legitimate URLs, and phishing URLs.
What is the size in byte of one sample?	Average sample size is approximately 336 bytes (67,200,000 bytes / 200,000 samples).
What is the total size of the whole dataset?	The total dataset size is approximately 67.2 MB.
What are the designed uses for this model?	Designed uses: sequence classification of emails and URLs as legitimate or phishing; phishing detection in cybersecurity applications.
How many epochs have been used in the finetuning?	3 epochs were used for fine-tuning.
How many model parameters (weights) does the model have?	The model has approximately 67 million parameters.
What is the science domain of the model?	The model is in the cybersecurity domain, focused on phishing detection.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves a classification task (multi-class sequence classification).
What is the intended use of this model?	The intended use is to classify emails and URLs as legitimate or phishing for security applications.
What is the size of the final model in Mb?	The final model checkpoint is approximately 260 MB.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using the Hugging Face Trainer API (standard supervised fine-tuning).
What is the claimed performance of this model?	Claimed performance: Accuracy 99.58%, F1-score 99.579%, Precision 99.583%, Recall 99.58%.
Are the performance shown in the pretrained version improved in the finetuning?	Yes; the base model is not a phishing detector, so fine-tuning on the phishing dataset yields high classification performance (99.58% accuracy), which is an improvement for this task.