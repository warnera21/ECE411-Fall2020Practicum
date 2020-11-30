import os
import cv2
import numpy as np
from PIL import Image

# using the LBPH recognizer which stands for Local binary patterns histograms
'''
To understand the LBPH face recognizer:
Take a 3×3 window and move it across one image.
At each move, compare the pixel at the center, with its surrounding pixels.
Denote the neighbors with intensity value less than or equal to the center
pixel by 1 and the rest by 0.

After you read these 0/1 values under the 3×3 window in a clockwise order,
you will have a binary pattern like 11100011 that is local to a particular
area of the picture. When you finish doing this on the whole image,
you will have a list of local binary patterns.
'''
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'Data'

def getImageID(path):
    '''
    # The function getImageID() joins the path and f which is a variable
    # containing the filename as the loop goes through the list of files inside
    the folder in the path by using os.listdir(path)
    '''
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]

    faces=[]
    IDs=[]
    
    '''
    For loop that will be TRUE for every image that we  have.
    
    '''
    for imagePath in imagePaths:
        # Converts image in monochromo format 
        faceImg = Image.open(imagePath).convert('L')
         # Convert the images into a numpy array of name faceImg with 8-bit integer value.
        faceNp = np.array(faceImg, 'uint8')
        #Extract the ID number from the actual filename (splits the path name for the images captured)
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        # Add the data into the array by the name of faces and the data being added (faceNp)
        faces.append(faceNp)
        print (ID)
        #Adds the ID to the arrays IDs(the entire data needs to be fetch as an array to the trainer)
        IDs.append(ID)
    #Return the values of IDs matching a face
    return IDs, faces
# then return the values of the IDs of the matching face to train the dataset
Ids, faces = getImageID(path)
# using.train to train the system based on their images
recognizer.train(faces, np.array(Ids))
# then proceed to save the model
recognizer.save('Recognizer/trainningData.yml')

cv2.destroyAllWindows()
