How many activities are present in the whole workflow?	3 activities are present in the workflow: DataPreparation, ModelFinetuning, and ModelEvaluation.
What is the final status of the workflow?	The workflow status is "Completed" with all activities marked as "success" or "finished".
What is the time to completion of the workflow?	The exact time to completion is not specified in the cards ("~" is used for duration fields).
List all the parameters of the first activity of the workflow	The first activity, DataPreparation, uses as parameters: USDA CDL 2022 (providing target class labels for 13 categories at 30m resolution) and HLS S30 scenes (2022) (three scenes per chip, early/mid/late season, reprojected to EPSG:5070).
What hardware was used in the workflow?	The specific hardware used is not provided in the cards (fields are marked "~").
Who is responsible for this workflow (person or username or entity)?	The workflow is attributed to the IBM/NASA team, with Dr. Hamed Alemohammad listed as a point of contact for the dataset.
What was the specific execution order of the tasks?	The execution order is: 1. DataPreparation, 2. ModelFinetuning, 3. ModelEvaluation.
List all parameters for all activites in the workflow	DataPreparation: USDA CDL 2022, HLS S30 scenes (2022). ModelFinetuning: ibm-nasa-geospatial/Prithvi-100M, ibm-nasa-geospatial/multi-temporal-crop-classification, multi_temporal_crop_classification.py. ModelEvaluation: Prithvi-100M-multi-temporal-crop-classification, validation split.
What was the peak RAM consumption during the workflow?	Peak RAM consumption is not specified in the cards ("~" is used for memory fields).
Has the model been trained in a distributed setting?	There is no information in the cards about distributed training.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Total GPU power consumption is not specified in the cards.
What significant input artifacts are involved in the generation of the finetuned model?	The significant input artifacts are: ibm-nasa-geospatial/Prithvi-100M (pretrained model weights) and ibm-nasa-geospatial/multi-temporal-crop-classification (3,854 GeoTIFF chips with 18 bands and masks).
What is the total energy use for completing the workflow?	Total energy use is not specified in the cards.
List all input files with size larger than 100Mb	The input files larger than 100Mb are: ibm-nasa-geospatial/Prithvi-100M (model weights) and ibm-nasa-geospatial/multi-temporal-crop-classification (dataset of 3,854 chips).
List all different file types used as input	Input file types include: GeoTIFF (.tif) for imagery and masks, Python scripts/configs (.py), and PyTorch model weights.
Identify the largest output	The largest output is the fine-tuned segmentation model: Prithvi-100M-multi-temporal-crop-classification.
What is the science domain of the dataset?	The science domain is remote sensing and geospatial crop/land cover classification.
Does the dataset have a predetermined train-test split?	Yes, the dataset is split 80% training and 20% validation, with splits recorded in train_data.txt and validation_data.txt.
How many samples are present in the whole dataset?	The dataset contains 3,854 chips (samples).
What is the data type of the ground truth (if present)?	The ground truth is a single-band GeoTIFF mask with integer values (class labels 0–13).
What is the specific task for which the dataset was created?	The dataset was created for multi-temporal crop and land cover segmentation/classification.
What is the size in byte of one sample?	The exact byte size per sample is not specified in the cards.
What is the total size of the whole dataset?	The total dataset size is not specified in bytes in the cards.
What are the designed uses for this model?	Designed uses include crop type and land cover classification across the contiguous United States using time-series HLS satellite imagery; also applicable to other geospatial segmentation tasks.
How many epochs have been used in the finetuning?	80 epochs were used for finetuning.
How many model parameters (weights) does the model have?	The model has 100 million parameters.
What is the science domain of the model?	The science domain is geospatial artificial intelligence, specifically remote sensing and crop/land cover classification.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves a classification (segmentation) task.
What is the intended use of this model?	The intended use is for multi-temporal crop and land cover classification from satellite imagery, and general geospatial segmentation tasks.
What is the size of the final model in Mb?	The exact size in Mb is not specified, but the model is described as having 100M parameters (typical ViT models of this size are several hundred MB).
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using standard supervised segmentation training with the mmsegmentation library.
What is the claimed performance of this model?	The model achieves mIoU: 0.4269, mAcc: 64.06%, aAcc: 60.64% on the validation set; per-class IoU ranges from 0.31 (Alfalfa) to 0.68 (Open Water).
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the finetuned model achieves task-specific segmentation/classification performance, which is an improvement over the generic pretraining (which was not directly evaluated for this task).