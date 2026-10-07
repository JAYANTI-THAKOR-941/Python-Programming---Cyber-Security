
password = input("Enter password:")

if len(password) >=8 and len(password)<=65:
    print("Your password strong.!")
else:
    print("Your password is too weak.")