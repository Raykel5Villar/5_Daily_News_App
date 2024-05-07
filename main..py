import requests
from send_email import send_email
import os

topic = "Python"
api_key = "0a16afc8fb7f49b6bb20eaa6135a1c1f"
url = f'https://newsapi.org/v2/everything?q={topic}&from=2024-05-06&to=2024-05-06&sortBy=popularity&apiKey=0a16afc8fb7f49b6bb20eaa6135a1c1f'

# Make Request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = "Subject: Today's news Python\n"
for article in content['articles'][:20]:
    if article['title'] is not None:
        body += article['title'] + "\n" + article['description'] + "\n" + article['url'] + 2*"\n"
    
body = body.encode("utf-8")
send_email(message=body)

