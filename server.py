def SendImage():
    import socket
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('localhost',1002))
    server.listen()
    client_socket,client_address =server.accept()
    studentID = input("Öğrencinin numarasını giriniz >>>")
    client_socket.send(studentID.encode())
    def sendImage(count):
        file = open(f"images/Student.{studentID}.{count}.jpg","rb")
        img_data = file.read(8000*2)
        client_socket.send(img_data)
        file.close()
    count =1
    while count <=200:
        sendImage(count)
        print(client_socket.recv(8000*2).decode())
        count+=1
    server.close()