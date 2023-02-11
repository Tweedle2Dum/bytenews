import requests
import os

def send_simple_message():
	template=open("newsletter_template.html")
	return requests.post(
		"https://api.mailgun.net/v3/sandbox8a3862acac9b45fe87fb5f9404836bc0.mailgun.org/messages",
		auth=("api", os.getenv("MAILGUN_API_KEY")),
		data={"from": "Excited User <technewletter@technews.me>",
			"to": ["sankhayan2002@gmail.com",],
			"subject": "Hello",
			"html":template})


r=send_simple_message()
print(r.text)