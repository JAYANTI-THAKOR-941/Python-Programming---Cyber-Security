
def getPort():
    port = int(input("Enter port:"))
    if not 0<= port <=65535:
        raise ValueError(f"{port} is out range.!")
    return port

try:
    print("Valid port:",getPort())
except ValueError as e:
    print(e)
