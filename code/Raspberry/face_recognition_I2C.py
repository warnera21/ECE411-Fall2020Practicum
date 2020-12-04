import numpy as np
import cv2
import time
from smbus import SMBus

addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1


faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer/trainningData.yml")
id = 0
font = cv2.FONT_HERSHEY_SIMPLEX

def solenoid():
       
            # unlock door
            bus.write_byte(addr, 0x1)
            # wait for 3 seconds before locking door
            time.sleep(3)
            #lock the door
            bus.write_byte(addr, 0x0) 
    
while True:
 try:
   ret, img = cam.read()
   gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   faces = faceDetect.detectMultiScale(gray,1.3,5)

   for (x,y,w,h) in faces:
       cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
       id, conf = rec.predict(gray[y:y+h, x:x+w])
       
       
       if id==1:
            id = "josh"
            print('Welcome Josh Pradera! ')
            cam.release()
            cam = cv2.VideoCapture(0)
            solenoid()
         
            
       #cv2.putText(img, str(id), (x,y+h),font,3, (255,0,0),1,)

   #cv2.imshow("face", img)
   
   if cv2.waitKey(1)==ord('q'):
             break
 except KeyboardInterrupt:
   print (' All done... ')
   break

cam.release()
cv2.destroyAllWindows()

