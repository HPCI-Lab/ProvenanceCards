How many activities are present in the whole workflow?	There are three activities in the workflow: DataPreparation, ModelFinetuning, and ModelEvaluation.
What is the final status of the workflow?	The workflow status is "Completed" with all three activities marked as "success" or "finished".
What is the time to completion of the workflow?	The time to completion is not specified in the cards; all duration fields are marked as "~".
List all the parameters of the first activity of the workflow	The first activity, DataPreparation, uses as parameters: USDA CDL 2022 (target class labels), HLS S30 scenes (2022) (three scenes per chip, March–September, reprojected to EPSG:5070), and outputs 3,854 GeoTIFF chips (18-band input, 1-band mask), with an 80/20 train/validation split.
What hardware was used in the workflow?	The hardware used is not specified; fields for host_os and compute_hardware are marked as "~".
Who is responsible for this workflow (person or username or entity)?	The workflow is produced by IBM and NASA teams; the dataset point of contact is Dr. Hamed Alemohammad (halemohammad@clarku.edu).
What was the specific execution order of the tasks?	The execution order is: 1. DataPreparation, 2. ModelFinetuning, 3. ModelEvaluation.
List all parameters for all activites in the workflow	DataPreparation: USDA CDL 2022, HLS S30 scenes (2022), Fmask quality control, EPSG:5070 reprojection. ModelFinetuning: Prithvi-100M pretrained model, multi-temporal crop classification dataset, mmsegmentation config (multi_temporal_crop_classification.py), 80 epochs. ModelEvaluation: fine-tuned checkpoint, validation split.
What was the peak RAM consumption during the workflow?	Peak RAM consumption is not specified in the cards.
Has the model been trained in a distributed setting?	There is no information provided about distributed training in the cards.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Total GPU power consumption is not specified in the cards.
What significant input artifacts are involved in the generation of the finetuned model?	The significant input artifacts are: ibm-nasa-geospatial/Prithvi-100M (pretrained model) and ibm-nasa-geospatial/multi-temporal-crop-classification (3,854 GeoTIFF chips dataset).
What is the total energy use for completing the workflow?	Total energy use is not specified in the cards.
List all input files with size larger than 100Mb	The input dataset ibm-nasa-geospatial/multi-temporal-crop-classification (3,854 GeoTIFF chips) is larger than 100Mb; the Prithvi-100M model weights are also likely larger than 100Mb.
List all different file types used as input	Input file types include GeoTIFF (.tif) for imagery and masks, PyTorch model weights, and Python configuration files (.py).
Identify the largest output	The largest output is the fine-tuned segmentation model checkpoint: Prithvi-100M-multi-temporal-crop-classification.
What is the science domain of the dataset?	The science domain is remote sensing and geospatial crop/land cover classification.
Does the dataset have a predetermined train-test split?	Yes, the dataset is split 80% training and 20% validation, with splits recorded in train_data.txt and validation_data.txt.
How many samples are present in the whole dataset?	There are 3,854 samples (chips) in the dataset.
What is the data type of the ground truth (if present)?	The ground truth is a single-band GeoTIFF mask with integer values representing 13 classes.
What is the specific task for which the dataset was created?	The dataset was created for multi-temporal crop and land cover segmentation/classification.
What is the size in byte of one sample?	The exact byte size per sample is not specified in the cards.
What is the total size of the whole dataset?	The total dataset size is not specified in bytes, but it consists of 3,854 GeoTIFF chips (224×224 px, 18 bands) plus masks.
What are the designed uses for this model?	Designed uses include segmentation of crop types and land cover from time-series remote sensing imagery, e.g., burn scars, flood mapping, crop classification.
How many epochs have been used in the finetuning?	80 epochs were used in the fine-tuning process.
How many model parameters (weights) does the model have?	The model has 100 million parameters.
What is the science domain of the model?	The model's science domain is geospatial remote sensing and Earth observation.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves a classification (segmentation) task.
What is the intended use of this model?	The intended use is for geospatial segmentation/classification of land cover and crop types from multi-temporal satellite imagery.
What is the size of the final model in Mb?	The exact size in Mb is not specified, but the model is described as having 100M parameters (typical ViT models of this size are several hundred MB).
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using standard supervised segmentation training with mmsegmentation; no mention of LoRa, GAN, or other special techniques.
What is the claimed performance of this model?	The fine-tuned model achieves mIoU: 0.4269, mAcc: 64.06%, aAcc: 60.64% on the validation set.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the fine-tuned model achieves specific segmentation performance on the crop classification task; the pretrained model is not directly evaluated for this task, so fine-tuning provides improved, task-specific results.