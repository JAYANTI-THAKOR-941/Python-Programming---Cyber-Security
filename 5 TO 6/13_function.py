# function in python

# definition
# def greet():
#     print("Hello Hackers.!")

# #function calling
# greet()
# greet()

# def say_Hello(name="Jayanti"):
#     print(f"Hii,{name}.Welcome to Python Course.")

# say_Hello("Krish")
# say_Hello("Ajay")
# say_Hello()
# say_Hello("Alpesh")

def get_ports(*ports):
    print("Open ports.!")
    for i,port in enumerate(ports,start=1):
        print(f"{i}.{port}")

get_ports(80,22,21,443)
get_ports(80,22,8000,5000,443)
