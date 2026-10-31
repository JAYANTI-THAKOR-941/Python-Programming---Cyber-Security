"""
Program 02 : Variable
Cyber Expert : Jayanti Thakor

Definition:
    Variable ek naam hota hai jo memory me data store karta hai.
    Python me variable banane ke liye data type batana zaroori nahi hai.
    Common data types : int (80), float (3.5), str ("admin"), bool (True/False).
"""

target_ip = "192.168.1.26"   # str
port = 80                    # int
is_online = True             # bool

print("Target IP :", target_ip)
print("PORT      :", port)
print("Online    :", is_online)

# Variable ki value change ho sakti hai
attempts = 1
print("Attempts count:", attempts)
attempts = 2
print("Attempts count:", attempts)

# Multiple assignment
host, port = "localhost", 5000
print(host, port)

# type() se data type pata chalta hai
print(type(target_ip), type(port), type(is_online))

# Output:
# Target IP : 192.168.1.26
# PORT      : 80
# Online    : True
# Attempts count: 1
# Attempts count: 2
# localhost 5000
# <class 'str'> <class 'int'> <class 'bool'>
