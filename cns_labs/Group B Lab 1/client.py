import socket

c = socket.socket()

c.connect(("localhost", 8888))
print("Connected to Server...")
