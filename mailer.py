#!/usr/bin/python3

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open("emails.txt") as f:
    emails = f.readlines()

emails = [email.strip() for email in emails]

IP = ""  # put the IP of the server here
PORT = 25  # put port number here

mailserver = smtplib.SMTP(IP, PORT)

try:
    mailserver.ehlo()

    for email in emails:
        try:
            msg = MIMEMultipart()
            msg['From'] = "example@example.com"
            msg['To'] = email
            msg['Subject'] = "click here"
            message = "put your message here"
            msg.attach(MIMEText(message))
            mailserver.sendmail("example@example.com", email, msg.as_string())
            print("email sent to %s" % email)
        except:
            print("could not send email")

except:
    print("error connecting")
