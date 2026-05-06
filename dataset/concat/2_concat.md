---
license: apache-2.0
tags:
- Pytorch
- Geospatial
- Temporal ViT
- Vit
---

### Model and Inputs
Prithvi-EO-1.0 is a first-of-its-kind temporal Vision transformer pre-trained by the IBM and NASA team on contiguous US Harmonised Landsat Sentinel 2 (HLS) data. The model adopts a self-supervised encoder developed with a ViT architecture and Masked AutoEncoder (MAE) learning strategy, with an MSE loss function. The model includes spatial attention across multiple patches and also temporal attention for each patch.

![](GFM.png)

The model accepts remote sensing data in a video format (B, C, T, H, W). Note that the temporal dimension (T) is very important in this application and not present in most other works around remote sensing modeling. The ability to handle a time series of remote sensing images can benefit a variety of downstream tasks (e.g. Burn Scars segmentation, Flood Segmentation, Land Cover Classification). The model can also handle static imagery which can be fed into the model with T=1.

### Pre-training
The model was pre-trained with NASA's HLS V2 L30 product (30m granularity) from the contiguous United States. The bands that were used are the following:

1.  Blue
2.  Green
3.  Red
4.  Narrow NIR
5.  SWIR 1
6.  SWIR 2

### Code
The model follows the [original MAE repo](https://github.com/facebookresearch/mae) with some modifications including:

1. replace 2D patch embed with 3D patch embed;
2. replace 2D positional embed with 3D positional embed;
3. replace 2D patchify and unpatchify with 3D.
4. adding infrared bands besides RGB

### Inference and demo
There is an inference script (`inference.py`) that allows to run the image reconstruction on a set of HLS images assumed to be from the same location at different time steps(see example below). These should be provided in chronological order in geotiff format, including the channels described above (Blue, Green, Red, Narrow NIR, SWIR 1, SWIR 2) in reflectance units. There is also a **demo** that leverages the same code [here](https://huggingface.co/spaces/ibm-nasa-geospatial/Prithvi-EO-1.0-demo).

```
python inference.py --data_files t1.tif t2.tif t3.tif --input_indices <optional, space separated 0-based indices of the six Prithvi channels in your input>
```

This demo is a starting point that can be used as a starting point to generalize to different input shapes / types.

### Finetuning examples
Examples of finetuning the model for image segmentation using the mmsegmentation library are available through Hugging Face (e.g. [burn scars segmentation](https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M-burn-scar), [flood mapping](https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M-sen1floods11), and [multi temporal crop classification](https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M-multi-temporal-crop-classification)), with the code used for the experiments available on [github](https://github.com/NASA-IMPACT/hls-foundation-os/tree/main/fine-tuning-examples). This also contains instructions to finetune the model for flood detection on the popular open access [sen1floods11 dataset](https://github.com/cloudtostreet/Sen1Floods11).

### Feedback

Your feedback is invaluable to us. If you have any feedback about the model, please feel free to share it with us. You can do this by submitting issues on our open-source repository, [hls-foundation-os](https://github.com/NASA-IMPACT/hls-foundation-os/issues), on GitHub.

### Citation

If this model helped your research, please cite `Prithvi-100M` in your publications. Here are two BibTeX entries as examples:

```
@article{Prithvi-100M-preprint,
    author          = {Jakubik, Johannes and Roy, Sujit and Phillips, C. E. and Fraccaro, Paolo and Godwin, Denys and Zadrozny, Bianca and Szwarcman, Daniela and Gomes, Carlos and Nyirjesy, Gabby and Edwards, Blair and Kimura, Daiki and Simumba, Naomi and Chu, Linsong and Mukkavilli, S. Karthik and Lambhate, Devyani and Das, Kamal and Bangalore, Ranjini and Oliveira, Dario and Muszynski, Michal and Ankur, Kumar and Ramasubramanian, Muthukumaran and Gurung, Iksha and Khallaghi, Sam and Li, Hanxi (Steve) and Cecil, Michael and Ahmadi, Maryam and Kordi, Fatemeh and Alemohammad, Hamed and Maskey, Manil and Ganti, Raghu and Weldemariam, Kommy and Ramachandran, Rahul},
    month           = oct,
    title           = {{Foundation Models for Generalist Geospatial Artificial Intelligence}},
    journal         = {Preprint Available on arxiv:2310.18660},
    year            = {2023}
}

@misc{Prithvi-100M,
    author          = {Jakubik, Johannes and Chu, Linsong and Fraccaro, Paolo and Gomes, Carlos and Nyirjesy, Gabby and Bangalore, Ranjini and Lambhate, Devyani and Das, Kamal and Oliveira Borges, Dario and Kimura, Daiki and Simumba, Naomi and Szwarcman, Daniela and Muszynski, Michal and Weldemariam, Kommy and Zadrozny, Bianca and Ganti, Raghu and Costa, Carlos and Edwards, Blair & Watson, Campbell and Mukkavilli, Karthik and Schmude, Johannes & Hamann, Hendrik and Robert, Parkin and Roy, Sujit and Phillips, Christopher and Ankur, Kumar and Ramasubramanian, Muthukumaran and Gurung, Iksha and Leong, Wei Ji and Avery, Ryan and Ramachandran, Rahul and Maskey, Manil and Olofossen, Pontus and Fancher, Elizabeth and Lee, Tsengdar and Murphy, Kevin and Duffy, Dan and Little, Mike and Alemohammad, Hamed and Cecil, Michael and Li, Steve and Khallaghi, Sam and Godwin, Denys and Ahmadi, Maryam and Kordi, Fatemeh and Saux, Bertrand and Pastick, Neal and Doucette, Peter and Fleckenstein, Rylie and Luanga, Dalton and Corvin, Alex and Granger, Erwan},
    doi             = {10.57967/hf/0952},
    month           = aug,
    title           = {{Prithvi-100M}},
    repository-code = {https://github.com/NASA-IMPACT/hls-foundation-os},
    year            = {2023}
}
```

---
license: apache-2.0
language:
- en
tags:
- Pytorch
- mmsegmentation
- segmentation
- Crop Classification
- Multi Temporal
- Geospatial
- Foundation model
datasets:
- ibm-nasa-geospatial/multi-temporal-crop-classification
metrics:
- accuracy
- IoU
library_name: terratorch
pipeline_tag: image-segmentation
---
### Model and Inputs
The pretrained [Prithvi-EO-1.0-100M](https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M/blob/main/README.md) parameter model is finetuned to classify crop and other land cover types based off HLS data and CDL labels from the [multi_temporal_crop_classification dataset](https://huggingface.co/datasets/ibm-nasa-geospatial/multi-temporal-crop-classification). 

This dataset includes input chips of 224x224x18, where 224 is the height and width and 18 is combined with 6 bands of 3 time-steps. The bands are:
 
1. Blue
2. Green
3. Red
4. Narrow NIR
5. SWIR 1
6. SWIR 2

Labels are from CDL(Crop Data Layer) and classified into 13 classes.

![](multi_temporal_crop_classification.png)

The Prithvi-100m model was initially pretrained using a sequence length of 3 timesteps. For this task, we leverage the capacity for multi-temporal data input, which has been integrated from the foundational pretrained model. This adaptation allows us to achieve more generalized finetuning outcomes.

### Code
Code for Finetuning is available through [github](https://github.com/NASA-IMPACT/hls-foundation-os/)

Configuration used for finetuning is available through [config](https://github.com/NASA-IMPACT/hls-foundation-os/blob/main/configs/multi_temporal_crop_classification.py).

### Results
The experiment by running the mmseg stack for 80 epochs using the above config led to the following result:

|     **Classes**    | **IoU**| **Acc**|
|:------------------:|:------:|:------:|
| Natural Vegetation | 0.4038 | 46.89% |
|       Forest       | 0.4747 | 66.38% |
|        Corn        | 0.5491 | 65.47% |
|      Soybeans      | 0.5297 | 67.46% |
|      Wetlands      | 0.402  | 58.91% |
|  Developed/Barren  | 0.3611 | 56.49% |
|     Open Water     | 0.6804 | 90.37% |
|    Winter Wheat    | 0.4967 | 67.16% |
|       Alfalfa      | 0.3084 | 66.75% |
|Fallow/Idle Cropland| 0.3493 | 59.23% |
|       Cotton       | 0.3237 | 66.94% |
|       Sorghum      | 0.3283 | 73.56% |
|        Other       | 0.3427 | 47.12% |

|**aAcc**|**mIoU**|**mAcc**|
|:------:|:------:|:------:|
| 60.64% | 0.4269 | 64.06% |

It is important to acknowledge that the CDL (Crop Data Layer) labels employed in this process are known to contain noise and are not entirely precise, thereby influencing the model's performance. Fine-tuning the model with more accurate labels is expected to further enhance its overall effectiveness, leading to improved results.

### Baseline
The baseline model along with its results can be accessed [here](https://github.com/ClarkCGA/multi-temporal-crop-classification-baseline).

### Inference
The github repo includes an inference script that allows to run the hls-cdl crop classification model for inference on HLS images. These input have to be geotiff format, including 18 bands for 3 time-step, and each time-step includes the channels described above (Blue, Green, Red, Narrow NIR, SWIR, SWIR 2) in order. There is also a **demo** that leverages the same code **[here](https://huggingface.co/spaces/ibm-nasa-geospatial/Prithvi-100M-multi-temporal-crop-classification-demo)**.

### Feedback

Your feedback is invaluable to us. If you have any feedback about the model, please feel free to share it with us. You can do this by submitting issues on our open-source repository, [hls-foundation-os](https://github.com/NASA-IMPACT/hls-foundation-os/issues), on GitHub.

## Citation

If this model helped your research, please cite `HLS Multi Temporal Crop Classification Model` in your publications. Here is an example BibTeX entry:

```
@misc{hls-multi-temporal-crop-classification-model,
    author = {Li, Hanxi (Steve) and Khallaghi, Sam and Cecil, Michael and Kordi, Fatemeh and Fraccaro, Paolo and Alemohammad, Hamed and Ramachandran, Rahul},
    doi    = { 10.57967/hf/0954 },
    month  = aug,
    title  = {{HLS Multi Temporal Crop Classification Model}},
    url    = {https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M-multi-temporal-crop-classification},
    year   = {2023}
}
```
---
license: cc-by-4.0
language:
- en
tags:
- remote sensing
- segmentation
- crop type
- foundation model
size_categories:
- 1K<n<10K
---


# Dataset Card for Multi-Temporal Crop Classification

## Dataset Description

- **Homepage: https://huggingface.co/datasets/ibm-nasa-geospatial/cdl-crops/**
- **Point of Contact: Dr. Hamed Alemohammad (halemohammad@clarku.edu)** 

### Dataset Summary

This dataset contains temporal Harmonized Landsat-Sentinel imagery of diverse land cover and crop type classes across the Contiguous United States for the year 2022. The target labels are derived from USDA's Crop Data Layer (CDL). It's primary purpose is for training segmentation geospatial machine learning models.

### Dataset Structure


## TIFF Files
Each tiff file covers a 224 x 224 pixel area at 30m spatial resolution. Each input satellite file contains 18 bands including 6 spectral bands for three time steps stacked together. Each GeoTIFF file for the mask contains one band with the target classes for each pixel. 

## Band Order
In each input GeoTIFF the following bands are repeated three times for three observations throughout the growing season:
Channel, Name, HLS S30 Band number  
1, Blue,  B02  
2, Green, B03  
3, Red,   B04  
4, NIR,   B8A  
5, SW 1,  B11  
6, SW 2,  B12  

Masks are a single band with values:  
0   :   "No Data"
1	:	"Natural Vegetation"
2	:	"Forest"
3	:	"Corn"
4	:	"Soybeans"
5	:	"Wetlands"
6	:	"Developed/Barren"
7	:	"Open Water"
8	:	"Winter Wheat"
9	:	"Alfalfa"
10	:	"Fallow/Idle Cropland"
11	:	"Cotton"
12	:	"Sorghum"
13	:	"Other"	 

## Class Distribution
### Training Data Distribution
![Training Data](training_dst.png)

### Validation Data Distribution
![Validation Data](validation_dst.png)

## Data Splits
The 3,854 chips have been randomly split into training (80%) and validation (20%) with corresponding ids recorded in cvs files `train_data.txt` and `validation_data.txt`.

## Dataset Creation
### Query and Scene Selection
First, a set of 5,000 chips were defined based on samples from the USDA CDL to ensure a representative sampling across the CONUS. Next, for each chip, the corresponding HLS S30 scenes between March and September 2022 were queried, and scenes with low cloud cover were retrieved. Then, three scenes are selected among the low cloudy scenes to ensure a scene from early in the season, one in the middle, and one toward the end. The three final scenes were then reprojected to CDL's projection grid (`EPSG:5070`) using bilinear interpolation. 

### Chip Generation
In the final step, the three scenes for each chip were clipped to the bounding box of the chip, and 18 spectral bands were stacked together. In addition, a quality control was applied to each chip using the `Fmask` layer of the HLS dataset. Any chip containing clouds, cloud shadow, adjacent to cloud or missing values were discarded. This resulted in 3,854 chips.

### Dataset Download
You can download the data in `.tgz` format from this repository (you need to install [Git Large File Sotrage](https://git-lfs.com/) for this). The same version of the data is hosted on [Source Cooperative](https://beta.source.coop/repositories/clarkcga/multi-temporal-crop-classification/description) as objects on AWS S3. 

### Citation

If this dataset helped your research, please cite `hls-multi-temporal-crop-classification` in your publications. Here is an example BibTeX entry:

```
@misc{hls-multi-temporal-crop-classification,
    author = {Cecil, Michael and Kordi, Fatemehand Li, Hanxi (Steve) and Khallaghi, Sam and Alemohammad, Hamed},
    doi    = {10.57967/hf/0955},
    month  = aug,
    title  = {{HLS Multi Temporal Crop Classification}},
    url    = {https://huggingface.co/ibm-nasa-geospatial/multi-temporal-crop-classification},
    year   = {2023}
}
```
# Workflow Card: Use Case 2 — Multi-Temporal Crop Classification Fine-Tuning

---

## 1. Workflow

- **name**: prithvi_crop_classification_finetuning
- **description**: End-to-end ML workflow that fine-tunes the IBM/NASA Prithvi-EO-1.0-100M geospatial foundation model on the HLS Multi-Temporal Crop Classification dataset to produce a segmentation model capable of classifying crop types and land cover across the contiguous United States using time-series Harmonised Landsat-Sentinel (HLS) satellite imagery.

---

## 2. Summary

- **execution_id**: prithvi_crop_classification_finetuning_v0
- **version**: 0
- **started_at**: ~
- **ended_at**: ~
- **duration**: ~
- **status**: Completed
- **location**: ~
- **user**: ~
- **entrypoint.repository**: https://github.com/NASA-IMPACT/hls-foundation-os
- **entrypoint.branch**: main
- **entrypoint.short_sha**: ~

---

## 3. Infrastructure

- **host_os**: ~
- **compute_hardware**: ~
- **runtime_environment**: ~
- **resource_manager**: ~
- **primary_software**: Python, PyTorch, mmsegmentation, terratorch; Hugging Face Transformers
- **environment_snapshot**: https://github.com/NASA-IMPACT/hls-foundation-os/blob/main/configs/multi_temporal_crop_classification.py

---

## 4. Overview

### 4.1 Run Summary

- **total_activities**: 3
- **status_counts**: finished: 3
- **arguments**: epochs: 80, optimiser: ~, learning rate: ~

**Notable Inputs:**
  - `ibm-nasa-geospatial/multi-temporal-crop-classification` — format: GeoTIFF chips (224×224 px, 18 bands, 30m resolution), size: 3 854 chips split 80/20 train/validation, source: https://huggingface.co/datasets/ibm-nasa-geospatial/cdl-crops/
  - `ibm-nasa-geospatial/Prithvi-100M` — format: PyTorch model weights, size: 100M parameters, source: https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M

**Notable Outputs:**
  - `Prithvi-100M-multi-temporal-crop-classification` — type: fine-tuned segmentation model, location: https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M-multi-temporal-crop-classification

**Structure (activity DAG):**
  1. DataPreparation
  2. ModelFinetuning
  3. ModelEvaluation

- **observations**: CDL (Crop Data Layer) labels are known to contain noise, which influences model performance. Fine-tuning with more accurate labels is expected to further improve results. Class imbalance is present (e.g., Open Water achieves highest IoU at 0.68 vs Alfalfa at 0.31). The model also handles static imagery via T=1.

### 4.2 Resource Usage

- **cpu**: ~
- **memory**: ~
- **gpu**: ~
- **disk**: ~
- **network**: ~

---

## 5. Activities

#### Activity: `DataPreparation`

- **name**: DataPreparation
- **task_count**: 1
- **started_at**: ~
- **ended_at**: ~
- **duration**: ~
- **status**: success: 1
  - **hosts**: ~
  - **inputs**:
    - `USDA CDL 2022` — USDA Crop Data Layer providing target class labels for 13 land-cover/crop categories at 30m resolution across the CONUS
    - `HLS S30 scenes (2022)` — Harmonised Landsat-Sentinel scenes (March–September 2022) retrieved for each chip location; three scenes per chip (early/mid/late season); reprojected to EPSG:5070
  - **outputs**:
    - `ibm-nasa-geospatial/multi-temporal-crop-classification` — 3 854 GeoTIFF chips (post quality control with Fmask); 18-band input (6 spectral bands × 3 time steps) + 1-band CDL-derived mask; 80/20 train/validation split recorded in train_data.txt / validation_data.txt

#### Activity: `ModelFinetuning`

- **name**: ModelFinetuning
- **task_count**: 1
- **started_at**: ~
- **ended_at**: ~
- **duration**: ~
- **status**: success: 1
  - **hosts**: ~
  - **inputs**:
    - `ibm-nasa-geospatial/Prithvi-100M` — pretrained temporal ViT encoder (MAE, MSE loss) trained on contiguous US HLS V2 L30 data; 100M parameters; accepts (B, C, T, H, W) remote sensing video format
    - `ibm-nasa-geospatial/multi-temporal-crop-classification` — 3 854 chip dataset; input chips 224×224×18; 13-class CDL-derived masks
    - `multi_temporal_crop_classification.py` — mmsegmentation training configuration defining model, dataset, augmentation, optimiser and schedule
  - **outputs**:
    - `Prithvi-100M-multi-temporal-crop-classification` — fine-tuned segmentation model checkpoint; 80-epoch training run; mIoU: 0.4269, mAcc: 64.06%, aAcc: 60.64%

#### Activity: `ModelEvaluation`

- **name**: ModelEvaluation
- **task_count**: 1
- **started_at**: ~
- **ended_at**: ~
- **duration**: ~
- **status**: success: 1
  - **hosts**: ~
  - **inputs**:
    - `Prithvi-100M-multi-temporal-crop-classification` — fine-tuned checkpoint
    - `validation split` — 20% held-out chips from ibm-nasa-geospatial/multi-temporal-crop-classification
  - **outputs**:
    - Per-class IoU / Acc report — Natural Vegetation: IoU 0.40; Forest: 0.47; Corn: 0.55; Soybeans: 0.53; Wetlands: 0.40; Developed/Barren: 0.36; Open Water: 0.68; Winter Wheat: 0.50; Alfalfa: 0.31; Fallow/Idle: 0.35; Cotton: 0.32; Sorghum: 0.33; Other: 0.34
    - Aggregate metrics — mIoU: 0.4269, mAcc: 64.06%, aAcc: 60.64%

---

## 6. Significant Artifacts

### Input Artifacts

**Artifact: `ibm-nasa-geospatial/Prithvi-100M`**
- **name**: ibm-nasa-geospatial/Prithvi-100M
- **description**: First-of-its-kind temporal Vision Transformer (ViT + MAE) pretrained by IBM and NASA on contiguous US HLS V2 L30 data. Accepts remote sensing data in (B, C, T, H, W) format. 100M parameters. Six spectral bands (Blue, Green, Red, Narrow NIR, SWIR 1, SWIR 2). License: Apache-2.0.
- **reference**: https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M

**Artifact: `ibm-nasa-geospatial/multi-temporal-crop-classification`**
- **name**: ibm-nasa-geospatial/multi-temporal-crop-classification
- **description**: 3 854 GeoTIFF chips of 224×224 px at 30m resolution covering the CONUS for 2022. Each chip has 18 input bands (6 spectral × 3 time steps) and a 13-class CDL-derived segmentation mask. Randomly split 80/20 train/validation. License: Apache-2.0.
- **reference**: https://huggingface.co/datasets/ibm-nasa-geospatial/cdl-crops/

### Output Artifacts

**Artifact: `Prithvi-100M-multi-temporal-crop-classification`**
- **name**: Prithvi-100M-multi-temporal-crop-classification
- **description**: Fine-tuned geospatial segmentation model based on Prithvi-EO-1.0-100M, trained for 80 epochs on the HLS multi-temporal crop classification dataset using the mmsegmentation stack. Achieves mIoU of 0.4269 across 13 land-cover/crop classes. Includes an inference script and interactive demo.
- **reference**: https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M-multi-temporal-crop-classification
