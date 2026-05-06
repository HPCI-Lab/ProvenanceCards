How many activities are present in the whole workflow?	There is no explicit enumeration of activities in the workflow, but the workflow includes at least data preparation, model finetuning, evaluation, and inference, based on the description provided.
What is the final status of the workflow?	The workflow was completed successfully, as evidenced by the reported results after 80 epochs of finetuning and the availability of inference scripts and demo.
What is the time to completion of the workflow?	The time to completion is not specified in the provided information.
List all the parameters of the first activity of the workflow	The parameters for the first activity (finetuning) are not fully listed, but the configuration file used is referenced: multi_temporal_crop_classification.py, which includes parameters such as number of epochs (80), input shape (224x224x18), number of classes (13), and model backbone (Prithvi-100M).
What hardware was used in the workflow?	The hardware used in the workflow is not specified in the provided information.
Who is responsible for this workflow (person or username or entity)?	The responsible entities are the authors listed in the citation: Li, Hanxi (Steve); Khallaghi, Sam; Cecil, Michael; Kordi, Fatemeh; Fraccaro, Paolo; Alemohammad, Hamed; Ramachandran, Rahul.
What was the specific execution order of the tasks?	The specific execution order is: data preparation, model finetuning using the provided config, evaluation of results, and inference using the inference script.
List all parameters for all activites in the workflow	Parameters include: input shape (224x224x18), number of bands (6 per timestep), number of timesteps (3), number of classes (13), model backbone (Prithvi-100M), number of epochs (80), and CDL labels as ground truth.
What was the peak RAM consumption during the workflow?	Peak RAM consumption is not specified in the provided information.
Has the model been trained in a distributed setting?	There is no information provided about distributed training.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Total power consumption in Watts is not specified in the provided information.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts include HLS geotiff images with 18 bands (3 timesteps x 6 bands) and CDL labels from the multi_temporal_crop_classification dataset.
What is the total energy use for completing the workflow?	Total energy use is not specified in the provided information.
List all input files with size larger than 100Mb	Input files larger than 100Mb are not explicitly listed, but the HLS geotiff images used for training are likely to exceed 100Mb due to their size and band count.
List all different file types used as input	Input file types include geotiff images and CDL label files.
Identify the largest output	The largest output is the finetuned Prithvi-100M model weights.
What is the science domain of the dataset?	The science domain of the dataset is geospatial crop classification and land cover mapping.
Does the dataset have a predetermined train-test split?	There is no explicit mention of a predetermined train-test split in the provided information.
How many samples are present in the whole dataset?	The total number of samples in the dataset is not specified in the provided information.
What is the data type of the ground truth (if present)?	The ground truth data type is categorical, with 13 classes from CDL labels.
What is the specific task for which the dataset was created?	The dataset was created for multi-temporal crop and land cover classification using remote sensing data.
What is the size in byte of one sample?	The size in bytes of one sample is not specified, but each sample is a 224x224x18 array, likely several megabytes depending on encoding.
What is the total size of the whole dataset?	The total size of the dataset is not specified in the provided information.
What are the designed uses for this model?	Designed uses include crop classification, land cover mapping, and geospatial analysis using multi-temporal remote sensing data.
How many epochs have been used in the finetuning?	Finetuning was performed for 80 epochs.
How many model parameters (weights) does the model have?	The model has 100 million parameters (Prithvi-EO-1.0-100M).
What is the science domain of the model?	The science domain of the model is geospatial remote sensing and crop classification.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves a classification task (crop and land cover classification).
What is the intended use of this model?	The intended use is for crop classification and land cover mapping from multi-temporal remote sensing data.
What is the size of the final model in Mb?	The size of the final model in Mb is not specified in the provided information.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using standard supervised learning techniques with the mmsegmentation stack.
What is the claimed performance of this model?	The claimed performance is: overall accuracy (aAcc) 60.64%, mean IoU (mIoU) 0.4269, mean accuracy (mAcc) 64.06%, with class-wise IoU and accuracy also reported.
Are the performance shown in the pretrained version improved in the finetuning?	Finetuning with multi-temporal data and CDL labels is claimed to improve generalization and performance compared to the pretrained version, as indicated by the reported results.