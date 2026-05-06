How many activities are present in the whole workflow?	The workflow includes at least the following activities: dataset creation (scene selection, chip generation, quality control), model pretraining, model finetuning, and inference/evaluation. Thus, there are at least four main activities.
What is the final status of the workflow?	The workflow is completed, as evidenced by the availability of the finetuned model, published results, and public inference/demo scripts.
What is the time to completion of the workflow?	The exact time to completion is not specified in the provided cards.
List all the parameters of the first activity of the workflow	The first activity, dataset creation, involves parameters such as: chip size (224x224 pixels), spatial resolution (30m), number of bands (6 bands per timestep, 3 timesteps), band order (Blue, Green, Red, NIR, SWIR 1, SWIR 2), time period (March–September 2022), cloud cover threshold (low cloud cover), projection (EPSG:5070), and quality control using Fmask.
What hardware was used in the workflow?	The specific hardware used is not mentioned in the provided cards.
Who is responsible for this workflow (person or username or entity)?	The workflow is attributed to the IBM and NASA team, with point of contact Dr. Hamed Alemohammad (halemohammad@clarku.edu), and authors listed in the citations.
What was the specific execution order of the tasks?	The execution order is: 1) Dataset creation (scene selection, chip generation, quality control), 2) Model pretraining on HLS data, 3) Model finetuning on the multi-temporal crop classification dataset, 4) Inference and evaluation.
List all parameters for all activites in the workflow	Dataset creation: chip size (224x224), spatial resolution (30m), bands (6 per timestep, 3 timesteps), band order, time period, cloud cover, projection, quality control. Pretraining: input shape (B, C, T, H, W), bands used, MAE loss, ViT architecture. Finetuning: epochs (80), config file, number of classes (13). Inference: input format (GeoTIFF, 18 bands), band order.
What was the peak RAM consumption during the workflow?	Peak RAM consumption is not specified in the provided cards.
Has the model been trained in a distributed setting?	There is no explicit mention of distributed training in the provided cards.
What was the total power consumption in Watts of the GPU(s) during the workflow?	Total power consumption is not specified in the provided cards.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts include the multi-temporal crop classification dataset (GeoTIFF chips with 18 bands and corresponding masks) and the pretrained Prithvi-100M model weights.
What is the total energy use for completing the workflow?	Total energy use is not specified in the provided cards.
List all input files with size larger than 100Mb	Input GeoTIFF files containing 224x224x18 bands of float data are likely larger than 100Mb, but specific file sizes are not provided.
List all different file types used as input	Input file types include GeoTIFF (.tif) for both imagery and masks, and text files (.txt) for train/validation splits.
Identify the largest output	The largest output is the finetuned Prithvi-100M multi-temporal crop classification model checkpoint.
What is the science domain of the dataset?	The science domain is remote sensing and geospatial analysis, specifically agricultural land cover and crop type classification.
Does the dataset have a predetermined train-test split?	Yes, the dataset is split into training (80%) and validation (20%) sets, with splits recorded in train_data.txt and validation_data.txt.
How many samples are present in the whole dataset?	The dataset contains 3,854 chips (samples).
What is the data type of the ground truth (if present)?	The ground truth is a single-band GeoTIFF mask with integer values representing class labels (0–13).
What is the specific task for which the dataset was created?	The dataset was created for semantic segmentation of crop and land cover types from multi-temporal satellite imagery.
What is the size in byte of one sample?	Exact size is not specified, but each sample is a 224x224x18 float32 array plus a 224x224 int mask. Rough estimate: (224*224*18*4) + (224*224*1) ≈ 3.6MB per sample.
What is the total size of the whole dataset?	Exact total size is not specified, but with 3,854 samples at ~3.6MB each, the dataset is roughly 13.9GB.
What are the designed uses for this model?	The model is designed for crop and land cover classification from multi-temporal remote sensing imagery, with applications in agriculture, environmental monitoring, and geospatial analysis.
How many epochs have been used in the finetuning?	Finetuning was performed for 80 epochs.
How many model parameters (weights) does the model have?	The model has 100 million parameters (Prithvi-100M).
What is the science domain of the model?	The science domain is geospatial artificial intelligence, remote sensing, and agricultural monitoring.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves a classification task (semantic segmentation of crop/land cover types).
What is the intended use of this model?	The intended use is for automated crop and land cover classification from satellite imagery, supporting agricultural and environmental applications.
What is the size of the final model in Mb?	The exact size is not specified, but a 100M parameter model is typically around 400MB (assuming float32 weights).
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	The model was finetuned using standard supervised learning with the mmsegmentation library and cross-entropy loss for segmentation.
What is the claimed performance of this model?	The model achieves a mean IoU (mIoU) of 0.4269, mean accuracy (mAcc) of 64.06%, and overall accuracy (aAcc) of 60.64% on the validation set.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, finetuning on the crop classification dataset adapts the pretrained model to the specific task, improving performance for crop and land cover segmentation compared to the generic pretrained version.