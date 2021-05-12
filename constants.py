import socket

host = "127.0.0.1" # Change This
port = 1234 # Change This

offset = 146 # Offset value. Change if neccesary


def send_payload(buffer):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(buffer)
    print(s.recv(1024))
    s.close()
