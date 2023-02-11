import requests

def test():
    url="http://localhost:8080/create"
    data = {
        "email":"test@gmail.com",
        }
    print(data)
    r = requests.post(url, json=data)
    print(r.text)
test()