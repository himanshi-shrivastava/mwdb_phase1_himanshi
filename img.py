import cv2
from PIL import Image
import os
import numpy as np
import Image
from scipy.stats import skew


def color_moments(image):

        #open th image,get the size of image and the pixels
        with Image.open(image) as img:
            width, height = img.size
        size_bytes = os.path.getsize(image)

        #read the image
        img1 = cv2.imread(image)

        #convert the image to yuv and show
        img_yuv = cv2.cvtColor(img1, cv2.COLOR_BGR2YUV)
        y, u, v = cv2.split(img_yuv)
        # print img_yuv.mode
        #cv2.imshow("yuv image", y)
        #cv2.waitKey(1000)

        # for computing mean var and skewness in 100*100 blocks
        w=(width/100)
        h=(height/100)

        y1_mean = []
        u1_mean = []
        v1_mean = []
        y1_variance = []
        u1_variance = []
        v1_variance = []
        y1_skew = []
        u1_skew = []
        v1_skew = []
        yuv_mean = []
        yuv_var = []
        yuv_skewness = []

        for i in range(h):
            for j in range(w):

                y4 = y[i * 100:100 + i * 100, j * 100:100 + j * 100]
                u4 = u[i * 100:100 + i * 100, j * 100:100 + j * 100]
                v4 = v[i * 100:100 + i * 100, j * 100:100 + j * 100]

             #calculating mean for each block of 100*100
                y1_mean.append(np.mean(y4))
                u1_mean.append(np.mean(u4))
                v1_mean.append(np.mean(v4))

             #calculating variance for each block of 100*100
                y1_variance.append(np.var(y4))
                u1_variance.append(np.var(u4))
                v1_variance.append(np.var(v4))


            #calculating skewness for each block of  100*100
                y1_skew.append(skew(y4.flatten()))
                u1_skew.append(skew(u4.flatten()))
                v1_skew.append(skew(v4.flatten()))

        yuv_mean = np.concatenate((y1_mean, u1_mean, v1_mean)).tolist()
        yuv_var = np.concatenate((y1_variance, u1_variance, v1_variance)).tolist()
        yuv_skewness = np.concatenate((y1_skew, u1_skew, v1_skew)).tolist()


        return yuv_mean , yuv_var , yuv_skewness




