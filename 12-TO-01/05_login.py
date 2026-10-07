correctUsername = "prakshal#123"
correctPassword = "123@pipl"

username = input("Enter username:")
password = input("Enter password:")

if username == correctUsername and password == correctPassword:
    print("Login successfully.!")
    print("Welcome in Prakshal Router Config..!!")
else:
    print("ERROR:Invalid username and password.!")
