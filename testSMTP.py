#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText 

to = 'wenting5@ualberta.ca'
user ='zwt467875460@gmail.com'
pwd = '489512Zwt'

msg = MIMEText('Test Body!')
msg['Subject'] = 'Test Subject'
msg['From']='wenting'
msg['To']='wenting5@ualberta.ca'
msg['Reply-To'] = "zwt467875460@yahoo.com"
print(msg.as_string())

smtpserver = smtplib.SMTP('smtp.gmail.com',587)
print('find server!')
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(user,pwd)
print('Login OK!')
#header = 'To:' + to + '\n' + 'From: ' + 'mailTest@shopify.com' + '\n' + 'Subject:Test! \n'
#msg = header + '\n Place Order#200 \n\n'
smtpserver.sendmail(user, to, msg.as_string())
print ('Done!')
smtpserver.close()