
import requests

res = requests.get("https://jsonplaceholder.typicode.com/users/2",timeout=5)

print("status:",res.status_code)

# print(res.json())

# print(res.headers)
print(res.encoding)

# if res.status_code == 200:
#     data = res.json()
#     # print("name:",data["name"])
#     # print("email:",data["email"])

#     for key,value in data.items():
#         print(f"{key} : {value}")

# else:
#     print("Something went wrong.!!")