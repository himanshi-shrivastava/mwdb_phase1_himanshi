import glob
from HOG import hog_feature_extraction
from img import color_moments
from pymongo import MongoClient
import os
import cv2
import pandas as pd
from dbconnect import insertHogDescripter

#database connection
client = MongoClient("mongodb://localhost:27017")
db = client.mwdb

image_list = []
HOG_feature_vector = []
y = []
i=0

for filename in glob.glob('C:\Users\himan\PycharmProjects\MWDB\Smaller Dataset\*.jpg'):


    #calling function to compute feature vector for HOG
    HOG_feature_vector = hog_feature_extraction(filename)

    #converting feature vector to list
    HOG_feature_vector = HOG_feature_vector.tolist()

    #insertion into database
    image_name = os.path.split(os.path.split(filename)[1])[1]
    db.hog.insert_one({"image_name": image_name, "feature": HOG_feature_vector})


    #calling function to calculate the mean var and skew
    mean, var , skew = color_moments(filename)
    feature = mean + var + skew
    #splitting the image name to store in database
    image_name = os.path.split(os.path.split(filename)[1])[1]
    db.moments.insert_one({'image_name' : image_name ,  'feature' : feature})
    # image_list.append(im)







