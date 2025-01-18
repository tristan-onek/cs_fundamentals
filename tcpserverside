import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 12345
server_socket.bind((host, port))

server_socket.listen(5)

print('Server is now listening.')

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print('Connected to:', client_address)

    # Receive data from the client
    data = client_socket.recv(1024)
    print('Received:', data.decode())

    # Send data to the client
    message = "Bon matin, client!"
    client_socket.send(message.encode())

    # Close the client socket
    client_socket.close()
