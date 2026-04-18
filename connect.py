# use the learning for the scanner
import socket

#address = ("192.168.2.108", 0)

for i in range(0, 100):
    address = ("Scanme.nmap.org", i)
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.settimeout(0.5)
    if mySocket.connect_ex(address) == 0:
        print(address[1], "port is open")
    else:
        #pass
        print(address[1], "Close")

