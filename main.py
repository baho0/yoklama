from email.mime import image
from mimetypes import init
import cv2
import numpy as np
import trainer
from logging import exception
import cv2


class student:
    def __init__(self,name,surname,className,id):
        self.name = name
        self.surname= surname
        self.className = className
        self.id = id
    

class functions:
    def __init__(self):
        pass
    def recognize():
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainer/trainer.yml')
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cam = cv2.VideoCapture(0)

        while True:
            ret, im =cam.read()
            gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2,5)
            for(x,y,w,h) in faces:
                cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
                Id = recognizer.predict(gray[y:y+h,x:x+w])
                if(Id[0] == 0):
                    Id = "zhra"
                elif(Id[0]==1):
                    Id = "bao"
                elif(Id[0]==2):
                    Id = "kaan"
                else:
                    Id = "Unknow"
                cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
                cv2.putText(im, str(Id), (x,y-40), font, 1, (255,255,255), 3)
                cv2.putText
            cv2.imshow('im',im) 
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()

    def addStudent():
        vid_cam = cv2.VideoCapture(0)
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        face_id=input("Öğrencinin numarasını giriniz >>> ")
        """while(True):
            try:
                facexist = open("dataset/User."+str(face_id)+".1.jpg")
                face_id+=1
                
            except Exception as e:
                print(e)
                break"""
        count = 0
        while(True):
            _, image_frame = vid_cam.read()
            img = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(img, 1.3, 6)
            print(image_frame)
            for (x,y,w,h) in faces:
                cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
                count += 1
                cv2.imwrite("images/Student." + str(face_id) + '.' + str(count) + ".jpg", img[y:y+h,x:x+w])
                cv2.imshow('frame', image_frame)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif count>=200:
                break
        vid_cam.release()
        cv2.destroyAllWindows()
        trainer.train()
while(True):
    print("""
        1 = yoklama al
        2 = yeni öğrenci ekle
        3 = çık
        """)
    selectedMode = int(input(">>> "))
    if selectedMode == 1:
        functions.recognize()
    elif selectedMode == 2:
        functions.addStudent()
    elif selectedMode == 3:
        break
    else:
        print("hatalı giriş")
