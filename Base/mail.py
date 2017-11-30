# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
msg = MIMEText("just a text mail")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of code named strawberry'
msg['From'] = 'noreply@mail.6-79.cn'
msg['To'] = 'i@6-79.cn'

# Send the message via our own SMTP server.
s = smtplib.SMTP('smtp.qq.com', 465)
s.send_message(msg)
s.quit()
