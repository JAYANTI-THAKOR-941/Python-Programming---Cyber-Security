"""
Program 11 : Dictionary and Set
Cyber Expert : Jayanti Thakor

Definition:
    Dictionary = data ko key:value pair me store karta hai. Symbol : { key: value }
                 Methods : get(), pop(), keys(), values(), items()
    Set        = unordered collection jisme duplicate values nahi hoti. Symbol : { }
                 Operations : & (intersection), | (union), - (difference)
"""

server = {
    "name": "LAB-SERVER 01",
    "ip": "192.168.1.14",
    "port": 8080,
    "is_online": True
}

print(server["name"])
print(server.get("os", "Not available"))   # key na ho to default value
server["os"] = "RedHat Server"             # naya key add

for key, value in server.items():
    print(f"{key.upper()} : {value}")

# Set
ports = {80, 22, 80, 443, 22}              # duplicate hat jate hai
print("Unique ports:", ports)

allowed = {22, 80, 443}
open_ports = {22, 80, 3389, 21}
print("Common   :", allowed & open_ports)
print("All      :", allowed | open_ports)
print("Not allowed:", open_ports - allowed)

# Output:
# LAB-SERVER 01
# Not available
# NAME : LAB-SERVER 01
# IP : 192.168.1.14
# PORT : 8080
# IS_ONLINE : True
# OS : RedHat Server
# (Note: set ka order alag-alag aa sakta hai, ye normal hai)
# Unique ports: {80, 443, 22}
# Common   : {80, 22}
# All      : {80, 22, 443, 3389, 21}
# Not allowed: {3389, 21}
