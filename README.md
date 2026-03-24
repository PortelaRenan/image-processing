# Fiber Volume Fraction (FVF) Analysis of Composite Materials

A Python-based image processing toolkit for evaluating the **Fiber Volume Fraction (FVF)** of composite materials from microscopy cross-section images. Developed as part of research on composite structures manufacturing processes.

---

## Overview

This tool automates the quantification of fiber content in composite material micrographs using classical computer vision techniques. It segments fiber and matrix phases via **Otsu's thresholding**, computes the FVF, and provides visualization utilities for region selection and microstructural inspection.

---

## Features

- 🔬 **Automated FVF computation** using Otsu's thresholding with Gaussian pre-filtering
- 🖼️ **Region of Interest (ROI) selection** with transparent overlay preview
- 🔍 **Zoomed inset visualization** for detailed microstructural inspection
- 📊 Segmented image display with diverging colormap for clear fiber/matrix contrast

---

## Requirements

```
opencv-python
numpy
matplotlib
```

Install dependencies with:

```bash
pip install opencv-python numpy matplotlib
```

---

## Usage

```python
from fvf_analysis import set_roi, fvf_evaluation, zoomed_image

# Step 1 – Crop the region of interest from the micrograph
img = set_roi(address='sample.jpg', ROI=[x_start, x_end, y_start, y_end])

# Step 2 – Compute and display the Fiber Volume Fraction
fvf_evaluation(img, name='sample.jpg')

# Optional – Inspect a zoomed region of the original image
zoomed_image(address='sample.jpg', zoomed_region=[x1, x2, y1, y2])
```

---

## Functions

| Function | Description |
|---|---|
| `set_roi()` | Loads an image and extracts a cropped ROI with a visual overlay preview |
| `fvf_evaluation()` | Computes FVF via Otsu's thresholding and displays the segmented image |
| `zoomed_image()` | Renders the full image with a highlighted inset zoom of a sub-region |

---

## Background

Fiber Volume Fraction is a critical quality metric in composite manufacturing, directly influencing the mechanical performance of the final part. This tool was developed to support microstructural analysis of samples produced via processes such as **HP-RTM (High-Pressure Resin Transfer Moulding)**.

---

## Author

**Renan Portel**
PhD in Mechanical Engineering — Composite Structures Manufacturing Processes
