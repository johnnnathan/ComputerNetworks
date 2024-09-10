from socket import *
import sys

# Get information from command line args
if len(sys.argv) != 4:
    print("Usage: python client.py <server_host> <server_port> <filename>")
    sys.exit()

serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
filename = sys.argv[3]

# Create a TCP client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

try:
    serverIP = gethostbyname(serverHost)
    print(f"Connecting to server IP: {serverIP} on port {serverPort}")
except gaierror:
    print(f"Error: Unable to resolve hostname '{serverHost}'")
    sys.exit()

clientSocket.connect((serverIP, serverPort))

# Send HTTP GET request
request = f"GET /{filename} HTTP/1.1\r\nHost: {serverHost}\r\n\r\n"
clientSocket.send(request.encode())

response = clientSocket.recv(4096).decode()

print("Server Response:\n")
print(response)

clientSocket.close()
