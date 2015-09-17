""""
@jpablotoledo

Send a binary file over the socket with python

"""
import socket

HOST = 'localhost' #Remote IP address
PORT = 5500 #Remote IP port
DIR = (HOST,PORT) #Array of HOST and IP port
BUFSIZE = 1024 #Buffer size for send data
SOURCE = 'origen/ASO2.pdf' #Ubication of a local file

connection = socket.socket() #Create a socket object
connection.connect(DIR) #Setup IP and port configuration
print('Socket connected to:'+HOST+':'+PORT)

file = open(SOURCE,'rb') #File object with permission to read binary files
buffer = file.read(BUFSIZE) #Setup stream buffer size
#When you still having more data to send
while buffer:
    connection.send(buffer)
    buffer = file.read(BUFSIZE)
    print('Sending data')
print('The file was sended')
connection.close()
print('Connection has been closed')