# setup two factor authentication in our gmail account

# generate app password

# create a function to send mail

# Import email library
from email.message import EmailMessage 
from app_variable import password
import ssl
import smtplib

email_sender = "harunaalvin69@gmail.com"
email_password = password

email_receiver = "harunaalvin@yahoo.com"

subject = "Don't forget to subscribe"
body = """
when you watch a video, please subscribe. """

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
