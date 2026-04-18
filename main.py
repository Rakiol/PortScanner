#first try´s

import os, socket
from os import read

HOST = ("127.0.0.1", 65432)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(HOST)
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)




#inp = input("Please enter an IP address: ")
'''
try:
    if not os.path.exists("ScanData.txt"):
        with open("ScanData.txt", "w") as file:
            file.write("Sample")
    else:
        file = open("ScanData.txt", "w")
        file.write("sample2")
except:

    print("Error")
'''
