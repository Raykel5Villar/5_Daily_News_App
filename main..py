import requests
from send_email import send_email

api_key = "0a16afc8fb7f49b6bb20eaa6135a1c1f"
url = "https://newsapi.org/v2/everything?q=apple&from=2024-05-06&to=2024-05-06&sortBy=popularity&apiKey=0a16afc8fb7f49b6bb20eaa6135a1c1f"

# Make Request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
for article in content['articles']:
    if article['title'] is not None:
        body = body + article['title'] + "\n" + article['description'] + 2*"\n"
    
body = body.encode("utf-8")
send_email(message=body)