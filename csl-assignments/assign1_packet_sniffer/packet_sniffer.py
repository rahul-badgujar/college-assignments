# Program to sniff packet sent over the local network and analyze it

import socket
import sys
from struct import *
from tokenize import String


def printInfo(keyValueDetails: dict) -> None:
    # Prints the given key-value pairs in format of key: value
    for key in keyValueDetails:
        value = keyValueDetails[key]
        print(f'{key}: {value}')


# Creating an INET, STREAMing socket
try:
    # Sniffing TCP Packets only
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
except socket.error as msg:
    errorCode = msg[0]
    message = msg[0]
    print('Socket could not be created. Below are the details:')
    printInfo(
        {
            'Error Code': errorCode,
            'Message': message
        }
    )
    sys.exit()

# Process the incoming packets
while True:
    # Receive the packet
    rawPacketReceived = s.recvfrom(65565)
    assert(len(rawPacketReceived) == 2, 'Packet received is in invalid format')

    # Extract the packet string from tuple
    packet = packet[0]

    # Extact the IP Header String => First 20 characters of packet represent IP Header
    ipHeaderStr = packet[0:20]

    # Unpack IP Header to IP Header Fields Tuple
    ipHeaderFields = unpack('!BBHHHBBH4s4s', ipHeaderStr)

    ipHeaderVersionRaw = ipHeaderFields[0]
    ipHeaderVersion = ipHeaderVersionRaw >> 4
    ipHeaderLength = ipHeaderVersionRaw & 0xF
    ttl = ipHeaderFields[5]
    protocol = ipHeaderFields[6]
    sourceAddress = socket.inet_ntoa(ipHeaderFields[8])
    destinationAddress = socket.inet_ntoa(ipHeaderFields[9])

    printInfo(
        {
            'Version': ipHeaderVersion,
            'IP Header Length': ipHeaderLength,
            'TTL': ttl,
            'Protocol': protocol,
            'Source Address': sourceAddress,
            'Destination Address': destinationAddress,
        }
    )

    # Extact the TCP Header String
    tcpHeaderStartIndex = ipHeaderLength * 4
    tcpHeaderRaw = packet[tcpHeaderStartIndex:tcpHeaderStartIndex+20]

    tcpHeaderFields = unpack('!HHLLBBHHH', tcpHeaderRaw)

    sourcePort = tcpHeaderFields[0]
    destinationPort = tcpHeaderFields[1]
    sequence = tcpHeaderFields[2]
    acknowledgement = tcpHeaderFields[3]
    doffReserved = tcpHeaderFields[4]
    tcpHeaderLength = doffReserved >> 4

    printInfo(
        {
            'Source Port': sourcePort,
            'Destination Port': destinationPort,
            'Sequence Number': sequence,
            'Acknowledgement': acknowledgement,
            'TCP Header Length': tcpHeaderLength,
        }
    )

    # Extract data from the packet
    dataStartIndex = tcpHeaderStartIndex + tcpHeaderLength * 4
    data = packet[dataStartIndex:]

    printInfo(
        {
            'Data': data,
        }
    )
