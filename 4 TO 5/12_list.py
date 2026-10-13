# list and tuple in python

# tuple
ALLOWED_PORT = (22,80,443) 

# list
open_ports = [22,80,5000,8080,443,3389,21,24]

unexcepted = []
allowed_found = []

print()

for port in open_ports:
    if port in ALLOWED_PORT:
        allowed_found.append(port)
    else:
        unexcepted.append(port)

print()

unexcepted.sort()

print(f"Total Open Ports:{len(open_ports)}")
print(f"Total Allowed Ports:{len(allowed_found)}")
print(f"Total Unexcepted Ports:{len(unexcepted)}")


print()

if unexcepted:
    print("Review this ports.")
    for i,port in enumerate(unexcepted,start=1):
        print(f"{i}.PORT:{port}") 
else:
    print("All open ports are allowed ports.")