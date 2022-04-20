import socket

s = socket.socket()

port = 1234
CONNECTION_CLOSED_CODE = "CONNECTION_CLOSED"

s.connect(("localhost", port))
recieve = s.recv(1024)
print(recieve.decode('utf-8'))

chat = 1

while (chat):
    msg = input("Enter the message: ")
    s.send(msg.encode('utf-8'))
    recieve = s.recv(1024)
    print(recieve.decode('utf-8'))
    chat = int(input("Continue chatting 0/1: "))
    if chat == 0:
        s.send(CONNECTION_CLOSED_CODE.encode("utf-8"))
        s.close()
