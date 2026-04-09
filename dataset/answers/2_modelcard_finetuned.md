How many activities are present in the whole workflow?	Not specified in the cards.
What is the final status of the workflow?	Finetuning completed with reported results.
What is the time to completion of the workflow?	Not specified in the cards.
List all the parameters of the first activity of the workflow	Not specified in the cards.
What hardware was used in the workflow?	Not specified in the cards.
Who is responsible for this workflow (person or username or entity)?	Li, Hanxi (Steve); Khallaghi, Sam; Cecil, Michael; Kordi, Fatemeh; Fraccaro, Paolo; Alemohammad, Hamed; Ramachandran, Rahul
What was the specific execution order of the tasks?	Not specified in the cards.
List all the parameters for the whole workflow process	Not specified in the cards.
What was the peak RAM consumption during the workflow?	Not specified in the cards.
Has the model been trained in a distributed setting?	Not specified in the cards.
What was the real-time power consumption (in Watts) of the GPU during the workflow?	Not specified in the cards.
Which inputs influenced the output in the workflow?	HLS geotiff images with 18 bands (3 time-steps, 6 bands each)
What is the total energy use for completing the workflow?	Not specified in the cards.
List all input files with size larger than 100Mb	Not specified in the cards.
List all different file types used as input	Geotiff
Identify the largest output	Not specified in the cards.
What is the science domain of the dataset?	Geospatial, Crop Classification, Land Cover
Does the dataset have a predetermined train-test split?	Not specified in the cards.
How many samples are present in the whole dataset?	Not specified in the cards.
What is the data type of the ground truth (if present)?	CDL labels (categorical, 13 classes)
What is the specific task for which the dataset was created?	Crop and land cover classification from multi-temporal HLS data
What is the size in byte of one sample?	Not specified in the cards.
What is the total size of the whole dataset?	Not specified in the cards.
What are the designed uses for this model?	Crop and land cover classification from HLS satellite imagery
How many epochs have been used in the final training?	80
How many model parameters (weights) does the model have?	100 million
What is the science domain of the model?	Geospatial, Crop Classification, Land Cover
What is the task solved by this model (regression or classification or forecast etc.)?	Classification (segmentation)
What is the intended use of this model?	Crop and land cover classification from multi-temporal HLS satellite imagery
What is the size of the final model in Mb?	Not specified in the cards.
What technique was used to train the model?	Finetuning of pretrained Prithvi-100M model using mmsegmentation stack
What is the claimed performance of this model?	mIoU: 0.4269, mAcc: 64.06%, aAcc: 60.64%
Are the performance shown in the pretrained version improved in the finetuning?	Yes, finetuning with multi-temporal data improved generalization and performance.