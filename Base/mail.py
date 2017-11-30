import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "mail.6-79.cn"
mail_user = "noreply@mail.6-79.cn"
mail_pass = "password"

sender = 'noreply@mail.6-79.cn'
receivers = ['i@6-79.cn']

message = MIMEText('Python test mail...', 'plain', 'utf-8')
message['From'] = Header("runoob", 'utf-8')
message['To'] = Header("for test", 'utf-8')

subject = 'Python SMTP mail testing'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.starttls()
    smtpObj.connect(mail_host, 587)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("send success")
except smtplib.SMTPException as e:
    print(e)
