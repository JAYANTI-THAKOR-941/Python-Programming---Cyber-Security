# simple login 
correctUsername = "admin@123"
correctPassword = "123@pipl"
PIN  = "121233"
MAX_ATTEMPT = 0
attempt = 0

while  attempt< MAX_ATTEMPT:
    userName = input("Enter username:")
    password = input("Enter password:")
    attempt += 1

    if userName == correctUsername and password == correctPassword:
        SECURITY_PIN = input("Enter Security PIN:")
        if SECURITY_PIN == PIN:
            print("Login successfully.!")
            print("Welcome admin.!")
        else:
            print("Your PIN is Incorrect.!")
    else:
        print("Invalid username and password.!")
else:
    print("You are blocked.!")


