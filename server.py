#SERVER CODE
# import socket library
import socket
#create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#reserve a port in your computer
serversocket.bind(('localhost', 8000))
# put socket into listening mode
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
        print "msg From ",address,buf
