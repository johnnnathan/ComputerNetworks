from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 8080 #Port number of host
serverIP = '0.0.0.0' #IP-address 

serverSocket.bind((serverIP, serverPort))  # Bind to the IP address and port
serverSocket.listen(1)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        #Read the file data 
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        #Send 200 Response
        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        #Send data
        connectionSocket.sendall(header.encode())
        connectionSocket.sendall(outputdata.encode())
        connectionSocket.close()

    except IOError:
        #Send 404 error response
        error_message = ("HTTP/1.1 404 NOT FOUND\r\n")
        connectionSocket.sendall(error_message.encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()
