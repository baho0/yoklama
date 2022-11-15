def GetImage():
    import socket
    from time import sleep
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("localhost",1002))
    studentID = client.recv(8000*2).decode()
    def getImage(studentID,count):
        file = open(f"serverImages/Student.{studentID}.{count}.jpg","wb")
        image_chunk = client.recv(8000*2)
        file.write(image_chunk)
        file.close()
    count = 1
    while count <=200:
        getImage(studentID,count)
        client.send("ok".encode())
        count+=1
