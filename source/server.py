import socket


def to_prime_numbers(n):
    i = 2
    primes_array = []
    while i * i <= abs(n):
        while abs(n) % i == 0:
            primes_array.append(i)
            n /= i
        i += 1
    primes_array.append(n)
    return primes_array


def run():
    host, port = '', 8880

    # socket implementation using default values
    Socket = socket.socket()

    # bind if the socket is not already in use
    Socket.bind((host, port))

    # waiting for one client
    Socket.listen(1)
    print('Server is waiting for connection...')

    # creating socket object, clientConnection, to receive info
    clientConnection, clientAddress = Socket.accept()
    # checking info from the client
    print('Connected.', 'Client address:', clientAddress)

    connection = True
    while connection:
        print('Server is waiting for data from the client...')
        input_string = clientConnection.recv(4096).decode('utf-8')
        print('input: ', input_string)

        try:
            primes_array = to_prime_numbers(int(input_string))
            bytearray_of_prime_numbers = bytearray()
            # for sending data in bytes
            for i in range(primes_array.__len__()):
                bytearray_of_prime_numbers += bytes(str(primes_array[i])
                                                    + ' ', 'utf-8')
            clientConnection.send(bytearray_of_prime_numbers)
            print('data was sent.')
        except ValueError:
            # to close the connection
            if input_string == 'exit':
                connection = False
                clientConnection.send(bytes('Bye.', 'utf-8'))
            # to continue
            else:
                clientConnection.send(bytes('Error. Try again.', 'utf-8'))

    clientConnection.close()


if __name__ == '__main__':
    run()
