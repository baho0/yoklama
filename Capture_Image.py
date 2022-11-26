import requests
import cv2
import os
import mysql.connector as mysql
from mysql.connector import Error

import os.path
# counting the numbers
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False



# Take image function

def takeImages():
    if os.path.exists('sinif.txt'):
        f = open("sinif.txt", "r")
        x=f.read()
        f.close()
    else:
        x=input("Sinif Giriniz (Ör: 11j ,10a) --> ")
        f = open("sinif.txt", "a")
        f.write(x)
        f.close()
    try:
        conn = mysql.connect(host='localhost', database=x, user='root', password='')
        if conn.is_connected():
            OgrenciNumara = input("Ogrenci Numarasi Giriniz: ")
            Isim = input("Isim Giriniz: ")
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("DataBase'e Baglanildi: ", record)
            if(is_number(OgrenciNumara) and Isim.isalpha()):
                cam = cv2.VideoCapture(0)
                OgrenciNumara=str(OgrenciNumara)
                harcascadePath = "haarcascade_frontalface_default.xml"
                detector = cv2.CascadeClassifier(harcascadePath)
                sampleNum = 0

                while(True):
                    ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30,30),flags = cv2.CASCADE_SCALE_IMAGE)
                    for(x,y,w,h) in faces:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
                        sampleNum = sampleNum+1
                        cv2.imwrite("TrainingImage" + os.sep +Isim + "."+OgrenciNumara + '.' +
                                    str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                        cv2.imshow('frame', img)
                    if cv2.waitKey(100) & 0xFF == ord('q'):
                        break
                    elif sampleNum > 45:
                        break
                cam.release()
                cv2.destroyAllWindows()
                res = "Resimler OgrenciNumara 'ya kaydedildi: " + OgrenciNumara + " Isim : " + Isim
                cursor.execute("CREATE TABLE IF NOT EXISTS ogrenci_data(OgrenciNumara int(255),Isim varchar(255));")
                sql = "INSERT INTO ogrenci_data (OgrenciNumara,Isim) VALUES (%s,%s);"
                row = [OgrenciNumara, Isim]
                cursor.execute(sql, tuple(row))
                print("Kayit Depolandi")
                conn.commit()

                
            else:
                if(is_number(OgrenciNumara)):
                    print("Alfabe de bulunan bir isim giriniz")
                if(Isim.isalpha()):
                    print("Sayisal bir ogrenci numarasi giriniz")

    except Error as e:
                print("MySQL'e Baglanirkan hata oldu -->", e)



