"""
Program 08 : for Loop (Password Guessing)
Cyber Expert : Jayanti Thakor

Definition:
    Loop ek code block ko baar-baar chalata hai.
    for loop kisi sequence (list, string, range) ke har item par chalta hai.
    break  = loop ko turant rok deta hai.
    range(start, stop) = start se stop-1 tak numbers deta hai.
"""

correctPassword = "123"
passwordList = ["yash123", "yash@123", "123", "12345678", "admin"]

for password in passwordList:
    if password == correctPassword:
        print("Password Matched.!")
        print("Correct password:", password)
        break
    else:
        print("Password does not match.!")

# range() example
for i in range(0, 3):
    print(f"192.168.1.{i}")

# Output:
# Password does not match.!
# Password does not match.!
# Password Matched.!
# Correct password: 123
# 192.168.1.0
# 192.168.1.1
# 192.168.1.2
