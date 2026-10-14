
server = {
    "name":"LAB-SERVER 01",
    "ip":"192.168.1.14",
    "port":8080,
    "is_online":True
}

# print(server)
# print(len(server))

# print(server["name"])
# print(server["os"]) # error
# print(server.get("os","Not available"))

# server["os"] = "RedHat Server"
# server["port"] = 8000

# print(server.pop("port"))
# print(server.pop("os","Not Available"))
# print(server)

# for key in server:
#     print(key)

# for value in server.values():
#     print(value)

# for key,value in server.items():
#     print(f"{key.upper()} : {value}")

# set

# ports = {80,22,80,33,443,22}
# print(ports)

# ips = ["10.0.0.5", "10.0.0.7", "10.0.0.5", "10.0.0.9", "10.0.0.7"]

# ips.append("10.0.0.8")
# ips.remove("10.0.0.5")
# unique_ips = set(ips)

# print(unique_ips)


allowed = {22, 80, 443}
open_ports = {22, 80, 3389, 21}

# print(allowed & open_ports)
# print(allowed | open_ports)
print(open_ports - allowed)