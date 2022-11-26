import os
import time
import cv2
import numpy as np
from PIL import Image
from threading import Thread



# -------------- image labels ------------------------

def getImagesAndLabels(path):
    # Klasördeki bütün resimlerin konumunu al
    resimKonumları = [os.path.join(path, f) for f in os.listdir(path)]
    yuzler = []
    OgrenciNumaralar = []
    # Resimleri yüzler ve numaralarla eşleştirir
    for resimKonumu in resimKonumları:
        # Bütün resimleri gri yapar
        pilImage = Image.open(resimKonumu).convert('L')
        # Resimleri numpy ile kullanılabilir hale getirir
        imageNp = np.array(pilImage, 'uint8')
        # Resimlerden öğrenci numaralarını alır
        OgrenciNumara = int(os.path.split(resimKonumu)[-1].split(".")[1])
        # extract the face from the training image sample
        yuzler.append(imageNp)
        OgrenciNumaralar.append(OgrenciNumara)
    return yuzler, OgrenciNumaralar


# ----------- Resimleri Kaydet ---------------
def TrainImages():
    kaydedici = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    yuzler, OgrenciNumara = getImagesAndLabels("TrainingImage")
    Thread(target = kaydedici.train(yuzler, np.array(OgrenciNumara))).start()
    Thread(target = counter_img("TrainingImage")).start()
    kaydedici.save("TrainingImageLabel"+os.sep+"Trainner.yml")
    print("Bütün Resimler Kaydedildi")

# Kaydedilen resimlerin sayısını hesaplar
def counter_img(path):
    imgcounter = 1
    resimKonumları = [os.path.join(path, f) for f in os.listdir(path)]
    for resimKonumu in resimKonumları:
        print(str(imgcounter) + " Resim Kaydedildi", end="\r")
        time.sleep(0.008)
        imgcounter += 1

