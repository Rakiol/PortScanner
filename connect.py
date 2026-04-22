# use the learning for the scanner
import socket
import sys




def scan_port(ip_scan, port):
    address = (ip_scan, port)
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.settimeout(0.5)
    if mySocket.connect_ex(address) == 0:
        try:
            ser = socket.getservbyport(address[1])
        except:
            ser = "unknown"
        print("Port ", address[1], " is OPEN and Service: ", ser )
    else:
        print("PORT ", address[1], " is CLOSED")
    mySocket.close()

def scan_range(ip_scan, range_first, range_end):
    with open("openPorts.txt", "a") as f:
        for i in range(range_first, range_end + 1):
            mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mySocket.settimeout(0.5)
            address = (ip_scan, i)
            print("Scanning Port: ", i)
            if mySocket.connect_ex(address) == 0:
                try:
                    n = socket.getservbyport(i)
                except:
                    n = "unknown"
                f.write(str(i) + " is Open and Service: " + n + "\n")
            else:
                pass
            mySocket.close()


if __name__ == "__main__":

    #print(len(sys.argv))
    if len(sys.argv) < 3:
        print("You need min. 2 Arguments")
        sys.exit(1)
    elif len(sys.argv) == 3:
        ip_scan = sys.argv[1]
        port = int(sys.argv[2])
        scan_port(ip_scan, port)
    elif len(sys.argv) == 4:
        ip_scan = sys.argv[1]
        range_first = int(sys.argv[2])
        range_end = int(sys.argv[3])
        scan_range(ip_scan, range_first, range_end)
    else:
        print("Wrong number of Arguments use help for help")



