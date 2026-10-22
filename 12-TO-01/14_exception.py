# Exception handling in python

# try:
#     number = int(input("Enter any number:"))
#     print("Square:",number*number)
# except ValueError:
#     print("Please enter valid number.!")


# try:
#     number1 = int(input("Enter any number1:"))
#     number2 = int(input("Enter any number2:"))
#     x = number1 / number2
#     print("Division:",x)
# except ZeroDivisionError:
#     print("Can not divide by zero.!")


try:
    number1 = int(input("Enter any number1:"))
    number2 = int(input("Enter any number2:"))
    x = number1 / number2
    print("Division:",x)
    
except ZeroDivisionError:
    print("Can not divide by zero.!")

except ValueError:
    print("Enter valid valu.!!")