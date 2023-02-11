import requests

def test():
    url="http://localhost:8080/delete/test@gmail.com"
    data = {
        "email":"test@gmail.com",
        }
    print(data)
    r = requests.delete(url, json=data)
    print(r.text)
test()