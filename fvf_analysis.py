# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:34:09 2024

@author: rmportel
"""

import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt

def fvf_evaluation(img: np.array, name: str) -> None:
    """
    Evaluates the Fiber Volume Fraction (FVF) of a carbon fiber composite material
    from a grayscale microscopy image using Otsu's thresholding method.

    The function applies Gaussian blurring to reduce noise, segments the image
    into fiber and matrix regions using an automatically determined threshold,
    computes the FVF as the ratio of fiber pixels to total pixels, and displays
    a segmented image using a diverging colormap.

    Parameters
    ----------
    img : np.array
        Grayscale image array of the composite cross-section (e.g., cropped ROI).
    name : str
        File path or name of the original image, used to derive a display label.

    Returns
    -------
    None
        Prints the FVF result to the console and displays the segmented image.
    """
    
    # Otsu's thresholding after Gaussian filtering
    blur = cv.GaussianBlur(img,(5,5),0)
    thresholds, _ = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    thresholds = np.array([thresholds])
    
    # Using the threshold values, we generate the two regions.
    regions = np.digitize(img, bins=thresholds)
    
    # Identify fibers based on the threshold
    fiber: bool = (img.ravel() > thresholds) 
    fvf: float = fiber.sum()/img.ravel().size

    # Print FVF     
    name: str = os.path.basename(name).split('.')[0]
    
    print(f'{name:-^60}')
    print(f'FVF = {fvf: .2%}')
    
    fig, ax = plt.subplots(figsize=(20,8))
    ax.imshow(regions, cmap = 'RdGy'), plt.xticks([]), plt.yticks([])
    plt.show()
    
def set_roi(address: str, ROI: list[int]) -> np.array:
    """
    Loads a grayscale image and extracts a Region of Interest (ROI),
    displaying a transparent green overlay to visually confirm the selected area.

    The ROI is defined by pixel coordinates [x_start, x_end, y_start, y_end]
    and the function returns the cropped sub-image for further analysis.

    Parameters
    ----------
    address : str
        File path to the input image.
    ROI : list[int]
        A list of four integers defining the region of interest in the format
        [x_start, x_end, y_start, y_end].

    Returns
    -------
    np.array
        Cropped grayscale image array corresponding to the specified ROI.
    """

    # Read image
    img = cv.imread(address, cv.IMREAD_GRAYSCALE)
    overlay = img.copy() 
    
    # Set ROI on Image
    x, y, w, h = [ROI[0], ROI[2], ROI[1] - ROI[0], ROI[3] - ROI[2]]
    
    # A filled rectangle 
    cv.rectangle(overlay, (x, y), (x+w, y+h), (0, 255, 0), -1) 
    
    # Transparency factor. 
    alpha = 0.4  
  
    # Following line overlays transparent rectangle 
    # over the image 
    image_new = cv.addWeighted(overlay, alpha, img, 1 - alpha, 0) 
    
    fig, ax = plt.subplots(figsize=(20,8))
    ax.imshow(image_new), plt.xticks([]), plt.yticks([]), plt.show()
    
    return img[ROI[2]:ROI[3], ROI[0]:ROI[1]]

def zoomed_image(address: str, zoomed_region: list[int]) -> None:
    """
    Displays a grayscale image with an inset zoomed-in view of a specified
    sub-region, highlighted with an orange border indicator.

    Useful for visually inspecting fine microstructural details within a
    larger microscopy image without losing overall context.

    Parameters
    ----------
    address : str
        File path to the input image.
    zoomed_region : list[int]
        A list of four integers [x1, x2, y1, y2] defining the pixel boundaries
        of the sub-region to zoom into.

    Returns
    -------
    None
        Displays the image with the zoomed inset using matplotlib.
    """

    img = cv.imread(address, cv.IMREAD_GRAYSCALE)
    
    fig, ax = plt.subplots(figsize=(20,8))

    ax.imshow(img, cmap = 'RdGy'), plt.xticks([]), plt.yticks([])
    
    # inset Axes....
    x1, x2, y1, y2 = zoomed_region  # subregion of the original image
    extent = (x1, x2, y1, y2)
    axins = ax.inset_axes(
        [0.6, 0.9, 0.47, 0.47],
        xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])
    axins.imshow(img, extent=extent, origin="lower")
    
    ax.indicate_inset_zoom(axins, edgecolor="orange", lw =7)
    
    
if __name__ == '__main__':
    img = set_roi(address = 'HP-RTM_SAMPLE_02.jpg', ROI = [12500, 23500, 0, 5500])
    fvf_evaluation(img, name = 'HP-RTM_SAMPLE_02.jpg')