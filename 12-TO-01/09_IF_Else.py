# conditional statement
# if - elif - else

ip = input("Enter source ip:") 
port = input("Enter destination port:")

blocked_ip = ["10.1.1.5","10.0.0.6","203.1.1.10","10.1.1.10"] #list
allowed_port = ["80","443","22","21"]

if ip in blocked_ip:
    print("DENY:This IP IS Blocked.!")
elif not port in allowed_port:
    print("DENY:This port is not allowed.!")
elif not ip.startswith("192.168."):
    print("DENY:Only allowed Class C IP.")
else:
    print("Allow.!")
    