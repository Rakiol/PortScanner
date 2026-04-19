# use the learning for the scanner
import socket

def scan_port(host, port):
    address = (host, port)
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.settimeout(0.5)
    if mySocket.connect_ex(address) == 0:
        print("Port ", address[1], " is OPEN")
    else:
        print("PORT ", address[1], " is CLOSED")
    mySocket.close()

def scan_range(host, range0, range1):

    for i in range(range0, range1):
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.settimeout(0.5)
        address = (host, i)
        file = open("openPorts.txt", "a")
        if mySocket.connect_ex(address) == 0:
            file.write(str(i) + " is Open\n")
        else:
            pass
        mySocket.close()

if __name__ == "__main__":
    a = input("Please write IP or Domain\n")
    b = int(input("Please write 1 = Single Port or 2 = Range\n"))
    if b == 1:
        c = int(input("Write PORT number\n"))
        scan_port(a, c)
    else:
        c = int(input("Write Start Range\n"))
        d = int(input("Write End Range\n"))
        scan_range(a, c, d)
    print()
    print("Finished")
