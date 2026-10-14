
server = {
    "name":"SERVER - 01",
    "ip":"192.168.1.10",
    "port":8080,
    "isOnline":True
}
# print(server)
# print("SERVER Name:",server["name"])
# print(server["os"]) # error

# print(server.get("os","Not Available"))

server["os"] = "RedHat Linux"

# server["port"] = 8000

# server.update({"port":5000,"os":"windows"})
# print(server)

# print(server.pop("sysInfo","Not Available"))
# print(server)


# for key in server:
#     print(key)

# for value in server.values():
#     print(value)

# for key,value in server.items():
#     print(f"{key.title()} : {value}")


# ports = {22, 80, 443, 80, 22}
# print(ports)

# ips = ["10.0.0.5", "10.0.0.7", "10.0.0.5", "10.0.0.9", "10.0.0.7"]

# unique_ips = set(ips)
# print(unique_ips)

# ports.remove(5000)
# ports.discard(5000)


# allowed = {22, 80, 443}
# open_ports = {22, 80, 3389, 21}

# print(allowed & open_ports)
# print(allowed | open_ports)
# print(allowed - open_ports)
# print(open_ports - allowed )
# print(open_ports ^ allowed )

