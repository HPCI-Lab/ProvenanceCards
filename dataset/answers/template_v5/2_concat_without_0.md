How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	13h 48m 44s
List all the parameters of the first activity of the workflow	USDA CDL 2022; HLS S30 scenes (2022)
What hardware was used in the workflow?	4× NVIDIA V100-SXM2-32GB GPUs, Intel Xeon E5-2686 v4 CPU, 244 GB RAM, AWS EC2 p3.8xlarge
Who is responsible for this workflow (person or username or entity)?	ibm-nasa-geospatial
What was the specific execution order of the tasks?	DataPreparation → ModelFinetuning → ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: USDA CDL 2022, HLS S30 scenes (2022); ModelFinetuning: Prithvi-100M, multi-temporal-crop-classification, multi_temporal_crop_classification.py; ModelEvaluation: Prithvi-100M-multi-temporal-crop-classification, validation split
What was the peak RAM consumption during the workflow?	96 GB
Has the model been trained in a distributed setting?	Yes, training used 4 GPUs in parallel
What was the total power consumption in Watts of the GPU(s) during the workflow?	Not specified in the cards
What significant input artifacts are involved in the generation of the finetuned model?	ibm-nasa-geospatial/Prithvi-100M; ibm-nasa-geospatial/multi-temporal-crop-classification
What is the total energy use for completing the workflow?	Not specified in the cards
List all input files with size larger than 100Mb	ibm-nasa-geospatial/Prithvi-100M (model weights); ibm-nasa-geospatial/multi-temporal-crop-classification (3,854 GeoTIFF chips, ~14 GB)
List all different file types used as input	GeoTIFF, PyTorch model weights, Python config file
Identify the largest output	Prithvi-100M-multi-temporal-crop-classification (fine-tuned segmentation model checkpoint)
What is the science domain of the dataset?	Geospatial, Remote Sensing, Agriculture
Does the dataset have a predetermined train-test split?	Yes, 80/20 train/validation split
How many samples are present in the whole dataset?	3,854 chips
What is the data type of the ground truth (if present)?	Segmentation mask (13-class, CDL-derived)
What is the specific task for which the dataset was created?	Multi-temporal crop and land cover classification (segmentation)
What is the size in byte of one sample?	Approximately 3.6 MB per chip (14 GB / 3,854 chips)
What is the total size of the whole dataset?	~14 GB
What are the designed uses for this model?	Segmentation/classification of crop types and land cover from multi-temporal satellite imagery; downstream geospatial tasks (burn scars, flood mapping, land cover)
How many epochs have been used in the finetuning?	80
How many model parameters (weights) does the model have?	100 million
What is the science domain of the model?	Geospatial, Remote Sensing, Earth Observation
What is the task solved by this model (regression or classification or forecast etc.)?	Classification (segmentation)
What is the intended use of this model?	Generalist geospatial segmentation/classification from multi-temporal satellite imagery
What is the size of the final model in Mb?	~380 MB
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Standard supervised fine-tuning using mmsegmentation (AdamW optimizer, cosine schedule)
What is the claimed performance of this model?	mIoU: 0.4269, mAcc: 64.06%, aAcc: 60.64% (on 13 classes)
Are the performance shown in the pretrained version improved in the finetuning?	Yes, finetuning adapts the pretrained model for crop classification, achieving specific segmentation metrics not present in the pretraining stage