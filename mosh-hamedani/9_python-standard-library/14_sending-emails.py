from email.mime.multipart import MIMEMultipart #MIME = Multipurpose Internet Mail Extensions. It's a sub-package in email package
from email.mime.text import MIMEText
import smtplib


message = MIMEMultipart()
message["from"] = "Md Zaman"
message["to"] = "xxxxxx"
message["subject"] = "This is a test"
message.attach(MIMEText("Body", ))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("xxxxxxxx", "xxxxxx")
    smtp.send_message(message)
    print("Sent...")



