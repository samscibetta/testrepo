#Enter the header values in each of the fields below and press "Submit".
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd) #sned above command to server

while True:
    data = mysock.recv(512) #max of 512 datapoints to be input
    if (len(data) <1) :
        break #This is telling it to end when no more data
    print(data.decode()) #converts back to 'unicode'
mysock.close()
