# coding: utf-8
import base64
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class PyEmailMessage():
    _email = ''
    _password = ''
    _email_server = ''
    _port = 25

    def __init__(self, recipients, cc, subject, contents, files=None):
        """
        :param recipients: list e.g. ['sun@gmail.com', 'moon@gmail.com']
        :param cc: list e.g. ['jupiter@gmail.com', 'mars@gmail.com']
        :param subject: str email subject
        :param contents: list email content e.g. [{'content': 'xxx', 'type': 'plain'}, {'content': 'xxx', 'type': 'html'}]
        :param files: list email attachments e.g. [{'name': 'hhh.xls', content: file raw object}]
        """
        msg = MIMEMultipart('alternative')
        msg['From'] = self._email
        msg['To'] = ','.join(recipients)
        msg['Cc'] = ','.join(cc)
        msg['Subject'] = subject
        for content in contents:
            msg.attach(MIMEText(content['content'], content['type'], 'utf-8'))
        if files:
            for f in files:
                file_name = f['name']
                file_content = f['content']
                att = MIMEApplication(file_content)
                # 处理中文附件下载文件名乱码
                att.add_header('Content-Disposition', 'attachment',
                               filename='=?utf-8?b?' + base64.b64encode(file_name.encode('UTF-8')) + '?=')
                msg.attach(att)

        self.recipients = recipients
        self.cc = cc
        self.msg = msg

    def reset_email_server(self, email, password, server, port=25):
        self._email = email
        self._password = password
        self._email_server = server
        self._port = port
        self.msg.replace_header('From', self._email)

    def send(self):
        smtp = smtplib.SMTP(self._email_server, port=self._port)
        smtp.ehlo()
        smtp.esmtp_features["auth"] = "LOGIN AUTH"
        smtp.login(self._email, self._password)
        smtp.sendmail(self._email, self.recipients+self.cc, self.msg.as_string())
        smtp.quit()
        return True

    def ssl_send(self):
        smtp = smtplib.SMTP(self._email_server, port=self._port)
        smtp.starttls()
        smtp.ehlo()
        smtp.esmtp_features["auth"] = "LOGIN AUTH"
        smtp.login(self._email, self._password)
        smtp.sendmail(self._email, self.recipients + self.cc, self.msg.as_string())
        smtp.quit()
        return True