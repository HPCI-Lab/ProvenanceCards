How many activities are present in the whole workflow?	1
What is the final status of the workflow?	Success
What is the time to completion of the workflow?	11h 30m 00s
List all the parameters of the first activity of the workflow	Bands: 6, Timesteps: 3, Classes: 13, Image Size: 224x224
What hardware was used in the workflow?	4x NVIDIA A100-40GB
Who is responsible for this workflow (person or username or entity)?	Clark University / IBM / NASA
What was the specific execution order of the tasks?	crop-segmentation-train
List all the parameters for the whole workflow process	Bands: 6, Timesteps: 3, Classes: 13, Image Size: 224x224
What was the peak RAM consumption during the workflow?	answer not found
Has the model been trained in a distributed setting?	answer not found
What was the real-time power consumption (in Watts) of the GPU during the workflow?	answer not found
Which inputs influenced the output in the workflow?	foundation-model, training-dataset
What is the total energy use for completing the workflow?	answer not found
List all input files with size larger than 100Mb	answer not found
List all different file types used as input	Remote Sensing GeoTIFF Dataset
Identify the largest output	HLS Multi Temporal Crop Classification Model
What is the science domain of the dataset?	Geospatial / Remote Sensing
Does the dataset have a predetermined train-test split?	answer not found
How many samples are present in the whole dataset?	3,854
What is the data type of the ground truth (if present)?	CDL labels (Crop Data Layer), classified into 13 classes
What is the specific task for which the dataset was created?	Crop and land cover classification (segmentation)
What is the size in byte of one sample?	answer not found
What is the total size of the whole dataset?	answer not found
What are the designed uses for this model?	Crop and land cover classification from HLS data
How many epochs have been used in the final training?	80
How many model parameters (weights) does the model have?	100M
What is the science domain of the model?	Geospatial / Remote Sensing
What is the task solved by this model (regression or classification or forecast etc.)?	classification (segmentation)
What is the intended use of this model?	Crop and land cover classification from HLS data
What is the size of the final model in Mb?	answer not found
What technique was used to train the model?	Fine-Tuning (Segmentation) with Prithvi-100M backbone and U-Net/Segmentation head
What is the claimed performance of this model?	mIoU: 0.4269, aAcc: 60.64%, mAcc: 64.06%
Are the performance shown in the pretrained version improved in the finetuning?	answer not found