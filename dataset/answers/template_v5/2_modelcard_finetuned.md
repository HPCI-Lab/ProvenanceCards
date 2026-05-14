How many activities are present in the whole workflow?	There is no explicit enumeration of activities in the workflow, but the workflow includes at least data preparation, model finetuning, evaluation, and inference, as described in the documentation.
What is the final status of the workflow?	The workflow resulted in a finetuned model for multi-temporal crop classification, with performance metrics reported after 80 epochs of training.
What is the time to completion of the workflow?	The time to completion is not specified in the documentation.
List all the parameters of the first activity of the workflow	The parameters for the first activity (finetuning) are available in the linked configuration file, but not listed in the documentation. The input shape is 224x224x18, with 6 bands per timestep and 3 timesteps, and 13 output classes.
What hardware was used in the workflow?	The hardware used in the workflow is not specified in the documentation.
Who is responsible for this workflow (person or username or entity)?	The responsible entities are the authors listed in the citation: Li, Hanxi (Steve); Khallaghi, Sam; Cecil, Michael; Kordi, Fatemeh; Fraccaro, Paolo; Alemohammad, Hamed; Ramachandran, Rahul.
What was the specific execution order of the tasks?	The execution order is: data preparation, model finetuning using the mmseg stack and config, evaluation, and inference.
List all parameters for all activites in the workflow	The parameters for all activities are not fully listed in the documentation; key parameters include input shape (224x224x18), 6 bands per timestep, 3 timesteps, 13 classes, and 80 epochs for finetuning.
What was the peak RAM consumption during the workflow?	Peak RAM consumption is not specified in the documentation.
Has the model been trained in a distributed setting?	There is no information provided about distributed training in the documentation.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Total power consumption in Watts is not specified in the documentation.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts include HLS geotiff images with 18 bands (3 timesteps x 6 bands), CDL labels, and the multi_temporal_crop_classification dataset.
What is the total energy use for completing the workflow?	Total energy use is not specified in the documentation.
List all input files with size larger than 100Mb	Input files larger than 100Mb are not specified in the documentation.
List all different file types used as input	Input file types include geotiff images and CDL label files.
Identify the largest output	The largest output is the finetuned Prithvi-100M multi-temporal crop classification model.
What is the science domain of the dataset?	The science domain of the dataset is geospatial crop and land cover classification.
Does the dataset have a predetermined train-test split?	The documentation does not specify whether the dataset has a predetermined train-test split.
How many samples are present in the whole dataset?	The total number of samples in the dataset is not specified in the documentation.
What is the data type of the ground truth (if present)?	The ground truth data type is categorical, with 13 classes from CDL labels.
What is the specific task for which the dataset was created?	The dataset was created for multi-temporal crop and land cover classification using remote sensing data.
What is the size in byte of one sample?	The size in bytes of one sample is not specified in the documentation.
What is the total size of the whole dataset?	The total size of the dataset is not specified in the documentation.
What are the designed uses for this model?	Designed uses for this model include crop and land cover classification from multi-temporal remote sensing data.
How many epochs have been used in the finetuning?	Finetuning was performed for 80 epochs.
How many model parameters (weights) does the model have?	The model has 100 million parameters.
What is the science domain of the model?	The science domain of the model is geospatial crop and land cover classification.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves a classification task.
What is the intended use of this model?	The intended use is crop and land cover classification from HLS remote sensing data.
What is the size of the final model in Mb?	The size of the final model in Mb is not specified in the documentation.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using standard supervised learning techniques with the mmsegmentation stack.
What is the claimed performance of this model?	The claimed performance is: overall accuracy 60.64%, mean IoU 0.4269, mean accuracy 64.06%, with class-wise IoU and accuracy reported in the results table.
Are the performance shown in the pretrained version improved in the finetuning?	Finetuning with multi-temporal data and CDL labels is claimed to improve generalization and performance over the pretrained version, as indicated in the documentation.