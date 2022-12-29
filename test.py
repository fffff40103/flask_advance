MY_DOMAIN_NAME="sandbox468ab229b32b4d009f4927529b3f0f3a.mailgun.org"
MY_API_KEY="055c0b06961a7d9aa24f299fe832e4bf-eb38c18d-f49e40aa"
import requests
def send_simple_message():
	return requests.post(
		f"https://api.mailgun.net/v3/{MY_DOMAIN_NAME}/messages",
		auth=("api", MY_API_KEY),
		data={"from": f"Excited User <mailgun@{MY_DOMAIN_NAME}>",
			"to": ["yunrouchen079@gmail.com",MY_DOMAIN_NAME ],
			"subject": "Hello",
			"text": "HI"})

send_simple_message()