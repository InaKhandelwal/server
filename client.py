#CLIENT CODE
#import socket library
import socket
#import subprocess library
import subprocess
#create an INET, STREAMing socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#reserve a port in your computer
clientsocket.connect(('localhost', 8000))
while True:
    test = subprocess.Popen(["netstat","-np","TCP"],stdout=subprocess.PIPE)
    output = test.communicate()[0]
    if (output.find(":22") >= 1):
        clientsocket.send('Somebody attempted to do SSH')
    else:
        clientsocket.send("SSH login not found")
