from email.message import EmailMessage
from password_forEmail import password
import ssl
import smtplib
email_sender = 'varshneyabhinav66@gmail.com'
email_password = password
email_reciever = '221b013@juetguna.in'
subject = 'Practicing python email module'
body = "I'm Abhinav Varshney and I want to become a pro programmer and fantastic developer."
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    print("EMAIL SEND HO GYA HAI")
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())