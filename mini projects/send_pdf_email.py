import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'myanmar to do list'
msg['From'] = 'csecse924@gmail.com'
msg['To'] = 'thih41232@gmail.com'
msg.set_content('file attached...')

with open('myanmar.pdf', 'rb') as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login('csecse924@gmail.com', 'thihahan9')
    smtp.send_message(msg)