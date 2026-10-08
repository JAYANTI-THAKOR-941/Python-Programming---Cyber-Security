
ip = input("Enter source ip:")
port = input("Enter destination port:")

blocked_ip = ["10.1.1.5","203.0.0.5","10.0.0.6"]
allowed_port = ["22","443","80"]

if ip in blocked_ip:
    print("DENY:this IP in blacklist..!")
elif not port in allowed_port:
    print("DENY:this port is not allowed.!!")
elif not ip.startswith("192.168."):
    print("DENY:Only allow class C IP.")
else:
    print("Allow.!")