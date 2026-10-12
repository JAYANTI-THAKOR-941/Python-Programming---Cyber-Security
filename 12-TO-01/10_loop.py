# loop in python

correctPassword = "Ravi@123"

passwordList = [
    "ravi123",
    "123",
    "admin",
    "ravi@123",
    "ravi#123",
    "12345678",
    "Ravi@123",
    "12345",
    "user123",
    "Ravi#123"
]

for password in passwordList:
    if password == correctPassword:
        print("\nPassword found.!")
        print("Correct Password:",password)
        break
    else:
        print("Password does not matched.!")

