import smtplib, os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")

email = EmailMessage()

email["from"] = user
email["to"] = user
email["subject"] = "Test Email"

email.set_content("Hello from Python 😊")

"""
# Using SMTP function - here its initially unencrypted and uses starttls() to encrypt the plain connection

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()     # encryption method for security
    smtp.login("bhargesh546@gmail.com", "diyasbhar5")
    smtp.send_message(email)
    print("All done!")

"""

# Using SMTP_SSL

with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465) as smtp:
    smtp.login(user, password)
    smtp.send_message(email)
    print("Email sent")

