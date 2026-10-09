correctPassword = "admin@123"

passwordList = [
    "admin",
    "admin#123",
    "123",
    "admin@123",    
    "system"
]

for password in passwordList:
    if password == correctPassword:
        print("Access granted.!!")
        print("correct password:",password)
        break
    else:
        print("No password match.!")
    

