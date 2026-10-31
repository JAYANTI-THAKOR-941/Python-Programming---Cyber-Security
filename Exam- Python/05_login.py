"""
Program 05 : Login System (input + nested if-else)
Cyber Expert : Jayanti Thakor

Definition:
    input() function user se keyboard par data leta hai (hamesha string me).
    Nested if-else matlab if ke andar dusra if. Pehli condition true ho tabhi
    andar wali condition check hoti hai (jaise username/password ke baad PIN).
"""

correctUsername = "admin@123"
correctPassword = "123@pass"
correctPIN = "121233"

username = input("Enter username:")
password = input("Enter password:")

# nested if else statement
if username == correctUsername and password == correctPassword:
    SECURITY_PIN = input("Enter PIN:")
    if SECURITY_PIN == correctPIN:
        print("Login Successfully.!")
    else:
        print("Incorrect PIN.")
else:
    print("Error: Invalid username and password.!")

# Output (sahi data par):
# Enter username:admin@123
# Enter password:123@pass
# Enter PIN:121233
# Login Successfully.!
