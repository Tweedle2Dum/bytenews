import requests

def test():
    url="http://localhost:8080/create"
    data = {
        "email":"test1@gmail.com",
        }
    print(data)
    r = requests.post(url, json=data)
    print(r.text,r.status_code)
test()