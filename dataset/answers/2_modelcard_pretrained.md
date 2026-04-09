How many activities are present in the whole workflow?	Not specified in the cards.
What is the final status of the workflow?	Not specified in the cards.
What is the time to completion of the workflow?	Not specified in the cards.
List all the parameters of the first activity of the workflow	Not specified in the cards.
What hardware was used in the workflow?	Not specified in the cards.
Who is responsible for this workflow (person or username or entity)?	IBM and NASA team.
What was the specific execution order of the tasks?	Not specified in the cards.
List all the parameters for the whole workflow process	Not specified in the cards.
What was the peak RAM consumption during the workflow?	Not specified in the cards.
Has the model been trained in a distributed setting?	Not specified in the cards.
What was the real-time power consumption (in Watts) of the GPU during the workflow?	Not specified in the cards.
Which inputs influenced the output in the workflow?	Remote sensing data in video format (B, C, T, H, W) with 6 bands: Blue, Green, Red, Narrow NIR, SWIR 1, SWIR 2.
What is the total energy use for completing the workflow?	Not specified in the cards.
List all input files with size larger than 100Mb	Not specified in the cards.
List all different file types used as input	GeoTIFF (.tif)
Identify the largest output	Not specified in the cards.
What is the science domain of the dataset?	Geospatial / Remote Sensing
Does the dataset have a predetermined train-test split?	Not specified in the cards.
How many samples are present in the whole dataset?	Not specified in the cards.
What is the data type of the ground truth (if present)?	Not specified in the cards.
What is the specific task for which the dataset was created?	Pre-training for generalist geospatial AI tasks (e.g., segmentation, classification, flood mapping, burn scar detection, crop classification)
What is the size in byte of one sample?	Not specified in the cards.
What is the total size of the whole dataset?	Not specified in the cards.
What are the designed uses for this model?	Burn scars segmentation, Flood segmentation, Land cover classification, Multi-temporal crop classification, and other geospatial downstream tasks.
How many epochs have been used in the final training?	Not specified in the cards.
How many model parameters (weights) does the model have?	100 million (Prithvi-100M)
What is the science domain of the model?	Geospatial / Remote Sensing
What is the task solved by this model (regression or classification or forecast etc.)?	Self-supervised representation learning (pretraining); downstream tasks include segmentation and classification.
What is the intended use of this model?	Generalist geospatial AI for remote sensing time series analysis and downstream tasks.
What is the size of the final model in Mb?	Not specified in the cards.
What technique was used to train the model?	Masked AutoEncoder (MAE) with Vision Transformer (ViT) architecture and MSE loss.
What is the claimed performance of this model?	Not specified in the cards.
Are the performance shown in the pretrained version improved in the finetuning?	Finetuning examples are provided and intended to improve performance for specific tasks.