# import smtplib
# from email.mime.image import MIMEImage
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from getpass import getpass

# # sending-only capability email with smtp

# SMTP_SERVER = 'smtp-mail.outlook.com'  # 'smtp.gmail.com'
# SMTP_PORT = 25  # 465


# def send_email(sender, recipient):
#     """ Send email message """
    
#     message = MIMEMultipart('alternative')
#     message['Subject'] = 'Test'
#     message['From'] = sender
#     message['To'] = recipient

#     message.attach(MIMEText('# A Heading\nSomething else in the body', 'plain'))
#     message.attach(MIMEText('<h1 style="color: blue">A Heading</a><p>Something else in the body</p>', 'html'))

#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(sender, 'Mauvidgam220984')
#     server.sendmail(sender, recipient, message.as_string())
#     server.quit()


# if __name__ == '__main__':
#     sender = 'maulberto3@hotmail.com'
#     recipient = 'maulberto3@hotmail.com'
#     send_email(sender, recipient)