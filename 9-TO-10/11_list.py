# list and tuple

ALLOWED_PORT = (22,80,443) #tuple

open_ports = [80,3389,443,21,22,8080,8000,5000] #list
 
unexcepted = [] #empty list

allowed_found = []

print("="*35)
print("PORT POLICY AUDITOR")
print("="*35)

for port in open_ports:
    if port in ALLOWED_PORT:
        allowed_found.append(port)
    else:
        unexcepted.append(port)

# sort data
unexcepted.sort()

print(f"Total Open Ports:{len(open_ports)}")
print(f"Total Allowed Ports:{len(allowed_found)}")
print(f"Total Unexcepted Ports:{len(unexcepted)}")

if unexcepted:
    print("\nReview this ports.")
    for i,port in enumerate(unexcepted,start=1):
        print(f"{i}.PORT:{port}")

else:
    print("All open port are allowed port.")