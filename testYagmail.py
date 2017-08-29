import yagmail


yag = yagmail.SMTP('zwt467875460@yahoo.com','489512Zwt')
yag.send('wenting5@ualberta.ca', subject = 'Orders', contents = 'Hello')