cisco_username = "admin"
cisco_password = "admin@123"

username = input("Enter username:")
password = input("Enter password:")

if username == cisco_username and password == cisco_password:
    print("You are login successfully.")
else:
    print("ERROR:Invalid username and password.!")