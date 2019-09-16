from socket import *
serverName="10.124.7.94"
serverPort=18000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence=input("enter file name")

clientSocket.send(sentence.encode())
filecontents=clientSocket.recv(1024).decode()
print('From Server:',filecontents)
clientSocket.close()
