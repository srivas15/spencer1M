import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
GMAIL_USERNAME = 'sharoon.srivastava@gmail.com'
GMAIL_PASSWORD = 'pass' #CAUTION: This is stored in plain text!

recipient1 = 'srivas15@purdue.edu'
recipient2 = 'sharoon.srivastava@yahoo.com'
subject = 'SPENCER FC HAS 1 MILLION SUBS!!!'
emailText = "<h1>Congrats! spencerFC has 1 million subs now</h1><h2><a href = 'https://www.youtube.com/user/officialfifaplaya'>Check it out !</a></h2><h6>This email was sent to you by a bot build by Sharoon Srivastava. <a href = 'https://github.com/srivas15/spencer1M'>Click here</a> to know more</h6><img src='https://yt3.ggpht.com/-UFb7taJXzCQ/AAAAAAAAAAI/AAAAAAAAAAA/QKhwKUfUTio/s900-c-k-no/photo.jpg'>"

emailText = "" + emailText + ""

headers1 = ["From: " + GMAIL_USERNAME,
           "Subject: " + subject,
           "To: " + recipient1,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers1 = "\r\n".join(headers1)

headers2 = ["From: " + GMAIL_USERNAME,
           "Subject: " + subject,
           "To: " + recipient2,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers2 = "\r\n".join(headers2)

session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

session.ehlo()
session.starttls()
session.ehlo

session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

session.sendmail(GMAIL_USERNAME, recipient1, headers1 + "\r\n\r\n" + emailText)
session.sendmail(GMAIL_USERNAME, recipient2, headers2 + "\r\n\r\n" + emailText)
session.quit()
