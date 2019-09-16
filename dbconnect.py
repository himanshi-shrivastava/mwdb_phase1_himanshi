from pymongo import MongoClient
from skimage import io
from pymongo import MongoClient

#connection with the data base
client = MongoClient("mongodb://localhost:27017")
db = client.mwdb
# imageid='Hand_0008662.jpg'

#insert HOG feature vector for each image into the database
def insertHogDescripter(imgname, feature_vector):
    success=  db.hog.insert_one({"image_name": imgname, "feature": feature_vector})
    return success

#get HOG_descriptor of particular image from database
def getHOGDescriptor(imageName):
    HOG_Descriptor = db.hog.find_one({"image_name" : imageName})
    return HOG_Descriptor["feature"]

#get color moments of particular image from database
def getcolormoments(imageName):
    features = db.moments.find_one({"image_name" : imageName})
    return features["feature"]


# def getallimages(imageid):
#
# results = db.hog.find({"image_name" : {"$ne" : imageid}},{"image_name" : 1})
# print results