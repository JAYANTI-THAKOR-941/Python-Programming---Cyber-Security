username = "admin"

print("-"*40)

print("username:",username)
print("type:",type(username))
print("length of string:",len(username))

# print("c:\\admin\\python")
host = "localhost" # 0 1 2 3 4 5 
port = "8000"

print(host+":"+port)


# print(f"host is {host} and port is {port} ")
print(f"connecting {host}:{port} ")

parts = ["192","168","1","5"]
print(".".join(parts))

print(host[0:5])