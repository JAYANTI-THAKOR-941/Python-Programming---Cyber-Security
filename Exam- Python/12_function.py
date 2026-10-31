"""
Program 12 : Function
Cyber Expert : Jayanti Thakor

Definition:
    Function code ka reusable block hai jo 'def' keyword se banta hai.
    Ek baar likho, kai baar call karo.
        Parameter = function ke andar ka variable
        Argument  = call karte waqt di gayi value
        return    = function se value wapas bhejta hai
        *args     = kitne bhi arguments le sakta hai
"""

# 1. Simple function
def greetUser():
    print("Hii User..!")

# 2. Parameter wala function
def greetMsg(name):
    print(f"Welcome, {name}")

# 3. return wala function
def checkPort(port):
    if port in (22, 80, 443):
        return "Allowed"
    return "Blocked"

# 4. *args wala function
def calc(*num):
    return sum(num)

greetUser()
greetMsg("Yash")
print("Port 80   :", checkPort(80))
print("Port 3389 :", checkPort(3389))
print("Addition  :", calc(50, 5, 8))
print("Addition  :", calc(50, 5, 8, 14, 80))

# Output:
# Hii User..!
# Welcome, Yash
# Port 80   : Allowed
# Port 3389 : Blocked
# Addition  : 63
# Addition  : 157
