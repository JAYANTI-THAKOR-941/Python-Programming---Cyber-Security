# Exception handling in python

# try:
#     number = int(input("Enter any number:"))
#     print(f"Double : {number * 2}")
# except ValueError:
#     print("This is not a valid number.!")


# try:
#     x = 10/0
#     print("Ans:",x)
# except ZeroDivisionError:
#     print("Can not divide by zero.")

# try:
#     x = "5" + 10
#     print("ans:",x)
# except TypeError:
#     print("Type Error.!!")

try:
    x = int(input("Enter x:"))
    y = int(input("Enter y:"))
    z = x/y
    print("Division:",z)
except ValueError:
    print("Please enter valid value.!")
except ZeroDivisionError:
    print("Can not divide by zero.")