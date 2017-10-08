#CLIENT CODE
import socket
import subprocess
    
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8000))
while True:
    test = subprocess.Popen(["netstat","-np","TCP"],stdout=subprocess.PIPE)
    output = test.communicate()[0]
    if (output.find(":22") >= 1):
        clientsocket.send('Somebody attempted to do SSH')
    else:
        clientsocket.send("SSH login not found")