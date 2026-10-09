correctUsername = "prakshal#123"
correctPassword = "123@pipl"
correctPIN = "151525"

username = input("Enter username:")
password = input("Enter password:")

if username == correctUsername and password == correctPassword:
    SECURITY_PIN = input("Enter PIN:")
    if SECURITY_PIN == correctPIN:
        print("Login successfully.!")
        print("Welcome in Prakshal Router Config..!!")
    else:
        print("Incorrect PIN..!!")
    
else:
    print("ERROR:Invalid username and password.!")
