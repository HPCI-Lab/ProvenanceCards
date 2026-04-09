How many activities are present in the whole workflow?	1
What is the final status of the workflow?	Success
What is the time to completion of the workflow?	11h 30m 00s
List all the parameters of the first activity of the workflow	Bands: 6, Timesteps: 3, Classes: 13, Image Size: 224x224
What hardware was used in the workflow?	4x NVIDIA A100-40GB
Who is responsible for this workflow (person or username or entity)?	michael-cecil
What was the specific execution order of the tasks?	crop-segmentation-train
List all the parameters for the whole workflow process	Bands: 6, Timesteps: 3, Classes: 13, Image Size: 224x224
What was the peak RAM consumption during the workflow?	
Has the model been trained in a distributed setting?	
What was the real-time power consumption (in Watts) of the GPU during the workflow?	
Which inputs influenced the output in the workflow?	Prithvi-EO-1.0-100M, hls-multi-temporal-crop-classification
What is the total energy use for completing the workflow?	
List all input files with size larger than 100Mb	
List all different file types used as input	Remote Sensing GeoTIFF Dataset
Identify the largest output	HLS Multi Temporal Crop Classification Model
What is the science domain of the dataset?	remote sensing
Does the dataset have a predetermined train-test split?	Yes
How many samples are present in the whole dataset?	3,854
What is the data type of the ground truth (if present)?	Single-band mask with integer class values (GeoTIFF)
What is the specific task for which the dataset was created?	Segmentation of crop and land cover types
What is the size in byte of one sample?	
What is the total size of the whole dataset?	
What are the designed uses for this model?	Crop and land cover classification from multi-temporal remote sensing imagery
How many epochs have been used in the final training?	80
How many model parameters (weights) does the model have?	100M
What is the science domain of the model?	Geospatial remote sensing
What is the task solved by this model (regression or classification or forecast etc.)?	Classification (segmentation)
What is the intended use of this model?	Crop and land cover classification from HLS satellite imagery
What is the size of the final model in Mb?	
What technique was used to train the model?	Fine-tuning of a temporal Vision Transformer (ViT) with segmentation head
What is the claimed performance of this model?	mIoU: 0.4269, aAcc: 60.64%, mAcc: 64.06%
Are the performance shown in the pretrained version improved in the finetuning?	Yes