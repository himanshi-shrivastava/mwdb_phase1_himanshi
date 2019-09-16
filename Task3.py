import math
import traceback
from dbconnect import getHOGDescriptor , getcolormoments
from skimage import io
from scipy.spatial import distance
import cv2
from HOG import hog_feature_extraction
from img import color_moments
from pymongo import MongoClient


path = "C:/Users/himan/PycharmProjects/MWDB/Smaller Dataset/"

#Funtion to find the euclidean distance between the 2 vectors
def euclideanDistance(U, V):
    sum=0

    for i in range(len(U)):
        sum= sum + math.pow((V[i] - U[i]), 2)
    dist = math.sqrt(sum)
    return dist

#Function to find the cosine similarity for the 2 vectors
def cosine(U, V):

    dot_product= 0
    U_magnitude = 0
    V_magnitude = 0

    for i in range(len(U)):
        dot_product = dot_product + U[i]*V[i]

        U_magnitude = U_magnitude + U[i]*U[i]
        V_magnitude = V_magnitude +  V[i]*V[i]

    U_magnitude = math.sqrt(U_magnitude)
    V_magnitude = math.sqrt(V_magnitude)

    #calculating cosine similarity using the formula
    cos_similarity = dot_product/(U_magnitude*V_magnitude)
    return cos_similarity


#function to compute and return similar image features descriptors
def similarImages(input_image_vector, features, model, k):

    #if model is hog, compute similarity using cosine similarity
    if model == 'hog':
        cos = []
        for i in features:
            cos_similarity = cosine(i['feature'], input_image_vector)
            cos.append([i['image_name'], cos_similarity])
        return sorted(cos, key=lambda x: x[1], reverse=True)[:k]


    #if model is color moments, compute similarity using euclidean distance
    elif model=='color moments':
        distance = []
        for i in features:
            euc_distance = euclideanDistance(input_image_vector, i['feature'])
            distance.append([i['image_name'], euc_distance])
        return sorted(distance, key=lambda x: x[1])[:k]

    else:
        print("please enter correct model names: color moments or hog")


def main():
    imageid = raw_input("Enter image id")
    model = raw_input("Enter the model: hog or color moments")
    k = raw_input("Enter the number of similar images")

    try:
        client = MongoClient("mongodb://localhost:27017")
        db = client.mwdb


        if model == 'hog':

            input_image_vector = getHOGDescriptor(imageid)
            if input_image_vector is not None:
                features = db.hog.find({'image_name': {"$ne": imageid}})
                distance=similarImages(input_image_vector, features, model, int(k))
                print distance

                # with open("output.text", "a") as file_output:
                #     file_output.writeLines(distance)



        elif model == 'color moments':

            image_vector = getcolormoments(imageid)
            if image_vector is not None:
                features = db.moments.find({'image_name': {"$ne": imageid}})
                distance = similarImages(image_vector, features, model, int(k))
                print distance

    except Exception as detail:
        traceback.print_exc()
        print "no success"


if __name__== '__main__':
    main()









