import cv2
import codecs, json
import os
import numpy as np
import Image
from skimage.transform import rescale
from skimage.feature import hog
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd

def hog_feature_extraction(image):

    img1 = cv2.imread(image,cv2.IMREAD_GRAYSCALE)

    #downsampling the image to 1:10 rows and cols
    img_rescaled = rescale(img1, 0.1, anti_aliasing=True)

    #extracting features of the histogram according to the mentioned parameter
    features, img_hog = hog(img_rescaled,
                            orientations=9,
                            pixels_per_cell=(8, 8),
                            cells_per_block=(2, 2),
                            visualize=True,
                            multichannel= False,
                            block_norm='L2-Hys')

    #printing features as the vector
    # print features

    #plotting the histogram of gradient against the features
    # plt.hist(features , bins=9, alpha=0.5)
    # pd.Series(features).to_json(orient='values')

    return features




