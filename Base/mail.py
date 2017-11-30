import smtplib
import email

msg = email.message.Message()
msg['From'] = 'noreply@mail.6-79.cn'
msg['To'] = 'i@6-79.cn'
msg['Subject'] = 'Test message'
server = smtplib.SMTP('smtp.qq.com', 587)
server.starttls()
server.ehlo_or_helo_if_needed()
try:
    failed = server.sendmail('noreply@mail.6-79.cn', 'i@6-79.cn', msg.as_string())
    server.close()
except Exception as e:
    print(e)
