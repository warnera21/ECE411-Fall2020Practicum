import numpy as np
import cv2
import serial
import random

TXD = 0
RXD = 0
l = 0

FaceDetect = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("Recognizer/trainningData.yml")
id = 0
font = cv2.FONT_HERSHEY_SIMPLEX


if __name__ == '__main__':
    while True:
        ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
        ser.flush()
        number = ser.read()
        if number != b'':
             if int.from_bytes(number, byteorder='big') == 0:
                TXD = 0;
                RXD = 0;
                print(RXD)
                print(TXD)
                ser.write(str(RXD).encode('utf-8'))
             if int.from_bytes(number, byteorder='big') == 1:
                TXD = 1;
                RXD = 0;
#             //////////////////////////////////////////////
#                 while True:
#                  try:
                ret, img = cam.read()
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces = FaceDetect.detectMultiScale(gray,1.3,5)

                for (x,y,w,h) in faces:
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
                    id, conf = rec.predict(gray[y:y+h, x:x+w])
                       
                       
                    if id==1:
                        id = "Hamed"
                        RXD = 1
                    elif id==2:
                        id = "Merdas"
                        RXD = 0
                    else:
                        RXD = 0
                    #cv2.putText(img, str(id), (x,y+h),font,2, (0,255,0),5)

                cv2.imshow("face", img)
                    #cam.release()
                         
                print(TXD)
                print(RXD)
                print("\n")
                ser.write(str(RXD).encode('utf-8'))
                     
                RXD = 0
                #except KeyboardInterrupt:
                  #     print (' All done... ')
               
                #break

    cam.release()
    cv2.destroyAllWindows()
