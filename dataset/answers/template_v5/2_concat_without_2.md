How many activities are present in the whole workflow?	The cards describe several activities: dataset creation (scene selection, chip generation, quality control), model pretraining, model finetuning, and inference. At least four main activities are present in the workflow.
What is the final status of the workflow?	The workflow is completed, as evidenced by the availability of the finetuned model, published results, and public inference/demo scripts.
What is the time to completion of the workflow?	The cards do not specify the total time to completion of the workflow.
List all the parameters of the first activity of the workflow	The first activity is dataset creation. Parameters include: selection of 5,000 chips based on USDA CDL samples, HLS S30 scenes between March and September 2022, low cloud cover filtering, three time steps (early, middle, late season), reprojection to EPSG:5070, chip size 224x224 pixels, 18 bands (6 bands x 3 time steps), and quality control using Fmask.
What hardware was used in the workflow?	The cards do not specify the hardware used in the workflow.
Who is responsible for this workflow (person or username or entity)?	Dr. Hamed Alemohammad (halemohammad@clarku.edu) is listed as the point of contact for the dataset; the IBM and NASA team are responsible for the model.
What was the specific execution order of the tasks?	The order is: 1) Dataset creation (scene selection, chip generation, quality control), 2) Model pretraining (Prithvi-100M on HLS data), 3) Model finetuning (on crop classification), 4) Inference and evaluation.
List all parameters for all activites in the workflow	Dataset creation: 5,000 chips, USDA CDL sampling, HLS S30 scenes (Mar–Sep 2022), low cloud cover, 3 time steps, EPSG:5070 reprojection, 224x224 pixels, 18 bands, Fmask quality control. Pretraining: HLS V2 L30, 6 bands, ViT-MAE, MSE loss, sequence length 3. Finetuning: 80 epochs, mmsegmentation stack, 13 classes. Inference: input 224x224x18 GeoTIFFs.
What was the peak RAM consumption during the workflow?	No information is provided about peak RAM consumption.
Has the model been trained in a distributed setting?	The cards do not specify if distributed training was used.
What was the total power consumption in Watts of the GPU(s) during the workflow?	No information is provided about GPU power consumption.
What significant input artifacts are involved in the generation of the finetuned model?	Significant input artifacts include the multi-temporal crop classification dataset (224x224x18 GeoTIFF chips with CDL labels) and the pretrained Prithvi-100M model weights.
What is the total energy use for completing the workflow?	No information is provided about total energy use.
List all input files with size larger than 100Mb	The dataset is available as .tgz archives and as GeoTIFF chips, but specific file sizes are not listed.
List all different file types used as input	.tgz (archive), .tif (GeoTIFF), .txt (split files), .png (distribution plots)
Identify the largest output	The largest output is the finetuned Prithvi-100M multi-temporal crop classification model.
What is the science domain of the dataset?	Remote sensing, geospatial analysis, crop classification, land cover mapping.
Does the dataset have a predetermined train-test split?	Yes, the dataset is split into training (80%) and validation (20%) sets, with splits recorded in .txt files.
How many samples are present in the whole dataset?	3,854 chips are present in the dataset.
What is the data type of the ground truth (if present)?	The ground truth is a single-band GeoTIFF mask with integer class labels (0–13).
What is the specific task for which the dataset was created?	The dataset was created for semantic segmentation (pixel-wise classification) of crop and land cover types.
What is the size in byte of one sample?	Each chip is 224x224x18 float32 (input) and 224x224x1 uint8 (mask). Input: 224*224*18*4 = 3,612,672 bytes (~3.45 MB). Mask: 224*224*1 = 50,176 bytes (~0.05 MB).
What is the total size of the whole dataset?	Not explicitly stated, but with 3,854 samples at ~3.5 MB each, the total is approximately 13.5 GB.
What are the designed uses for this model?	Designed uses include crop type and land cover segmentation, geospatial machine learning, and remote sensing applications.
How many epochs have been used in the finetuning?	80 epochs were used for finetuning.
How many model parameters (weights) does the model have?	The Prithvi-100M model has 100 million parameters.
What is the science domain of the model?	Remote sensing, geospatial artificial intelligence, earth observation.
What is the task solved by this model (regression or classification or forecast etc.)?	The model solves a classification task (semantic segmentation of crop/land cover types).
What is the intended use of this model?	Intended use is for geospatial image segmentation, crop classification, and land cover mapping from satellite imagery.
What is the size of the final model in Mb?	The exact size is not stated, but a 100M parameter model (float32) is about 400 MB.
What technique was used to fine-tune the model? (e.g. LoRa; GAN...)	Fine-tuning was performed using supervised learning with the mmsegmentation library.
What is the claimed performance of this model?	Mean IoU: 0.4269, mean accuracy: 64.06%, overall accuracy: 60.64%. Per-class IoU and accuracy are also reported.
Are the performance shown in the pretrained version improved in the finetuning?	Yes, finetuning on the crop classification dataset yields meaningful segmentation performance, which is not possible with the self-supervised pretrained model alone.