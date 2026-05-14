How many activities are present in the whole workflow?	The dataset card does not specify the number of activities in the workflow.
What is the final status of the workflow?	The dataset card does not specify the final status of the workflow.
What is the time to completion of the workflow?	The dataset card does not specify the time to completion of the workflow.
List all the parameters of the first activity of the workflow	The dataset card does not specify parameters for any workflow activities.
What hardware was used in the workflow?	The dataset card does not specify the hardware used in the workflow.
Who is responsible for this workflow (person or username or entity)?	Dr. Hamed Alemohammad (halemohammad@clarku.edu) is the point of contact for the dataset.
What was the specific execution order of the tasks?	The dataset card describes the following order: 1) Chip selection from USDA CDL, 2) Querying HLS S30 scenes, 3) Selecting three scenes per chip, 4) Reprojecting to EPSG:5070, 5) Clipping and stacking bands, 6) Quality control and filtering.
List all parameters for all activites in the workflow	The dataset card does not specify parameters for workflow activities.
What was the peak RAM consumption during the workflow?	The dataset card does not specify peak RAM consumption.
Has the model been trained in a distributed setting?	The dataset card does not mention model training or distributed settings.
What was the total power consumption in Watts of the GPU(s) during the workflow?	The dataset card does not specify GPU power consumption.
What significant input artifacts are involved in the generation of the finetuned model?	The significant input artifacts are Harmonized Landsat-Sentinel (HLS) S30 satellite imagery and USDA Crop Data Layer (CDL) masks.
What is the total energy use for completing the workflow?	The dataset card does not specify total energy use.
List all input files with size larger than 100Mb	The dataset card does not list individual input files or their sizes.
List all different file types used as input	Input files are GeoTIFF (.tif) files for both satellite imagery and masks.
Identify the largest output	The dataset card does not specify the largest output.
What is the science domain of the dataset?	The science domain is remote sensing and geospatial crop classification.
Does the dataset have a predetermined train-test split?	Yes, the dataset is split into training (80%) and validation (20%) sets.
How many samples are present in the whole dataset?	There are 3,854 chips (samples) in the dataset.
What is the data type of the ground truth (if present)?	The ground truth is a single-band GeoTIFF mask with integer class values per pixel.
What is the specific task for which the dataset was created?	The dataset is designed for training segmentation models for crop and land cover classification.
What is the size in byte of one sample?	The dataset card does not specify the size in bytes of one sample.
What is the total size of the whole dataset?	The dataset card does not specify the total size of the dataset.
What are the designed uses for this model?	The dataset is intended for training geospatial machine learning models for crop and land cover segmentation.
How many epochs have been used in the finetuning?	The dataset card does not mention model training or number of epochs.
How many model parameters (weights) does the model have?	The dataset card does not mention any model or its parameters.
What is the science domain of the model?	The dataset card does not describe a specific model.
What is the task solved by this model (regression or classification or forecast etc.)?	The dataset is for segmentation (classification) tasks.
What is the intended use of this model?	The dataset is intended for training segmentation models for crop and land cover classification.
What is the size of the final model in Mb?	The dataset card does not mention any model or its size.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The dataset card does not mention any model fine-tuning technique.
What is the claimed performance of this model?	The dataset card does not mention any model or its performance.
Are the performance shown in the pretrained version improved in the finetuning?	The dataset card does not mention any pretrained or finetuned model performance.