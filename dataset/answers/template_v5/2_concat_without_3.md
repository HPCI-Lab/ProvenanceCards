How many activities are present in the whole workflow?	3 activities are present in the workflow: DataPreparation, ModelFinetuning, and ModelEvaluation.
What is the final status of the workflow?	The final status of the workflow is "Completed".
What is the time to completion of the workflow?	The workflow started at 2024-02-05T13:30:00Z and ended at 2024-02-06T03:18:44Z, for a total duration of 13 hours, 48 minutes, and 44 seconds.
List all the parameters of the first activity of the workflow	The first activity, DataPreparation, uses the following parameters: USDA CDL 2022 (Crop Data Layer for 13 classes at 30m resolution), HLS S30 scenes (2022) (three scenes per chip, March–September, reprojected to EPSG:5070).
What hardware was used in the workflow?	The workflow used 4× NVIDIA V100-SXM2-32GB GPUs, Intel Xeon E5-2686 v4 CPU, and 244 GB RAM on AWS EC2 p3.8xlarge.
Who is responsible for this workflow (person or username or entity)?	The responsible entity is "ibm-nasa-geospatial".
What was the specific execution order of the tasks?	The execution order was: 1. DataPreparation, 2. ModelFinetuning, 3. ModelEvaluation.
List all parameters for all activites in the workflow	DataPreparation: USDA CDL 2022, HLS S30 scenes (2022). ModelFinetuning: ibm-nasa-geospatial/Prithvi-100M, ibm-nasa-geospatial/multi-temporal-crop-classification, multi_temporal_crop_classification.py, epochs: 80, optimiser: AdamW (β1=0.9, β2=0.999, weight_decay=0.05), learning rate: 6e-5 (cosine schedule, linear warmup 5 epochs). ModelEvaluation: Prithvi-100M-multi-temporal-crop-classification, validation split.
What was the peak RAM consumption during the workflow?	Peak RAM usage was 96 GB during concurrent chip loading with prefetch workers=8 per GPU.
Has the model been trained in a distributed setting?	Yes, the model was trained on 4 GPUs (4× NVIDIA V100-SXM2-32GB), indicating distributed training.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Not specified in the cards; no information provided.
What significant input artifacts are involved in the generation of the finetuned model?	The significant input artifacts are: ibm-nasa-geospatial/Prithvi-100M (pretrained model weights) and ibm-nasa-geospatial/multi-temporal-crop-classification (3,854 GeoTIFF chips).
What is the total energy use for completing the workflow?	Not specified in the cards; no information provided.
List all input files with size larger than 100Mb	ibm-nasa-geospatial/Prithvi-100M (model weights, size: 100M parameters), ibm-nasa-geospatial/multi-temporal-crop-classification (3,854 GeoTIFF chips, ~14 GB).
List all different file types used as input	Input file types: GeoTIFF (.tif), PyTorch model weights, Python configuration file (.py), text files (train_data.txt, validation_data.txt).
Identify the largest output	The largest output is the fine-tuned segmentation model checkpoint: Prithvi-100M-multi-temporal-crop-classification (~380 MB).
What is the science domain of the dataset?	The science domain is remote sensing and geospatial crop/land cover classification.
Does the dataset have a predetermined train-test split?	Yes, the dataset is split 80% training and 20% validation, with splits recorded in train_data.txt and validation_data.txt.
How many samples are present in the whole dataset?	There are 3,854 samples (chips) in the dataset.
What is the data type of the ground truth (if present)?	The ground truth is a single-band GeoTIFF mask with integer values (class labels 0–13).
What is the specific task for which the dataset was created?	The dataset was created for segmentation/classification of crop types and land cover from multi-temporal satellite imagery.
What is the size in byte of one sample?	Not specified directly; cannot be determined exactly from the cards.
What is the total size of the whole dataset?	The total size is approximately 14 GB for the 3,854 GeoTIFF chips.
What are the designed uses for this model?	The model is designed for segmentation/classification of crop types and land cover across the contiguous United States using multi-temporal HLS satellite imagery.
How many epochs have been used in the finetuning?	80 epochs were used in the finetuning.
How many model parameters (weights) does the model have?	The model has 100 million parameters.
What is the science domain of the model?	The science domain is remote sensing/geospatial machine learning for crop and land cover classification.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves a classification/segmentation task.
What is the intended use of this model?	The intended use is to classify crop types and land cover from multi-temporal satellite imagery for geospatial analysis.
What is the size of the final model in Mb?	The final model checkpoint is approximately 380 MB.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was fine-tuned using standard supervised learning with the mmsegmentation stack and AdamW optimizer.
What is the claimed performance of this model?	The model achieves mIoU: 0.4269, mAcc: 64.06%, aAcc: 60.64% on the validation set.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, the model was pretrained with MAE/MSE loss and then fine-tuned for segmentation/classification, resulting in the reported performance metrics.