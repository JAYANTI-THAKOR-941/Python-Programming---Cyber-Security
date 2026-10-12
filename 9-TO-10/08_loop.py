# loop in python

correctPassword = "123"

passwordList = [
    "yash123",
    "yash@123",
    "123",
    "12345678",
    "Yash#123",
    "12345",
    "admin"
]

for password in passwordList:
    if password == correctPassword:
        print("Password Matched.!")
        print("Login successfully.")
        print("Correct password:",password)
        break
    else:
        print("Password does not match.!")
