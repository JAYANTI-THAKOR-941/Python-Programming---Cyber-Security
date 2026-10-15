
# def greetUser(name="User"):
#     print(f"Hello,{name}")

# greetUser("Dhruv")
# greetUser("Krish")
# greetUser("Ajay")
# greetUser()


# def addition(n1,n2):
#     return n1+n2

# print("Addition:",addition(50,30))

def addition(*nums):
    return sum(nums)

print("Addition:",addition(50,30,50,20))
print("Addition:",addition(50,30,50,20,40,30))