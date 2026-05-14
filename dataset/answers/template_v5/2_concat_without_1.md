How many activities are present in the whole workflow?	3
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	13h 48m 44s
List all the parameters of the first activity of the workflow	USDA CDL 2022 (target class labels), HLS S30 scenes (2022) (input imagery), three scenes per chip (early/mid/late season), reprojected to EPSG:5070, Fmask quality control, output: 3,854 GeoTIFF chips, 18-band input, 1-band mask, 80/20 train/validation split
What hardware was used in the workflow?	4× NVIDIA V100-SXM2-32GB GPUs, Intel Xeon E5-2686 v4 CPU, 244 GB RAM, AWS EC2 p3.8xlarge
Who is responsible for this workflow (person or username or entity)?	ibm-nasa-geospatial
What was the specific execution order of the tasks?	DataPreparation → ModelFinetuning → ModelEvaluation
List all parameters for all activites in the workflow	DataPreparation: USDA CDL 2022, HLS S30 scenes (2022), three scenes per chip, EPSG:5070 reprojection, Fmask QC, 3,854 chips, 18-band input, 1-band mask, 80/20 split; ModelFinetuning: Prithvi-100M pretrained model, multi-temporal crop classification dataset, mmsegmentation config, epochs=80, AdamW optimizer (β1=0.9, β2=0.999, weight_decay=0.05), learning rate=6e-5 (cosine schedule, 5 epoch warmup); ModelEvaluation: fine-tuned checkpoint, validation split, per-class IoU/Acc report
What was the peak RAM consumption during the workflow?	96 GB
Has the model been trained in a distributed setting?	No explicit mention of distributed training; training was performed on a single node with 4 GPUs.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Not reported
What significant input artifacts are involved in the generation of the finetuned model?	ibm-nasa-geospatial/Prithvi-100M (pretrained model weights), ibm-nasa-geospatial/multi-temporal-crop-classification (GeoTIFF chips dataset)
What is the total energy use for completing the workflow?	Not reported
List all input files with size larger than 100Mb	ibm-nasa-geospatial/multi-temporal-crop-classification (~14 GB), ibm-nasa-geospatial/Prithvi-100M (model weights, size not specified but implied >100 MB)
List all different file types used as input	GeoTIFF (.tif), PyTorch model weights (.pth or similar), configuration file (.py), text files (.txt for splits)
Identify the largest output	Prithvi-100M-multi-temporal-crop-classification (fine-tuned segmentation model checkpoint)
What is the science domain of the dataset?	Geospatial remote sensing, crop/land cover classification
Does the dataset have a predetermined train-test split?	Yes (80% train, 20% validation, splits in train_data.txt and validation_data.txt)
How many samples are present in the whole dataset?	3,854
What is the data type of the ground truth (if present)?	Single-band segmentation mask (GeoTIFF), integer class labels (0–13)
What is the specific task for which the dataset was created?	Multi-temporal crop and land cover segmentation/classification from satellite imagery
What is the size in byte of one sample?	Approximately 4.7 MB (14 GB / 2,974 train + 880 validation ≈ 3,854 samples)
What is the total size of the whole dataset?	~14 GB
What are the designed uses for this model?	Geospatial segmentation/classification tasks on remote sensing imagery, including crop type mapping, land cover classification, burn scar segmentation, flood mapping
How many epochs have been used in the finetuning?	80
How many model parameters (weights) does the model have?	100 million
What is the science domain of the model?	Geospatial artificial intelligence, remote sensing
What is the task solved by this model (regression or classification or forecast etc.)?	Classification (semantic segmentation)
What is the intended use of this model?	Segmentation and classification of crop types and land cover from multi-temporal satellite imagery
What is the size of the final model in Mb?	~380 MB (model checkpoint)
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Full fine-tuning using mmsegmentation with AdamW optimizer and cosine learning rate schedule
What is the claimed performance of this model?	mIoU: 0.4269, mAcc: 64.06%, aAcc: 60.64% (on validation split)
Are the performance shown in the pretrained version improved in the finetuning?	Yes; the pretrained model is self-supervised and not directly evaluated on segmentation, while the fine-tuned model achieves mIoU 0.4269 on the downstream task