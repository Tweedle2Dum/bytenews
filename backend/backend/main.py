from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

origins = [
    #"http://localhost:8000",
    "*"
]

DEV_ADDRESS="sandbox8a3862acac9b45fe87fb5f9404836bc0.mailgun.org"
PROD_ADDRESS="daily.bytesizenewsletter.tech"
PROD_EMAIL="daily@daily.bytesizenewsletter.tech"
DEV_EMAIL="beta@sandbox8a3862acac9b45fe87fb5f9404836bc0.mailgun.org"
BASE_URL=f"https://api.mailgun.net/v3/"

EMAIL=DEV_EMAIL
ADDRESS=DEV_ADDRESS



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Email(BaseModel):
    email: str

@app.get("/")
async def root():
    print(BASE_URL)
    return {"message": "Hello World"}


def send_message(email:str):
    template=open("thankyou_template.html")
    print(f"{BASE_URL}{ADDRESS}/messages")
    return requests.post(
		f"{BASE_URL}{ADDRESS}/messages",
		auth=("api", "536f3dd4ed281a2775a533ed9e590f4e-d1a07e51-509eefca"),
		data={"from": 'ByteSized 🍪<newsletter@bytesizenewsletter.tech>',
			"to": [email,],
			"subject": "Welcome to ByteSize!",
			"html":template})

@app.post("/create")
async def create(email:Email,request: Request):
    #if request.url!="https://www.bytesizenewsletter.tech/":
    #    return {"message": "Not Found"}
    
    
    res1=requests.post(
        f"{BASE_URL}lists/{EMAIL}/members",
        auth=('api', "536f3dd4ed281a2775a533ed9e590f4e-d1a07e51-509eefca"),
        data={'subscribed': True,
              'address': email.email})
    if res1.status_code==200:
        res=send_message(email.email)
        if res.status_code==200:
            return {"message": "Created", "status_code": res.status_code, "data": res.text}
        else:
            res2=requests.delete(
            f"{BASE_URL}lists/{EMAIL}/members/{email.email}",
            auth=('api', "536f3dd4ed281a2775a533ed9e590f4e-d1a07e51-509eefca"))
            return {"message": "Error", "status_code": res.status_code, "data": res.text,"Removed status": res2.status_code, "User has been removed": res2.text}
    else:
        return {"message": "Bruh", "status_code": res1.status_code, "data": res1.text}