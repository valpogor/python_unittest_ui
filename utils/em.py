from email import message
import smtplib
import unittest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def sendEmail(m):
    me = os.environ['EMAIL']
    my_password = os.environ['PASSWORD']
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Lucky numbers"
    msg['From'] = me
    msg['To'] = me
    part2 = MIMEText(m, 'html')
    msg.attach(part2)
    s = smtplib.SMTP_SSL('smtp.gmail.com')
    s.login(me, my_password)
    s.sendmail(me, me, msg.as_string())
    s.quit()

class unit(unittest.TestCase):
    def setUp(self):
        return self

if __name__ == "__main__":
    unittest.main()