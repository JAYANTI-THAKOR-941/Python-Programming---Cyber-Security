# request library

import requests

res = requests.get("https://jsonplaceholder.typicode.com/users/1",timeout=2)

print("status code:",res.status_code)

if res.status_code == 200:
    data = res.json()
    print("Name:",data["name"])
    print("Email:",data["email"])
else:
    print("Something went wrong")