from socket import *
serverName="10.124.7.94"
serverPort=18000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print("server ready to recieve")
while 1:
    connectionSocket,addr=serverSocket.accept()
    sentence=connectionSocket.recv(1024).decode()

    file=open(sentence,"r")
    l=file.read(1024)

    connectionSocket.send(l.encode())
    file.close()
    connectionSocket.close()
