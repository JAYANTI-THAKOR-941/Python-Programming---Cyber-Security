"""
Program 06 : String
Cyber Expert : Jayanti Thakor

Definition:
    String characters ka sequence hai jo quotes ("  " ya '  ') me likha jata hai.
    String immutable hoti hai (ek baar ban jaye to change nahi hoti).
    Common methods : lower(), upper(), strip(), replace(), len(), slicing [start:end]
"""

msg = "Hello Hackers.!"
host = "localhost"

print("Length  :", len(host))
print("Slice   :", host[0:5], "|", host[5:])
print("f-string:", f"{msg} connecting {host}:22")

username = "HACKER12@gmail.com"
print("Lower   :", username.lower())

hostname = "------lab_server-1------"
print("Upper   :", hostname.upper())
print("Strip   :", hostname.strip("-"))

port = "open port is 555"
print("Replace :", port.replace("555", "80"))

parts = ["192", "168", "1", "8"]
print("Join    :", ".".join(parts))

# Output:
# Length  : 9
# Slice   : local | host
# f-string: Hello Hackers.! connecting localhost:22
# Lower   : hacker12@gmail.com
# Upper   : ------LAB_SERVER-1------
# Strip   : lab_server-1
# Replace : open port is 80
# Join    : 192.168.1.8
