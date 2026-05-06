How many activities are present in the whole workflow?	The workflow contains three activities: DataPreparation, ModelFinetuning, and ModelEvaluation.
What is the final status of the workflow?	The final status of the workflow is Completed.
What is the time to completion of the workflow?	The exact time to completion is not specified in the cards ("duration: ~").
List all the parameters of the first activity of the workflow	The first activity, DataPreparation, uses the following parameters: input dataset cybersectony/PhishingEmailDetectionv2.0 (raw), 200,000 entries, two columns (content, label), format Parquet, language English; outputs are train (120,000), validation (20,000), test (60,000) splits.
What hardware was used in the workflow?	The specific hardware used is not detailed in the cards ("compute_hardware: ~", "gpu: ~", "cpu: ~", "memory: ~").
Who is responsible for this workflow (person or username or entity)?	The responsible entity is not specified in the cards ("user: ~").
What was the specific execution order of the tasks?	The execution order is: 1. DataPreparation, 2. ModelFinetuning, 3. ModelEvaluation.
List all parameters for all activites in the workflow	DataPreparation: input dataset (200,000 entries, Parquet, content and label columns), output splits (train, validation, test). ModelFinetuning: base model (distilbert/distilbert-base-uncased), training data (train split), epochs=3, max_length=512, truncation=True. ModelEvaluation: model (finetuned), evaluation data (validation/test split).
What was the peak RAM consumption during the workflow?	Peak RAM consumption is not specified in the cards ("memory: ~").
Has the model been trained in a distributed setting?	There is no information indicating distributed training in the cards.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Total GPU power consumption is not specified in the cards ("gpu: ~").
What significant input artifacts are involved in the generation of the finetuned model?	The significant input artifacts are distilbert/distilbert-base-uncased (pretrained model) and cybersectony/PhishingEmailDetectionv2.0 (dataset).
What is the total energy use for completing the workflow?	Total energy use is not specified in the cards.
List all input files with size larger than 100Mb	No single input file is listed as larger than 100Mb; the total dataset size is ~67.2 MB.
List all different file types used as input	Input file types include Parquet (for the dataset) and PyTorch model weights (for the base model).
Identify the largest output	The largest output is the finetuned model phishing-email-detection-distilbert_v2.4.1.
What is the science domain of the dataset?	The science domain is cybersecurity (phishing detection).
Does the dataset have a predetermined train-test split?	Yes, the dataset is split into train (120,000), validation (20,000), and test (60,000) sets.
How many samples are present in the whole dataset?	The dataset contains 200,000 samples.
What is the data type of the ground truth (if present)?	The ground truth is a multi-class label (integer, 0–3).
What is the specific task for which the dataset was created?	The dataset was created for multi-class classification of emails and URLs as legitimate or phishing.
What is the size in byte of one sample?	Average sample size is approximately 335 bytes (67,150,692 bytes / 200,000 samples).
What is the total size of the whole dataset?	The total dataset size is approximately 67.2 MB (67,150,692 bytes).
What are the designed uses for this model?	The model is designed for phishing detection in emails and URLs, classifying content as legitimate or phishing.
How many epochs have been used in the finetuning?	The model was fine-tuned for 3 epochs.
How many model parameters (weights) does the model have?	The model has approximately 67 million parameters.
What is the science domain of the model?	The science domain is cybersecurity (phishing detection).
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves a classification task (multi-class classification).
What is the intended use of this model?	The intended use is to detect phishing in emails and URLs.
What is the size of the final model in Mb?	The size of the final model is not specified, but the base model is ~67MB; the finetuned model is likely similar.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using the Hugging Face Trainer API.
What is the claimed performance of this model?	The claimed performance is 99.58% accuracy, 99.579% F1-score, 99.583% precision, and 99.58% recall.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the finetuned model achieves high accuracy and F1 on phishing detection, which is a downstream task not present in the pretrained version.