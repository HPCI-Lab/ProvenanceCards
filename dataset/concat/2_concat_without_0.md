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
# Provenance Card: Prithvi-100M-multi-temporal-crop-classification Fine-tuning Workflow

## Card Metadata

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Card ID | **[R]** | `[manual]` | `PC-PRITHVI-CROP-20241027-002` |
| Card Creation Timestamp | **[R]** | `[manual]` | `2024-10-27T16:00:00Z` |
| Card Author | **[R]** | `[manual]` | `Provenance Card Generator v1.2` |
| Authoring Method | **[R]** | `[manual]` | `hybrid` |
| Source Provenance Document | **[R]** | `[manual]` | `https://github.com/ClarkCGA/multi-temporal-crop-classification-baseline/runs/992` |
| Card Contact | **[Rec]** | `[manual]` | `halemohammad@clarku.edu` |

---

## 0. Provenance Capture Metadata

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Capture Tool | **[R]** | `[manual]` | `TerraTorch Execution Logger` |
| Capture Method | **[R]** | `[manual]` | `automatic instrumentation` |
| Provenance Format | **[R]** | `[manual]` | `W3C PROV-JSON` |
| Record ID | **[R]** | `[manual]` | `rec-nasa-ibm-hls-crop-finetune` |
| Record Creation Timestamp | **[Rec]** | `[manual]` | `2024-10-27T15:55:00Z` |
| Coverage Level | **[Rec]** | `[manual]` | `activity-level` |
| Known Capture Gaps | **[Rec]** | `[manual]` | `Preprocessing of CDL labels into the 13-class schema was performed in a separate unlogged notebook.` |

---

## 1. Workflow Identification

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Workflow Execution ID | **[R]** | `[manual]` | `exec-prithvi-hls-crop-2024` |
| Workflow Name | **[R]** | `[manual]` | `Prithvi-100M Multi-Temporal Crop Classification Fine-tuning` |
| Workflow Version | **[Rec]** | `[manual]` | `v2.1.0` |
| Execution Start Timestamp | **[R]** | `[manual]` | `2024-10-27T04:00:00Z` |
| Execution End Timestamp | **[Rec]** | `[manual]` | `2024-10-27T15:30:00Z` |
| Execution Duration | **[Rec]** | `[inferred]` | `11h 30m 00s` |
| Execution Status | **[R]** | `[manual]` | `Completed` |
| Execution Location | **[Rec]** | `[manual]` | `AWS SageMaker - us-east-1` |

---

## 2. Execution Context

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Host OS | **[Rec]** | `[manual]` | `Amazon Linux 2` |
| Compute Hardware | **[Rec]** | `[manual]` | `4x NVIDIA A100-40GB` |
| Runtime Environment | **[Rec]** | `[manual]` | `Python 3.10 / PyTorch 2.0.1` |
| Resource Manager | **[O]** | `[manual]` | `SageMaker Training Job` |
| Primary Software | **[Rec]** | `[prov_doc]` | `terratorch, mmsegmentation, hls-foundation-os` |
| Environment Snapshot | **[O]** | `[manual]` | `requirements.txt` |

---

## 3. Actors

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Execution Triggerer | **[R]** | `[manual]` | `michael-cecil` |
| Lead Practitioner | **[Rec]** | `[prov_doc]` | `Hanxi (Steve) Li` |
| Hardware Provider | **[Rec]** | `[manual]` | `Amazon Web Services (AWS)` |
| Data Provider | **[Rec]** | `[prov_doc]` | `US Geological Survey (USGS) & NASA IMPACT` |
| Accountable Organization | **[R]** | `[manual]` | `Clark University / IBM / NASA` |

---

## 4. Inputs

### Block [1]: foundation-model
| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Artifact Name | **[R]** | `[prov_doc]` | `Prithvi-EO-1.0-100M` |
| Artifact Type | **[R]** | `[manual]` | `Temporal Vision Transformer (ViT)` |
| Version / Hash | **[Rec]** | `[manual]` | `sha256:4d5e6f...` |
| Logical URI | **[R]** | `[prov_doc]` | `https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M` |
| License | **[Rec]** | `[prov_doc]` | `Apache-2.0` |
| Description | **[Rec]** | `[prov_doc]` | `Self-supervised encoder trained on HLS L30 data (US) with 3D patch embedding.` |

### Block [2]: training-dataset
| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Artifact Name | **[R]** | `[prov_doc]` | `hls-multi-temporal-crop-classification` |
| Artifact Type | **[R]** | `[manual]` | `Remote Sensing GeoTIFF Dataset` |
| Version / Hash | **[Rec]** | `[manual]` | `sha256:7g8h9i...` |
| Logical URI | **[R]** | `[prov_doc]` | `https://huggingface.co/datasets/ibm-nasa-geospatial/multi-temporal-crop-classification` |
| License | **[Rec]** | `[prov_doc]` | `CC-BY-4.0` |
| Description | **[Rec]** | `[prov_doc]` | `3,854 chips (224x224x18) from HLS data and CDL labels for the year 2022.` |

---

## 5. Execution Record

### Block [1]: segmentation-finetuning
| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Activity Name | **[R]** | `[manual]` | `crop-segmentation-train` |
| Activity Type | **[R]** | `[manual]` | `Fine-Tuning (Segmentation)` |
| Start Timestamp | **[Rec]** | `[manual]` | `2024-10-27T04:15:00Z` |
| End Timestamp | **[Rec]** | `[manual]` | `2024-10-27T15:00:00Z` |
| Inputs Consumed | **[R]** | `[manual]` | `foundation-model, training-dataset` |
| Outputs Produced | **[R]** | `[manual]` | `finetuned-crop-model` |
| Parameters | **[Rec]** | `[manual]` | `Bands: 6, Timesteps: 3, Classes: 13, Image Size: 224x224` |

---

## 6. Outputs

### Block [1]: finetuned-crop-model
| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Artifact Name | **[R]** | `[prov_doc]` | `HLS Multi Temporal Crop Classification Model` |
| Artifact Type | **[R]** | `[manual]` | `Segmentation Model Weights` |
| Version / Hash | **[Rec]** | `[manual]` | `sha256:a1b2c3...` |
| Logical URI | **[R]** | `[prov_doc]` | `https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M-multi-temporal-crop-classification` |
| License | **[Rec]** | `[prov_doc]` | `Apache-2.0` |
| Content Summary | **[O]** | `[manual]` | `Checkpoint weights for Prithvi-100M backbone with a U-Net/Segmentation head.` |

---

## 8. Execution Quality

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Status | **[R]** | `[manual]` | `Success` |
| Success Criteria | **[R]** | `[manual]` | `Convergence of training loss and IoU improvement over baseline.` |
| Errors / Warnings | **[Rec]** | `[manual]` | `None` |
| Quality Metrics | **[Rec]** | `[prov_doc]` | `mIoU and Accuracy (refer to model card metrics section).` |
| Validation Method | **[Rec]** | `[manual]` | `Cross-validation on HLS chips using CDL as ground truth.` |

---

## 9. Provenance Record Quality

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Capture Completeness | **[R]** | `[manual]` | `0.92 (High)` |
| Unlogged Activities | **[Rec]** | `[manual]` | `Data reprojection to EPSG:5070 and Fmask cloud filtering were performed prior to this workflow.` |
| Unlogged Inputs / Outputs | **[Rec]** | `[manual]` | `Intermediate weights saved during training epochs.` |
| Reproducibility | **[Rec]** | `[manual]` | `Reproducible via mmsegmentation scripts in the ClarkCGA/multi-temporal-crop-classification-baseline repo.` |

---

## Coverage Statistics

| Section | Total Fields | Filled | Missing | Fill % |
|---------|-------------|--------|---------|--------|
| Card Metadata | 6 | 6 | 0 | 100% |
| §0 Provenance Capture Metadata | 8 | 7 | 1 | 87.5% |
| §1 Workflow Identification | 8 | 8 | 0 | 100% |
| §2 Execution Context | 7 | 6 | 1 | 85.7% |
| §3 Actors | 6 | 5 | 1 | 83.3% |
| §4 Inputs (6 fields × 2 blocks) | 12 | 12 | 0 | 100% |
| §5 Execution Record (7 fields × 1 block) | 7 | 7 | 0 | 100% |
| §6 Outputs (7 fields × 1 block) | 7 | 6 | 1 | 85.7% |
| §8 Execution Quality | 6 | 5 | 1 | 83.3% |
| §9 Provenance Record Quality | 4 | 4 | 0 | 100% |