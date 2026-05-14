How many activities are present in the whole workflow?	The workflow includes pretraining DistilBERT, fine-tuning on the phishing email detection dataset, and evaluation. At least three main activities are described: pretraining, fine-tuning, and evaluation.
What is the final status of the workflow?	The workflow was completed successfully, resulting in a fine-tuned DistilBERT model for phishing email and URL detection, with reported performance metrics.
What is the time to completion of the workflow?	The pretraining of DistilBERT took 90 hours on 8 V100 GPUs. The fine-tuning for phishing detection was performed for 3 epochs, but the exact time for fine-tuning is not specified.
List all the parameters of the first activity of the workflow	The first activity, pretraining DistilBERT, used the following parameters: lowercased text, WordPiece tokenization (vocab size 30,000), sequence length up to 512 tokens, 15% token masking, 8 V100 GPUs, 90 hours, and three training objectives (distillation loss, MLM, cosine embedding loss).
What hardware was used in the workflow?	Pretraining was performed on 8 NVIDIA V100 GPUs with 16 GB memory each.
Who is responsible for this workflow (person or username or entity)?	The DistilBERT model was developed by Victor Sanh, Lysandre Debut, Julien Chaumond, and Thomas Wolf. The phishing detection fine-tuning was performed by the Hugging Face user/entity "cybersectony".
What was the specific execution order of the tasks?	The workflow order is: (1) Pretraining DistilBERT on BookCorpus and Wikipedia, (2) Fine-tuning on the phishing email detection dataset, (3) Evaluation on test/validation splits.
List all parameters for all activites in the workflow	Pretraining: lowercased text, WordPiece tokenizer (vocab 30,000), max length 512, 15% masking, 8 V100 GPUs, 90 hours, distillation loss, MLM, cosine embedding loss. Fine-tuning: DistilBERT base, 3 epochs, Hugging Face Trainer API, phishing email detection dataset, multi-class classification.
What was the peak RAM consumption during the workflow?	Peak RAM consumption is not specified in the provided cards.
Has the model been trained in a distributed setting?	Yes, pretraining was performed in a distributed setting using 8 V100 GPUs.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Total power consumption in Watts is not specified in the provided cards.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts include the BookCorpus and Wikipedia datasets for pretraining, and the "cybersectony/PhishingEmailDetectionv2.0" dataset for fine-tuning.
What is the total energy use for completing the workflow?	Total energy use is not specified in the provided cards.
List all input files with size larger than 100Mb	The phishing email detection dataset has splits: train (47,241,927 bytes), validation (5,052,323 bytes), test (14,856,442 bytes). None of these exceed 100MB. BookCorpus and Wikipedia are used for pretraining but their sizes are not specified here.
List all different file types used as input	Input files are in text format, with columns for content (string) and label (int or class label).
Identify the largest output	The largest output is the fine-tuned DistilBERT model for phishing email detection.
What is the science domain of the dataset?	The dataset is in the cybersecurity domain, specifically for phishing detection in emails and URLs.
Does the dataset have a predetermined train-test split?	Yes, the dataset is split into train (120,000), validation (20,000), and test (60,000) sets.
How many samples are present in the whole dataset?	The dataset contains a total of 200,000 samples.
What is the data type of the ground truth (if present)?	The ground truth is a multi-class label (integer or class label) with four possible classes.
What is the specific task for which the dataset was created?	The dataset was created for multi-class classification of emails and URLs as legitimate or phishing.
What is the size in byte of one sample?	Average sample size is not specified, but the train split (120,000 samples) is 47,241,927 bytes, so approximately 393 bytes per sample.
What is the total size of the whole dataset?	The total dataset size is 67,150,692 bytes (about 67 MB).
What are the designed uses for this model?	The model is designed for phishing detection in emails and URLs, classifying content as legitimate or phishing.
How many epochs have been used in the finetuning?	Fine-tuning was performed for 3 epochs.
How many model parameters (weights) does the model have?	The number of parameters is not specified in the cards, but DistilBERT base typically has 66 million parameters.
What is the science domain of the model?	The model is in the cybersecurity domain, focused on phishing detection.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves a multi-class classification task.
What is the intended use of this model?	The intended use is to detect phishing in emails and URLs, classifying them as legitimate or phishing.
What is the size of the final model in Mb?	The size of the final model is not specified, but DistilBERT base models are typically around 250 MB.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using the Hugging Face Trainer API for sequence classification.
What is the claimed performance of this model?	The model claims 99.58% accuracy, 99.579 F1-score, 99.583 precision, and 99.58 recall.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the fine-tuned model achieves high performance on phishing detection, which is a downstream task not addressed by the pretrained version.