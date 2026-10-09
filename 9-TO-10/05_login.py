# Login
correctUsername = "prakshal@123"
correctPassword = "123@pipl"
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
    print("Error:Invalid username and password.!")


