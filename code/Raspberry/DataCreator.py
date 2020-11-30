import cv2
import numpy as np
from datetime import date
from datetime import datetime

FaceDetect = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

id = input('Enter user ID: ')
sampleNum = 0;

while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = FaceDetect.detectMultiScale(gray, 1.3, 5);
    
    for(x, y, w, h) in faces:
        sampleNum = sampleNum + 1;
        cv2.imwrite("Data/ID."+str(id)+"."+str(sampleNum)+".jpg",  gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
        cv2.waitKey(300);
        
    cv2.imshow("Face",img);
    cv2.waitKey(1);
    if(sampleNum>20):
        break
    
cam.release()
cv2.destroyAllWindows()