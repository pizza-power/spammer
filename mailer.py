#!/usr/bin/python3

import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

# open a text file containing one email address per line
with open("emails.txt") as f:
    emails = f.readlines()

emails = [email.strip() for email in emails]

IP = ""  # put the IP of the server here
PORT = 25  # put port number here

mailserver = smtplib.SMTP(IP, PORT)
# if attaching a file, put it here
files = []  # Example: "/home/user/contacts.txt"

try:
    mailserver.ehlo()

    for email in emails:
        try:
            msg = MIMEMultipart()
            msg["From"] = "example@example.com"  # put your email here
            msg["To"] = email
            msg["Subject"] = "subject"  # put the subject line here
            message = "message"  # put the message here
            msg.attach(MIMEText(message))

            for f in files or []:
                with open(f, "rb") as fil:
                    part = MIMEApplication(fil.read(), Name=basename(f))
                # After the file is closed
                part[
                    "Content-Disposition"
                ] = 'attachment; filename="%s"' % basename(f)
                msg.attach(part)

            mailserver.sendmail("example@example.com", email, msg.as_string())
            print("email sent to %s" % email)
        except:
            print("could not send email")

except:
    print("error connecting")
