import smtplib, ssl
import imghdr
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Check this file'
msg['From'] = 'csecse924@gmail.com'
msg['To'] = 'thih41232@gmail.com'
msg.set_content('Image attached...')

files = ['cir.jpg', 'wall6.jpeg']
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('csecse924@gmail.com', 'thihahan9')
    smtp.send_message(msg)

    