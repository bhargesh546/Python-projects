import os, smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")

html = Template(Path("index.html").read_text())

email = EmailMessage()

email["from"] = user
email["to"] = user
email["subject"] = "Test Email"

email.set_content(html.substitute(name = "Brad"), "html")

with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465) as smtp:
    smtp.login(user, password)
    smtp.send_message(email)
    print("Done!")