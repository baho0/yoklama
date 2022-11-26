import mysql.connector as mysql
from mysql.connector import Error
from datetime import datetime

def tarih_sil():
    try:
        x=input("Sinif Giriniz (Ör: 11j ,10a) --> ")
        conn = mysql.connect(host='localhost', database=x, user='root', password='')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("DataBase'e Baglanildi: ", record)
            tarihsec = input("Silmek istediginiz tarihi girin(gun/ay/yil): ")
            try:
                gun, ay, yil = tarihsec.split("/")
                gun = tarihsec[:tarihsec.find("/")]
                ay = tarihsec[tarihsec.find("/")+1:tarihsec.rfind("/")]
                yil = tarihsec[tarihsec.rfind("/")+1:]
            except:
                cursor.execute("DROP TABLE "+tarihsec)
                print("--------------------------------------------------------")
                print("Belirtilen Yoklama Kaydi SQL'den Silindi--> "+tarihsec)
            else:
                cursor.execute("DROP TABLE yoklama_bilgileri_"+gun+"_"+ay+"_"+yil)
                print("--------------------------------------------------------")
                print("Belirtilen Yoklama Kaydi SQL'den Silindi--> yoklama_bilgileri_"+gun+"_"+ay+"_"+yil)

    except Error as e:
                print("MySQL'e Baglanirkan hata oldu -->", e)
