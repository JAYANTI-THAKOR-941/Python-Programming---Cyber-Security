
def getPort():
    port = int(input("Enter port:"))
    #  0 - 65535
    if not 0<= port <=65535:
        raise ValueError(f"Port number is out of range:{port}")
    return port

try:
    port = getPort()
    print("Given Port Number:",port)
except ValueError as e:
    print(e)