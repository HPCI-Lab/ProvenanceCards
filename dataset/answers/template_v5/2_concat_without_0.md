How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	~
List all the parameters of the first activity of the workflow	USDA CDL 2022, HLS S30 scenes (2022)
What hardware was used in the workflow?	~
Who is responsible for this workflow (person or username or entity)?	Dr. Hamed Alemohammad (halemohammad@clarku.edu)
What was the specific execution order of the tasks?	DataPreparation → ModelFinetuning → ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: USDA CDL 2022, HLS S30 scenes (2022); ModelFinetuning: ibm-nasa-geospatial/Prithvi-100M, ibm-nasa-geospatial/multi-temporal-crop-classification, multi_temporal_crop_classification.py; ModelEvaluation: Prithvi-100M-multi-temporal-crop-classification, validation split
What was the peak RAM consumption during the workflow?	~
Has the model been trained in a distributed setting?	Not specified
What was the total power consumption in Watts of the GPU(s) during the workflow?	~
What significant input artifacts are involved in the generation of the finetuned model?	ibm-nasa-geospatial/Prithvi-100M, ibm-nasa-geospatial/multi-temporal-crop-classification
What is the total energy use for completing the workflow?	~
List all input files with size larger than 100Mb	ibm-nasa-geospatial/Prithvi-100M, ibm-nasa-geospatial/multi-temporal-crop-classification
List all different file types used as input	GeoTIFF, PyTorch model weights, Python config (.py)
Identify the largest output	Prithvi-100M-multi-temporal-crop-classification (fine-tuned segmentation model checkpoint)
What is the science domain of the dataset?	Remote sensing, geospatial, agriculture
Does the dataset have a predetermined train-test split?	Yes (80% train, 20% validation)
How many samples are present in the whole dataset?	3,854 chips
What is the data type of the ground truth (if present)?	Single-band GeoTIFF mask with integer values (0–13)
What is the specific task for which the dataset was created?	Segmentation/classification of crop types and land cover from multi-temporal satellite imagery
What is the size in byte of one sample?	Not specified
What is the total size of the whole dataset?	Not specified
What are the designed uses for this model?	Crop and land cover classification from multi-temporal HLS satellite imagery
How many epochs have been used in the finetuning?	80
How many model parameters (weights) does the model have?	100M parameters
What is the science domain of the model?	Remote sensing, geospatial, agriculture
What is the task solved by this model (regression or classification or forecast etc.)?	Segmentation/classification
What is the intended use of this model?	Classifying crop types and land cover from multi-temporal satellite imagery
What is the size of the final model in Mb?	Not specified
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Standard supervised fine-tuning using mmsegmentation stack
What is the claimed performance of this model?	mIoU: 0.4269, mAcc: 64.06%, aAcc: 60.64%
Are the performance shown in the pretrained version improved in the finetuning?	Finetuning adapts the pretrained model for crop classification; performance metrics are reported for the finetuned model only.