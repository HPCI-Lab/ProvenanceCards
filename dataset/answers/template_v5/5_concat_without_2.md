How many activities are present in the whole workflow?	3 activities are present in the workflow: DataPreparation, ModelFinetuning, and ModelEvaluation.
What is the final status of the workflow?	The final status of the workflow is Completed, with all activities marked as success or finished.
What is the time to completion of the workflow?	The exact time to completion is not specified in the cards; the duration fields are marked as ~.
List all the parameters of the first activity of the workflow	The first activity, DataPreparation, uses the following parameters: input dataset cybersectony/PhishingEmailDetectionv2.0 (raw), 200,000 entries, two columns (content, label), format Parquet, language English, and outputs train/validation/test splits.
What hardware was used in the workflow?	The specific hardware used (CPU, GPU, memory, etc.) is not provided; the fields for compute_hardware, cpu, memory, gpu, disk, and network are marked as ~.
Who is responsible for this workflow (person or username or entity)?	The responsible entity is not explicitly stated; user and related fields are marked as ~.
What was the specific execution order of the tasks?	The execution order is: 1. DataPreparation, 2. ModelFinetuning, 3. ModelEvaluation.
List all parameters for all activites in the workflow	DataPreparation: input dataset (200,000 entries, content and label columns, Parquet format), output: train/validation/test splits. ModelFinetuning: input model (distilbert/distilbert-base-uncased), input train split (120,000 examples, max_length=512, truncation=True, 4-class labels), output: fine-tuned model. ModelEvaluation: input fine-tuned model, input validation/test split, output: evaluation report (accuracy, F1, precision, recall).
What was the peak RAM consumption during the workflow?	Peak RAM consumption is not specified; the memory field is marked as ~.
Has the model been trained in a distributed setting?	There is no information indicating distributed training; no mention of multi-node or multi-GPU setup.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Total power consumption is not specified; the gpu and energy fields are marked as ~.
What significant input artifacts are involved in the generation of the finetuned model?	The significant input artifacts are: distilbert/distilbert-base-uncased (pretrained model weights, ~67M parameters) and cybersectony/PhishingEmailDetectionv2.0 (train split, 120,000 examples).
What is the total energy use for completing the workflow?	Total energy use is not specified in the cards.
List all input files with size larger than 100Mb	The only input file with size larger than 100Mb is the full cybersectony/PhishingEmailDetectionv2.0 dataset (~67.2 MB), which is less than 100Mb; no input files above 100Mb are listed.
List all different file types used as input	Input file types include Parquet (for the dataset) and PyTorch model weights (for the pretrained model).
Identify the largest output	The largest output is the fine-tuned model artifact: phishing-email-detection-distilbert_v2.4.1.
What is the science domain of the dataset?	The science domain is cybersecurity, specifically phishing detection in emails and URLs.
Does the dataset have a predetermined train-test split?	Yes, the dataset is split into train (120,000), validation (20,000), and test (60,000) sets.
How many samples are present in the whole dataset?	The dataset contains 200,000 samples in total.
What is the data type of the ground truth (if present)?	The ground truth is an integer class label (0–3), corresponding to four classes.
What is the specific task for which the dataset was created?	The dataset was created for multi-class classification of emails and URLs as legitimate or phishing.
What is the size in byte of one sample?	Average sample size is approximately 335 bytes (67,150,692 bytes / 200,000 samples).
What is the total size of the whole dataset?	The total dataset size is approximately 67.2 MB (67,150,692 bytes).
What are the designed uses for this model?	The model is designed for phishing detection in emails and URLs, distinguishing between legitimate and phishing content.
How many epochs have been used in the finetuning?	3 epochs were used for fine-tuning.
How many model parameters (weights) does the model have?	The model has approximately 67 million parameters.
What is the science domain of the model?	The science domain is cybersecurity, focusing on phishing detection.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves a classification task (multi-class classification).
What is the intended use of this model?	The intended use is to classify emails and URLs as legitimate or phishing for security applications.
What is the size of the final model in Mb?	The size of the final model is not explicitly stated, but the base model is ~67M parameters, typically around 250–300 MB for DistilBERT.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using the Hugging Face Trainer API (standard supervised fine-tuning).
What is the claimed performance of this model?	The model claims 99.58% accuracy, 99.579% F1-score, 99.583% precision, and 99.58% recall.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the fine-tuned model achieves high performance on phishing detection, which is a downstream task not covered by the pretrained version.