============================================================
REDI - Data Readiness Analysis
============================================================

# Data Card: jan2017_hpx64_9varCoupledAtmos-sst.zarr

## 1. Dataset Overview

- **Name:** jan2017_hpx64_9varCoupledAtmos-sst.zarr
- **Version:** 
- **Description:** Binary/specialized format: .zarr
- **Purpose:** 
- **Size:** 576.00 B
- **Records:** 0
- **Features:** 0
- **Format:** .zarr

## 2. Provenance

- **Authors:** Not specified
- **Organization:** 
- **Collection Method:** 
- **Data Sources:** Not specified
- **License:** 

## 3. Dataset Characteristics

- **Domain:** climate
- **Data Types:** 
- **Temporal Coverage:** 
- **Spatial Coverage:** 
- **Missing Data Strategy:** 

## 4. Sensitive Attributes

- **Contains PII:** No

## 5. Transformations

- **Normalization:** 
- **Train/Val/Test Split:** 

## 6. Annotations

- **Has Labels:** No

## 7. Limitations

## 8. AI Readiness Assessment

- **Current Level:** 5 - FULLY_READY
- **Description:** Sharded, normalized, in optimized format (HDF5/TFRecord/NPZ/Zarr)
- **Detected Domain:** climate


============================================================

# Pipeline Recommendations: Climate Data Pipeline

**Detected Domain:** climate
**Current Readiness Level:** FULLY_READY - Sharded, normalized, in optimized format (HDF5/TFRecord/NPZ/Zarr)
**Target Level:** FULLY_READY

## Pipeline Steps

| Step | Name | Description | Status |
|------|------|-------------|--------|
| 1 | download | Acquire data from sources (ERA5, CMIP6, etc.) | [x] |
| 2 | regrid | Regrid to uniform spatial/temporal resolution | [x] |
| 3 | normalize | Compute and apply normalization (mean/std) | [x] |
| 4 | shard | Partition into shards (.npz, .zarr) | [x] |

## Recommended Tools

- `xarray`
- `xesmf`
- `netCDF4`
- `zarr`

## Output Formats

- NPZ
- Zarr
- TFRecord
