import socket

s = socket.socket()
print("Created the socket...")

s.bind(("localhost", 8888))
s.listen(3)
print("Waiting for connection...")

while True:
    c, add = s.accept()
    print("New Client Connected...", add)
    c.send(bytes("Welcome to network", "utf-8"))
    c.close()
