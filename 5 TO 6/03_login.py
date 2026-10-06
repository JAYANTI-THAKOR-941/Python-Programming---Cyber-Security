# simple login 
correctUsername = "admin@123"
correctPassword = "123@pipl"

userName = input("Enter username:")
password = input("Enter password:")

if userName == correctUsername or password == correctPassword:
    print("Login successfully.!!")
else:
    print("Invalid username and password.!")