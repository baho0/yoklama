import os  
import check_camera
import Capture_Image
import Train_Image
import Recognize
import yoklamasil
import first

def title_bar():
    os.system('cls') 

    

    print("\t**********************************************")
    print("\t******** Yuz Algilama Yoklama Sistemi ********")
    print("\t**********************************************")



def anaMenu():
    title_bar()
    print()
    print(10 * "*", "HOSGELDIN", 10 * "*")
    print("[1] Kamera Kontrol")
    print("[2] Ogrenci Tanit")
    print("[3] Resimleri Kaydet")
    print("[4] Yoklama Al")
    print("[5] Kapat")

    while True:
        try:
            secim = int(input("Secim Yapin: "))
            
            if secim == 0 and os.path.isfile("key.lock")==True:
                Setup()
                break
            if os.path.isfile("key.lock")==True:
                print("Setup Calistirilmamis!!!")
            
            elif secim == 1:
                kameraKontrol()
                break
            elif secim == 2:
                ogrenciTanit()
                break
            elif secim == 3:
                Trainimages()
                break
            elif secim ==4:
                YoklamaBaslat()
                break
            elif secim == 5:
                print("Gorusuruz")
                break
            elif secim == 8:
                YoklamaSil()
                break
                
            else:
                print("Yanlis Secim. 1-6 Arasinda Bir Deger Girin")
                anaMenu()
            
        except ValueError:
            print("Yanlis secim. 1-6 Arasinda Girin\n Tekrar Deneyin")
    exit


# ---------------------------------------------------------


def kameraKontrol():
    check_camera.camer()
    key = input("Ana menuye donmek icin bir tusa basin...")
    anaMenu()


# --------------------------------------------------------------


def ogrenciTanit():
    Capture_Image.takeImages()
    key = input("Ana menuye donmek icin bir tusa basin...")
    anaMenu()


# -----------------------------------------------------------------


def Trainimages():
    Train_Image.TrainImages()
    key = input("Ana menuye donmek icin bir tusa basin...")
    anaMenu()

# --------------------------------------------------------------------


def YoklamaBaslat():
    Recognize.recognize_attendence()
    key = input("Ana menuye donmek icin bir tusa basin...")
    anaMenu()
    
# --------------------------------------------------------------------

def YoklamaSil():
    yoklamasil.tarih_sil()
    key = input("Ana menuye donmek icin bir tusa basin...")
    anaMenu()

# --------------------------------------------------------------------

def Setup():
    first.setup()
    key = input("Ana menuye donmek icin bir tusa basin...")
    anaMenu()

anaMenu()


