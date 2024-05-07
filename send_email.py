import smtplib, ssl
import json


def send_email(message):
    with open('config.json') as config_file:
        config = json.load(config_file)
    password = config['gmail_app_password']

    host = "smtp.gmail.com"
    port = 465

    username = "raykelvillar50@gmail.com"

    receiver = "raykelvillar@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)