import datetime
import os
import time
import mysql.connector as mysql
from mysql.connector import Error
import cv2


#-------------------------
def recognize_attendence():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  
    recognizer.read("./TrainingImageLabel/Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
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
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("DataBase'e Baglanildi: ", record)
            while True:
                _,im = cam.read()
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray, 1.2, 5,minSize = (int(minW), int(minH)),flags = cv2.CASCADE_SCALE_IMAGE)
                for(x, y, w, h) in faces:
                    cv2.rectangle(im, (x, y), (x+w, y+h), (10, 159, 255), 2)
                    OgrenciNumara, conf = recognizer.predict(gray[y:y+h, x:x+w])

                    if conf < 100:
                        #MYSQL BAĞLANTISI EKLENCEK
                        cursor.execute("SELECT * from ogrenci_data WHERE OgrenciNumara ="+str(OgrenciNumara))
                        taninanOgrenci = cursor.fetchone()
                        print(taninanOgrenci)
                        OgrenciNumara,Isim = taninanOgrenci
                        confstr = "  {0}%".format(round(100 - conf))
                        GorselIsim = str(OgrenciNumara)+"-"+Isim



                    else:
                        OgrenciNumara = '  Unknown  '
                        GorselIsim = str(OgrenciNumara)
                        confstr = "  {0}%".format(round(100 - conf))

                    if (100-conf) > 67:
                        ts = time.time()
                        Saat = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                        sqldate=datetime.datetime.fromtimestamp(ts).strftime('%d_%m_%Y')
                        cursor.execute("CREATE TABLE IF NOT EXISTS yoklama_bilgileri_"+sqldate+"(ID int NOT NULL AUTO_INCREMENT, OgrenciNumara int(255),Isim varchar(255),Saat varchar(255),PRIMARY KEY (ID));")
                        cursor.execute("DELETE c1 FROM yoklama_bilgileri_"+sqldate+" c1 INNER JOIN yoklama_bilgileri_"+sqldate+" c2 WHERE c1.ID >= c2.ID AND c1.OgrenciNumara = c2.OgrenciNumara")
                        print("Table Olusturuldu....")
                        sql = "INSERT INTO yoklama_bilgileri_"+sqldate+"(OgrenciNumara,Isim,Saat) VALUES (%s,%s,%s);"
                        row = [OgrenciNumara,Isim, Saat]
                        cursor.execute(sql, tuple(row))
                        print("Kayit Depolandi")
                        conn.commit()

                    GorselIsim = str(GorselIsim)[2:-2]
                    
                    #Yazı Renk ve Stilleri
                    if(100-conf) > 67:
                        GorselIsim = GorselIsim + " [Pass]"
                        cv2.putText(im, str(GorselIsim), (x+5,y-5), font, 1, (255, 255, 255), 2)
                    else:
                        cv2.putText(im, str(GorselIsim), (x + 5, y - 5), font, 1, (255, 255, 255), 2)

                    if (100-conf) > 67:
                        cv2.putText(im, str(confstr), (x + 5, y + h - 5), font,1, (0, 255, 0),1 )
                    elif (100-conf) > 50:
                        cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 255, 255), 1)
                    else:
                        cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 0, 255), 1)


                cv2.imshow('Attendance', im)
                if (cv2.waitKey(1) == ord('q')):
                    break   
            cam.release()
            cv2.destroyAllWindows()      
                    
    except Error as e:
                print("MySQL'e Baglanirkan hata oldu -->", e)


