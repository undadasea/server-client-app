import pytest
import socket


# client simulation
def test_connection():
    s = socket.socket()
    s.connect(('localhost', 8880))

    s.send(bytes('10', 'utf-8'))
    assert '2 5.0 ' == s.recv(4096).decode('utf-8')

    s.send(bytes('-12', 'utf-8'))
    assert '2 2 -3.0 ' == s.recv(4096).decode('utf-8')

    s.send(bytes('0', 'utf-8'))
    assert '0 ' == s.recv(4096).decode('utf-8')

    s.send(bytes('1', 'utf-8'))
    assert '1 ' == s.recv(4096).decode('utf-8')

    s.send(bytes('-1', 'utf-8'))
    assert '-1 ' == s.recv(4096).decode('utf-8')

    s.send(bytes('100001', 'utf-8'))
    assert '11 9091.0 ' == s.recv(4096).decode('utf-8')

    s.send(bytes('nothing', 'utf-8'))
    assert 'Error. Try again.' == s.recv(4096).decode('utf-8')

    s.send(bytes('5560-', 'utf-8'))
    assert 'Error. Try again.' == s.recv(4096).decode('utf-8')

    s.send(bytes('exit', 'utf-8'))



