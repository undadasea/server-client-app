import socket


host, port = '', 8880
# initializing and connecting of the socket
Socket = socket.socket()
Socket.connect((host, port))

connection = True
while connection:
    inputNumber = input("Enter a number or "
                        "'exit' to close the connection: ")
    if inputNumber != '':
        Socket.send(bytes(inputNumber, 'utf-8'))

        data_from_server = Socket.recv(4096)
        print(data_from_server.decode('utf-8'))

        if data_from_server.decode('utf-8') == 'Bye.':
            connection = False

Socket.close()
