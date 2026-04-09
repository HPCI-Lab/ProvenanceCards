How many activities are present in the whole workflow?	answer not found
What is the final status of the workflow?	answer not found
What is the time to completion of the workflow?	answer not found
List all the parameters of the first activity of the workflow	answer not found
What hardware was used in the workflow?	answer not found
Who is responsible for this workflow (person or username or entity)?	Dr. Hamed Alemohammad (halemohammad@clarku.edu)
What was the specific execution order of the tasks?	answer not found
List all the parameters for the whole workflow process	answer not found
What was the peak RAM consumption during the workflow?	answer not found
Has the model been trained in a distributed setting?	answer not found
What was the real-time power consumption (in Watts) of the GPU during the workflow?	answer not found
Which inputs influenced the output in the workflow?	Temporal Harmonized Landsat-Sentinel imagery (18 bands: 6 bands x 3 time steps) in GeoTIFF format
What is the total energy use for completing the workflow?	answer not found
List all input files with size larger than 100Mb	answer not found
List all different file types used as input	GeoTIFF (.tif)
Identify the largest output	answer not found
What is the science domain of the dataset?	Geospatial remote sensing, crop classification
Does the dataset have a predetermined train-test split?	Yes (train_data.txt and validation_data.txt, 80%/20%)
How many samples are present in the whole dataset?	3,854 chips
What is the data type of the ground truth (if present)?	Single-band GeoTIFF mask with integer class values (0–13)
What is the specific task for which the dataset was created?	Segmentation/classification of crop and land cover types from satellite imagery
What is the size in byte of one sample?	answer not found
What is the total size of the whole dataset?	answer not found
What are the designed uses for this model?	Crop and land cover classification, segmentation, geospatial machine learning tasks using multi-temporal satellite imagery
How many epochs have been used in the final training?	80 epochs
How many model parameters (weights) does the model have?	100 million (100M)
What is the science domain of the model?	Geospatial artificial intelligence, remote sensing
What is the task solved by this model (regression or classification or forecast etc.)?	Classification (segmentation)
What is the intended use of this model?	Multi-temporal crop and land cover classification from satellite imagery
What is the size of the final model in Mb?	answer not found
What technique was used to train the model?	Masked AutoEncoder (MAE) with Vision Transformer (ViT) architecture, self-supervised pretraining, finetuning with mmsegmentation
What is the claimed performance of this model?	mIoU: 0.4269, mAcc: 64.06%, aAcc: 60.64% (see per-class results in card)
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the model is finetuned for improved crop classification performance on the target dataset