# -*- coding: UTF-8 -*-
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime
def init_policy_commit_email(email_data):
    content = u"""

    """
    return content.format(**email_data)



class PyEmailMessage():
    _email = ''
    _password = ''
    _email_server = ''

    def __init__(self, recipients, cc, subject, content, files=None):
        """
        :param recipients: list
        :param cc: list
        :param subject: str email subject
        :param content: str email content
        :param files: list email attachments
        """
        msg = MIMEMultipart('alternative')
        msg['From'] = self._email
        msg['To'] = ','.join(recipients)
        msg['Cc'] = ','.join(cc)
        msg['Subject'] = subject
        msg.attach(MIMEText(content, 'html', 'utf-8'))
        if files:
            for f in files:
                file_name = f['name']
                file_content = f['content']
                att = MIMEApplication(file_content)
                att.add_header('Content-Disposition', 'attachment', filename= '=?utf-8?b?' + base64.b64encode(file_name.encode('UTF-8')) + '?=')
                msg.attach(att)
        self.recipients = recipients
        self.cc = cc
        self.msg = msg.as_string()

    def send(self):
        smtp = smtplib.SMTP(self._email_server)
        smtp.ehlo()
        smtp.esmtp_features["auth"] = "LOGIN AUTH"
        smtp.login(self._email, self._password)
        smtp.sendmail(self._email, self.recipients+self.cc, self.msg) 


if __name__ == '__main__':
	pass