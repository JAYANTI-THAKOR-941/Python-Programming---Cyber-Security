# list and tuple in python
# 
#
ALLOWED_PORT = (22,80,443)

open_ports = [4080,80,22,3399,8080,21,5000,443]

unexpected = []

allowed_found = []


for port in open_ports:
    if port in ALLOWED_PORT:
        allowed_found.append(port)
    else:
        unexpected.append(port)

unexpected.sort()

print(F"Total Open Ports:{len(open_ports)}")
print(F"Total Allowed Ports:{len(allowed_found)}")
print(F"Total Unexcepted Ports:{len(unexpected)}")

print()

if unexpected:
    print("Review this ports.")
    for i,port in enumerate(unexpected,start=1):
        print(f"{i}.Port : {port}")
else:
    print("All open ports are allowed ports.")



