""""
@jpablotoledo

Recieve a binary file over the socket with python

"""
import socket

HOST = '' #Must be empty in Server side
PORT = 5500 #Port to listen new connections
DIR = (HOST,PORT) #Array of IP an PORT
BUFSIZE = 1024 #Buffer size to send data

#Create a datagram socket object for IPv4
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Configure socket as a server socket
socket.bind(DIR)
#Preparte to listen new connections (max 5)
socket.listen(5)
print('Listenning for a new connection')

#Connections will be accepted in a secuential order
while True:
	#Accept a new connection
    connection, clientIP = socket.accept()
    print('Connected with: '+clientIP)
	#Prepare a file object to write a binary file
    file = open('file.pdf','wb')
    while True:
        data = connection.recv(BUFSIZE) #Recieved buffer
        if not data:
			print('End of file')
            break #Recieved all parts of the file
        file.write(data)
        print('Writting data')
    print('Closing file')
	file.close()
    print('Desconnecting '+clientIP)
	connection.close()
	