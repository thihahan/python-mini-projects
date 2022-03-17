import smtplib
from email.message import EmailMessage
# import os
#
#
# EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
# print(f"{EMAIL_ADDRESS}: {EMAIL_PASSWORD}")
msg = EmailMessage()
msg['Subject'] = 'This is html email'
msg['From'] = 'csecse924@gmail.com'
msg['To'] = 'thih41232@gmail.com'
msg.set_content('as a developer')
msg.add_alternative("""
<!DOCTYPE html>
<html lang="en">
<body>
  <h1>This is html email</h1>
  <p>hello world</p>
</body>
</html>

""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('csecse924@gmail.com', 'thihahan9')
    smtp.send_message(msg)

