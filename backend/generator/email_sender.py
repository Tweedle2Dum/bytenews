import requests
import os

DEV_ADDRESS="sandbox8a3862acac9b45fe87fb5f9404836bc0.mailgun.org"
DEV_EMAIL="beta@sandbox8a3862acac9b45fe87fb5f9404836bc0.mailgun.org"

PROD_ADDRESS="daily.bytesizenewsletter.tech"
PROD_EMAIL="daily@daily.bytesizenewsletter.tech"
BASE_URL=f"https://api.mailgun.net/v3/"

EMAIL=PROD_EMAIL
ADDRESS=PROD_ADDRESS

def send_message():
    template=open("")
    template=template.read().replace("\n","")
    print(f"{BASE_URL}{ADDRESS}/messages")
    return requests.post(
		f"{BASE_URL}{ADDRESS}/messages",
		auth=("api", "536f3dd4ed281a2775a533ed9e590f4e-d1a07e51-509eefca"),
		data={"from": 'ByteSized 🍪<newsletter@bytesizenewsletter.tech>',
			"to": [EMAIL,],
			"subject": "Google Chrome's new battery saving feature 🔋, outlook users report broken spam filters 🗑️ and many more",
			"html":template})
def list_members():
    print(os.getenv('MAILGUN_API_KEY'))
    return requests.get(
        "https://api.mailgun.net/v3/lists/daily@daily.bytesizenewsletter.tech/members/pages",
        auth=('api',os.getenv('MAILGUN_API_KEY')))
def add_new_member():
    return requests.post(
        "https://api.mailgun.net/v3/lists/daily@daily.bytesizenewsletter.tech/members",
        auth=('api', os.getenv('MAILGUN_API_KEY')),
        data={'subscribed': True,
              'address': 'ss'})

r=send_message()
print(r.text,r.status_code)