
import socket

print(socket.gethostname())
print(socket.gethostbyname("localhost"))
print(socket.gethostbyname(socket.gethostname()))
print(socket.gethostbyname("google.com"))
