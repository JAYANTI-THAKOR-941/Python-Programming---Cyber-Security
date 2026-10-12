# loop in python

correctPassword = "admin@123"

passwordList = [
    "admin",
    "123",
    "Admin@123",
    "admin#123",
    "1234",
    "admin@123",
    "12345678",
    "user123"
]

for password in passwordList:
    if password == correctPassword:
        print("\nMatch success.!")
        print("Correct Password:",password)
        break
    else:
        print("Password does not matched.!")