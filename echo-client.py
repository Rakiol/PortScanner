#socket testing client
import socket

HOST = ("127.0.0.1", 65432)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST))
    s.sendall((b"Hello, World"))
    data = s.recv(1024)
print(f"Received {data!r}")