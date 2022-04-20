from audioop import add
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Created socket...")

port = 1234
CONNECTION_CLOSED_CODE = "CONNECTION_CLOSED"

s.bind(("localhost", port))
print("Binded to localhost:{port}".format(port=port))

s.listen(10)
print("Socket is listening...")

count = 0
while True:
    c, addr = s.accept()
    count += 1
    print("Client Connected ({addr})".format(addr=addr))
    message = "Thank you for connecting, Client No. {clientNo}".format(
        clientNo=count)
    c.send(message.encode("utf-8"))
    while True:
        receive = c.recv(1024)
        if(receive.decode("utf-8") == CONNECTION_CLOSED_CODE):
            print("Client Disconnected ({addr})".format(addr=addr))
            c.close()
        else:
            print(receive.decode("utf-8"))
            message = input("Enter you reply: ")
            c.send(message.encode("utf-8"))
