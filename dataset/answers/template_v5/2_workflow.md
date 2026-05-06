How many activities are present in the whole workflow?	3 activities are present in the workflow: DataPreparation, ModelFinetuning, and ModelEvaluation.
What is the final status of the workflow?	The workflow status is "Completed".
What is the time to completion of the workflow?	The time to completion is not specified in the cards (fields are marked as ~).
List all the parameters of the first activity of the workflow	The first activity, DataPreparation, uses the following parameters: USDA CDL 2022 (providing target class labels for 13 land-cover/crop categories at 30m resolution across the CONUS) and HLS S30 scenes (2022) (Harmonised Landsat-Sentinel scenes from March–September 2022, three scenes per chip, reprojected to EPSG:5070).
What hardware was used in the workflow?	The hardware used is not specified in the cards (fields are marked as ~).
Who is responsible for this workflow (person or username or entity)?	The responsible user or entity is not specified in the cards (fields are marked as ~).
What was the specific execution order of the tasks?	The execution order is: 1. DataPreparation, 2. ModelFinetuning, 3. ModelEvaluation.
List all parameters for all activites in the workflow	DataPreparation: USDA CDL 2022, HLS S30 scenes (2022). ModelFinetuning: ibm-nasa-geospatial/Prithvi-100M, ibm-nasa-geospatial/multi-temporal-crop-classification, multi_temporal_crop_classification.py. ModelEvaluation: Prithvi-100M-multi-temporal-crop-classification, validation split.
What was the peak RAM consumption during the workflow?	Peak RAM consumption is not specified in the cards (fields are marked as ~).
Has the model been trained in a distributed setting?	There is no information in the cards indicating distributed training.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Total GPU power consumption is not specified in the cards (fields are marked as ~).
What significant input artifacts are involved in the generation of the finetuned model?	The significant input artifacts are: ibm-nasa-geospatial/Prithvi-100M (pretrained temporal ViT encoder) and ibm-nasa-geospatial/multi-temporal-crop-classification (3,854 GeoTIFF chips dataset).
What is the total energy use for completing the workflow?	Total energy use is not specified in the cards (fields are marked as ~).
List all input files with size larger than 100Mb	The dataset ibm-nasa-geospatial/multi-temporal-crop-classification (3,854 GeoTIFF chips) and the model weights ibm-nasa-geospatial/Prithvi-100M (100M parameters) are both likely larger than 100Mb.
List all different file types used as input	Input file types include GeoTIFF (for chips), PyTorch model weights, and Python configuration files (.py).
Identify the largest output	The largest output is the fine-tuned segmentation model checkpoint: Prithvi-100M-multi-temporal-crop-classification.
What is the science domain of the dataset?	The science domain is geospatial/remote sensing for crop and land cover classification.
Does the dataset have a predetermined train-test split?	Yes, the dataset is split 80/20 into train and validation sets.
How many samples are present in the whole dataset?	There are 3,854 samples (chips) in the dataset.
What is the data type of the ground truth (if present)?	The ground truth is a 13-class CDL-derived segmentation mask (categorical raster).
What is the specific task for which the dataset was created?	The dataset was created for multi-temporal crop and land cover classification (segmentation).
What is the size in byte of one sample?	The exact size in bytes of one sample is not specified in the cards.
What is the total size of the whole dataset?	The total size of the dataset is not specified in the cards.
What are the designed uses for this model?	The model is designed for classifying crop types and land cover across the contiguous United States using time-series HLS satellite imagery.
How many epochs have been used in the finetuning?	80 epochs were used in the fine-tuning.
How many model parameters (weights) does the model have?	The model has 100 million parameters.
What is the science domain of the model?	The science domain is geospatial/remote sensing.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves a classification (segmentation) task.
What is the intended use of this model?	The intended use is for geospatial segmentation of crop and land cover types from satellite imagery.
What is the size of the final model in Mb?	The size in Mb of the final model is not specified in the cards.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using the mmsegmentation stack (standard supervised fine-tuning).
What is the claimed performance of this model?	The model achieves mIoU: 0.4269, mAcc: 64.06%, aAcc: 60.64% on the validation set.
Are the performance shown in the pretrained version improved in the finetuning?	The cards do not provide pretrained model performance, so improvement cannot be determined from the provided information.