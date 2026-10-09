# conditional statement
# if-else and elif

ip = input("Enter source ip:")
port = input("Enter destination port:")

blocked_ip = ["192.168.1.11","10.0.0.11","10.1.1.12","203.1.1.15","192.168.1.10"]

allowed_port = ["80","443","22","21","25"]

if ip in blocked_ip:
    print("DENY:Your ip is blocked.!")
elif not port in allowed_port:
    print("DENY:This port is not allowed.!")
elif not ip.startswith("192.168."):
    print("DENY:Only allowed class C Ip.")
else:
    print("Allowed.!")
