import requests
import os
def send_message():
	template=open("newsletter_template.html")
	return requests.post(
		"https://api.mailgun.net/v3/daily.bytesizenewsletter.tech/messages",
		auth=("api", os.getenv('MAILGUN_API_KEY')),
		data={"from": 'ByteSized 🍪<newsletter@bytesizenewsletter.tech>',
			"to": ["daily@daily.bytesizenewsletter.tech",],
			"subject": "Hello",
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
r=add_new_member()
print(r.text,r.status_code)