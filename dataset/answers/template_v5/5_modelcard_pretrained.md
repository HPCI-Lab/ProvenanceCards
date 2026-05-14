How many activities are present in the whole workflow?	The card does not specify the number of activities in the workflow.
What is the final status of the workflow?	The card does not specify the final status of the workflow.
What is the time to completion of the workflow?	The card states that pretraining took 90 hours on 8 16GB V100 GPUs.
List all the parameters of the first activity of the workflow	The card does not specify parameters for individual activities.
What hardware was used in the workflow?	8 16GB V100 GPUs were used for pretraining.
Who is responsible for this workflow (person or username or entity)?	The authors are Victor Sanh, Lysandre Debut, Julien Chaumond, and Thomas Wolf.
What was the specific execution order of the tasks?	The card does not specify the execution order of tasks.
List all parameters for all activites in the workflow	The card does not specify parameters for all activities.
What was the peak RAM consumption during the workflow?	The card does not specify peak RAM consumption.
Has the model been trained in a distributed setting?	Yes, the model was trained on 8 GPUs, indicating distributed training.
What was the total power consumption in Watts of the GPU(s) during the workflow?	The card does not specify total power consumption in Watts.
What significant input artifacts are involved in the generation of the finetuned model?	The significant input artifacts are the BookCorpus and English Wikipedia datasets.
What is the total energy use for completing the workflow?	The card does not specify total energy use.
List all input files with size larger than 100Mb	The card does not specify input file sizes.
List all different file types used as input	The card does not specify file types, but mentions BookCorpus and Wikipedia text data.
Identify the largest output	The card does not specify the largest output.
What is the science domain of the dataset?	The datasets are from general English language sources (books and Wikipedia), so the domain is general language.
Does the dataset have a predetermined train-test split?	The card does not specify if there is a predetermined train-test split.
How many samples are present in the whole dataset?	The card does not specify the number of samples.
What is the data type of the ground truth (if present)?	The ground truth is masked tokens for masked language modeling.
What is the specific task for which the dataset was created?	The dataset is used for masked language modeling and next sentence prediction.
What is the size in byte of one sample?	The card does not specify the size of one sample.
What is the total size of the whole dataset?	The card does not specify the total dataset size.
What are the designed uses for this model?	The model is designed for masked language modeling, next sentence prediction, and fine-tuning for tasks like sequence classification, token classification, and question answering.
How many epochs have been used in the finetuning?	The card does not specify the number of epochs used in finetuning.
How many model parameters (weights) does the model have?	The card does not specify the number of parameters, but DistilBERT base typically has 66 million parameters.
What is the science domain of the model?	The model is for general English language understanding.
What is the task solved by this model (regression or classification or forecast etc.)?	The model is primarily for classification tasks (sequence and token classification), masked language modeling, and question answering.
What is the intended use of this model?	The intended use is for fine-tuning on downstream NLP tasks such as classification and question answering.
What is the size of the final model in Mb?	The card does not specify the model size, but DistilBERT base is typically about 256 MB.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The card does not specify a fine-tuning technique; it describes pretraining via distillation, MLM, and cosine embedding loss.
What is the claimed performance of this model?	The card reports GLUE test results: MNLI 82.2, QQP 88.5, QNLI 89.2, SST-2 91.3, CoLA 51.3, STS-B 85.8, MRPC 87.5, RTE 59.9.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the card presents results for fine-tuned downstream tasks, indicating improved performance after fine-tuning.