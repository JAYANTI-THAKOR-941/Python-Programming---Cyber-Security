cisco_username = "admin"
cisco_password = "admin@123"
security_pin = "151525"

attempt = 0

while attempt < 3:
    username = input("Enter username:")
    password = input("Enter password:")

    attempt +=1

    if username == cisco_username and password == cisco_password:
        PIN = input("Enter PIN:")
        if PIN == security_pin:
            print("You are login successfully.")
        else:
            print("Incorrect PIN.")
        break
    else:
        print("ERROR:Invalid username and password.!")
else:
    print("Account loacked.!")