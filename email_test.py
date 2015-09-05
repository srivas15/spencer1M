import smtplib

sender = 'sharoon.srivastava@yahoo.com'
receivers = ['srivas15@purdue.edu']

message = """From: From Person <sharoon.srivastava@yahoo.com>
To: To Person <srivas15@purdue.edu>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

#try:
smtpObj = smtplib.SMTP('localhost')
smtpObj.sendmail(sender, receivers, message)         
print "Successfully sent email"
#except SMTPException:
#   print "Error: unable to send email"
