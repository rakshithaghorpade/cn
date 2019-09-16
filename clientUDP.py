from socket import *
serverName="10.124.7.94"
serverPort=18000
clientSocket=socket(AF_INET,SOCK_DGRAM)

sentence=input("enter file name")
clientSocket.sendto(bytes(sentence,"utf-8"),(serverName,serverPort))
filecontents,serverAddress=clientSocket.recvfrom(2048)
print("From Server: ",filecontents)

clientSocket.close()
