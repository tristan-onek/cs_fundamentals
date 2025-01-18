import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'  # Server's IP address or hostname
port = 12345      # Port number
client_socket.connect((host, port))

message = "Hello!"
client_socket.send(message.encode())

data = client_socket.recv(1024)  # 1024b of buffer
print('Received:', data.decode())
client_socket.close()
