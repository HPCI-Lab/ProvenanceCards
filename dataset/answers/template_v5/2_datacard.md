How many activities are present in the whole workflow?	The dataset card does not specify the number of activities in the workflow.
What is the final status of the workflow?	The dataset card does not specify the final status of the workflow.
What is the time to completion of the workflow?	The dataset card does not provide information about the time to completion of the workflow.
List all the parameters of the first activity of the workflow	The dataset card does not specify parameters for any activity in the workflow.
What hardware was used in the workflow?	The dataset card does not mention any hardware used in the workflow.
Who is responsible for this workflow (person or username or entity)?	Dr. Hamed Alemohammad (halemohammad@clarku.edu) is the point of contact for the dataset.
What was the specific execution order of the tasks?	The dataset card describes the following order: 1) Query and scene selection, 2) Chip generation, 3) Quality control and filtering.
List all parameters for all activites in the workflow	The dataset card does not specify parameters for activities in the workflow.
What was the peak RAM consumption during the workflow?	The dataset card does not provide information about peak RAM consumption.
Has the model been trained in a distributed setting?	The dataset card does not mention model training or distributed settings.
What was the total power consumption in Watts of the GPU(s) during the workflow?	The dataset card does not provide information about GPU power consumption.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts include Harmonized Landsat-Sentinel (HLS S30) imagery and USDA Crop Data Layer (CDL) masks.
What is the total energy use for completing the workflow?	The dataset card does not provide information about total energy use.
List all input files with size larger than 100Mb	The dataset card does not list individual input files or their sizes, but mentions data is available in .tgz format and as GeoTIFFs.
List all different file types used as input	Input file types include GeoTIFF (.tif) and compressed archive (.tgz).
Identify the largest output	The dataset card does not specify outputs other than the dataset itself; the largest output is likely the full dataset archive.
What is the science domain of the dataset?	The science domain is remote sensing and geospatial crop classification.
Does the dataset have a predetermined train-test split?	Yes, the dataset is split into training (80%) and validation (20%) sets, with splits recorded in train_data.txt and validation_data.txt.
How many samples are present in the whole dataset?	The dataset contains 3,854 chips (samples).
What is the data type of the ground truth (if present)?	The ground truth is a single-band mask with integer values representing classes.
What is the specific task for which the dataset was created?	The dataset was created for segmentation and classification of crop types and land cover from satellite imagery.
What is the size in byte of one sample?	The dataset card does not specify the size in bytes of one sample.
What is the total size of the whole dataset?	The dataset card does not specify the total size of the dataset.
What are the designed uses for this model?	The dataset is designed for training segmentation geospatial machine learning models for crop and land cover classification.
How many epochs have been used in the finetuning?	The dataset card does not mention model finetuning or number of epochs.
How many model parameters (weights) does the model have?	The dataset card does not mention any model or its parameters.
What is the science domain of the model?	The dataset card does not describe a specific model, but the domain is remote sensing and geospatial analysis.
What is the task solved by this model (regression or classification or forecast etc.)?	The dataset is intended for classification and segmentation tasks.
What is the intended use of this model?	The dataset is intended for training models to classify crop types and land cover from satellite imagery.
What is the size of the final model in Mb?	The dataset card does not mention any model or its size.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The dataset card does not mention any model finetuning technique.
What is the claimed performance of this model?	The dataset card does not provide any claimed model performance.
Are the performance shown in the pretrained version improved in the finetuning?	The dataset card does not mention pretrained or finetuned model performance.