import glob
from HOG import hog_feature_extraction
from pymongo import MongoClient
import pandas as pd

#database connection
client = MongoClient("mongodb://localhost:27017")
db = client.mwdb

image_list = []
HOG_feature_vector = []
i=0

for filename in glob.glob('C:\Users\himan\PycharmProjects\MWDB\Smaller Dataset\*.jpg'):
    # im=Image.open(filename)
    HOG_feature_vector = hog_feature_extraction(filename)
    print HOG_feature_vector
    #db.hog.insert_one({"image_name": filename, "feature": HOG_feature_vector})
    # image_list.append(im)
    i= i+1


print i
