How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	13h 48m 44s
List all the parameters of the first activity of the workflow	USDA CDL 2022 (Crop Data Layer, 13 classes, 30m resolution), HLS S30 scenes (2022, 3 per chip, March–September, reprojected to EPSG:5070)
What hardware was used in the workflow?	4× NVIDIA V100-SXM2-32GB GPUs, Intel Xeon E5-2686 v4 CPU, 244 GB RAM, AWS EC2 p3.8xlarge
Who is responsible for this workflow (person or username or entity)?	ibm-nasa-geospatial
What was the specific execution order of the tasks?	DataPreparation → ModelFinetuning → ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: USDA CDL 2022, HLS S30 scenes (2022); ModelFinetuning: Prithvi-100M pretrained weights, multi-temporal-crop-classification dataset, multi_temporal_crop_classification.py config (epochs: 80, AdamW optimizer, lr: 6e-5, cosine schedule, warmup 5 epochs); ModelEvaluation: fine-tuned checkpoint, validation split
What was the peak RAM consumption during the workflow?	96 GB
Has the model been trained in a distributed setting?	No explicit mention of distributed training; training was performed on 4 GPUs on a single node (multi-GPU, single-node)
What was the total power consumption in Watts of the GPU(s) during the workflow?	Not reported
What significant input artifacts are involved in the generation of the finetuned model?	ibm-nasa-geospatial/Prithvi-100M (pretrained model weights), ibm-nasa-geospatial/multi-temporal-crop-classification (GeoTIFF chips dataset)
What is the total energy use for completing the workflow?	Not reported
List all input files with size larger than 100Mb	ibm-nasa-geospatial/Prithvi-100M (model weights, ~380 MB), ibm-nasa-geospatial/multi-temporal-crop-classification (GeoTIFF chips, ~14 GB)
List all different file types used as input	GeoTIFF (.tif), PyTorch model weights (.pth), Python config (.py), text files (.txt for splits)
Identify the largest output	Prithvi-100M-multi-temporal-crop-classification (fine-tuned segmentation model checkpoint, ~380 MB)
What is the science domain of the dataset?	Remote sensing, geospatial, agricultural monitoring
Does the dataset have a predetermined train-test split?	Yes, 80% train / 20% validation split, with splits recorded in train_data.txt and validation_data.txt
How many samples are present in the whole dataset?	3,854 chips
What is the data type of the ground truth (if present)?	Single-band GeoTIFF mask with integer values (0–13) representing land cover/crop classes
What is the specific task for which the dataset was created?	Semantic segmentation (crop and land cover classification) from multi-temporal satellite imagery
What is the size in byte of one sample?	Not explicitly stated; estimated at ~3.7 MB per chip (14 GB / 3,854)
What is the total size of the whole dataset?	~14 GB
What are the designed uses for this model?	Segmentation of crop types and land cover from multi-temporal satellite imagery; general geospatial downstream tasks (e.g., burn scar, flood, land cover classification)
How many epochs have been used in the finetuning?	80
How many model parameters (weights) does the model have?	100 million (100M)
What is the science domain of the model?	Remote sensing, geospatial artificial intelligence
What is the task solved by this model (regression or classification or forecast etc.)?	Classification (semantic segmentation)
What is the intended use of this model?	Geospatial segmentation/classification of crop and land cover types from satellite time series imagery
What is the size of the final model in Mb?	~380 MB
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Full model fine-tuning using mmsegmentation (no mention of LoRA or adapters)
What is the claimed performance of this model?	mIoU: 0.4269, mAcc: 64.06%, aAcc: 60.64% (per-class IoU up to 0.68 for Open Water)
Are the performance shown in the pretrained version improved in the finetuning?	Yes; the pretrained model is self-supervised (MAE reconstruction), while the fine-tuned model achieves supervised segmentation performance (mIoU 0.4269)