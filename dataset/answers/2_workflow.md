How many activities are present in the whole workflow?	1
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	11h 30m 00s
List all the parameters of the first activity of the workflow	Bands: 6, Timesteps: 3, Classes: 13, Image Size: 224x224
What hardware was used in the workflow?	4x NVIDIA A100-40GB
Who is responsible for this workflow (person or username or entity)?	Clark University / IBM / NASA
What was the specific execution order of the tasks?	crop-segmentation-train
List all the parameters for the whole workflow process	Bands: 6, Timesteps: 3, Classes: 13, Image Size: 224x224
What was the peak RAM consumption during the workflow?	
Has the model been trained in a distributed setting?	
What was the real-time power consumption (in Watts) of the GPU during the workflow?	
Which inputs influenced the output in the workflow?	foundation-model, training-dataset
What is the total energy use for completing the workflow?	
List all input files with size larger than 100Mb	
List all different file types used as input	Temporal Vision Transformer (ViT), Remote Sensing GeoTIFF Dataset
Identify the largest output	HLS Multi Temporal Crop Classification Model
What is the science domain of the dataset?	Remote Sensing
Does the dataset have a predetermined train-test split?	
How many samples are present in the whole dataset?	3,854
What is the data type of the ground truth (if present)?	CDL labels (implied categorical raster)
What is the specific task for which the dataset was created?	Multi-temporal crop classification (segmentation)
What is the size in byte of one sample?	
What is the total size of the whole dataset?	
What are the designed uses for this model?	Crop type segmentation/classification on HLS data
How many epochs have been used in the final training?	
How many model parameters (weights) does the model have?	
What is the science domain of the model?	Remote Sensing
What is the task solved by this model (regression or classification or forecast etc.)?	Classification (segmentation)
What is the intended use of this model?	Crop type segmentation/classification on HLS data
What is the size of the final model in Mb?	
What technique was used to train the model?	Fine-Tuning (Segmentation)
What is the claimed performance of this model?	mIoU and Accuracy (refer to model card metrics section).
Are the performance shown in the pretrained version improved in the finetuning?	Convergence of training loss and IoU improvement over baseline.