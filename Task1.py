from pymongo import MongoClient
import glob
from HOG import hog_feature_extraction
from img import color_moments
import traceback

def main():
    imageid = raw_input("Enter image id")
    model = raw_input("Enter the model: hog or color moments")

    #database connection
    client = MongoClient("mongodb://localhost:27017")
    db = client.mwdb



    filename = 'C:/Users/himan/PycharmProjects/MWDB/Smaller Dataset/'+ imageid +'.jpg'

    if model == 'hog':
            HOG_feature_vector = hog_feature_extraction(filename)
            print HOG_feature_vector

    else:
            mean, var, skew = color_moments(filename)
            print ("mean" , mean)
            print ("variance" , var)
            print ("skewness" , skew)





if __name__== '__main__':
    main()
