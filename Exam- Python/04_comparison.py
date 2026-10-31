"""
Program 04 : Comparison and Logical Operators
Cyber Expert : Jayanti Thakor

Definition:
    Comparison operator do values ko compare karta hai aur True ya False deta hai.
        ==  (barabar)   !=  (barabar nahi)   <  >  <=  >=
    Logical operator conditions ko jodte hai :
        and = dono True ho to True
        or  = koi ek True ho to True
        not = result ulta kar deta hai
"""

a = 50
b = 30

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# Logical operators
port = 443
print("Port allowed:", port == 80 or port == 443)
print("Port allowed and secure:", port > 400 and port == 443)
print("Not 22:", not port == 22)

# Output:
# a == b : False
# a != b : True
# a > b  : True
# a < b  : False
# a >= b : True
# a <= b : False
# Port allowed: True
# Port allowed and secure: True
# Not 22: True
