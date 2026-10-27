
import requests

res = requests.get("https://jsonplaceholder.typicode.com/users/2",timeout=5)

# print(res.status_code)
# print(res.encoding)
# print(res.headers)
# print(res.json())                              

if res.status_code == 200:
    data = res.json()
    # print("name:",data["name"])
    # print("email:",data["email"])

    for key,value in data.items():
        if key == "address":
            print("Address:")
            for x,y in data['address'].items():
                print(f"\t{x} : {y}")
        else:
            print(f"{key} : {value}")
else:
    print("Server error.!")