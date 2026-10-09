# conditional statement
ip = input("Enter source IP:")
port = input("Enter destination port:")

blacklist_ip = ["10.1.1.5","10.0.0.3","203.0.0.8"]
allowed_ports = ["80","443","22"]

if ip in blacklist_ip:
    print("DENY:This IP is in Blacklist.!")
elif not port in allowed_ports:
    print("DENY:This port is not allowed.!")
elif not ip.startswith("192.168"):
    print("DENY:Only allowed class C IP.")
else:
    print("Allow.")