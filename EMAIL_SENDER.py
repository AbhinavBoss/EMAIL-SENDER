from email.message import EmailMessage
from password_forEmail import password
import ssl
import smtplib
email_sender = "SENDER's EMAIL"
email_password = password
email_reciever = "RECEIVER's EMAIL"
subject = 'WRITE A SUBJECT'
body = "WRITE THE MAIN CONTENT OF THE MAIL HERE"
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    print("EMAIL SEND HO GYA HAI")  #YOU CAN WRITE ANY MESSAGE HERE
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())
