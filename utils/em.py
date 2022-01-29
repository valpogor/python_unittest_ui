from email import message
import smtplib
import unittest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def sendEmail(m):
    me1 = os.environ['EMAIL']
    my_password1 = os.environ['PASSWORD']
    me = '${{ secrets.EMAIL }}'
    my_password = r'${{ secrets.PASSWORD }}'
    me2 = '${{ secret.EMAIL }}'
    my_password2 = r'${{ secret.PASSWORD }}'
    print(me)
    print(my_password)
    print(me1)
    print(my_password1)
    print(me2)
    print(my_password2)
    # secret = {{ secret.GIT_TOKEN }}.
    # msg = MIMEMultipart('alternative')
    # msg['Subject'] = "Lucky numbers"
    # msg['From'] = me
    # msg['To'] = me

    # # html = '<html><body><p>Hi, I have the following numbers for you!</p>/br<p>'+m+'</p></body></html>'
    # part2 = MIMEText(m, 'html')
    # msg.attach(part2)
    # s = smtplib.SMTP_SSL('smtp.gmail.com')
    # s.login(me, my_password)
    # s.sendmail(me, me, msg.as_string())
    # s.quit()


class unit(unittest.TestCase):
    def setUp(self):
        return self

if __name__ == "__main__":
    unittest.main()