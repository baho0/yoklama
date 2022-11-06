#giriş
import cv2
import numpy as np
import socket
HOST = "127.0.0.1"
PORT = 4444
print("a")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("b")
while True:
    try:
        s.connect((HOST, PORT)) 
        break
    except Exception as e:
        print("Sunucuya bağlanılamadı tekrar denemek için ENTER'a basın.")
        input()
        


#foto çek


#fotoyu at