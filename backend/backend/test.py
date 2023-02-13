import requests

def test():
    url="http://localhost:8000/create"
    data = {
        "email":"sankhayan2002@gmail.com",
        }
    print(data)
    r = requests.post(url, json=data)
    print(r.text,r.status_code)
test()