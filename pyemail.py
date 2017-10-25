# -*- coding: UTF-8 -*-
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime
def init_policy_commit_email(email_data):
    content = u"""
    <p>&nbsp;</p>

    <table style="line-height: 20.8px; margin: 40px auto 0px;">
        <tbody>
            <tr style="border-top-width: 1px; border-right-width: 1px; border-left-width: 1px; border-style: solid solid none; border-top-color: rgb(24, 155, 228); border-right-color: rgb(24, 155, 228); border-left-color: rgb(24, 155, 228);">
                <td style="width: 620px; padding: 0px 20px; margin: 40px 0px 0px; border-top-left-radius: 4px; border-top-right-radius: 4px; overflow: hidden; background: rgb(24, 155, 228);"><a href="http://www.2haohr.com" style="cursor: pointer;"><font color="#333333"><img src="http://cdn-dev.2haohr.com/e-dev/static/email/email_top2.png" style="padding: 20px 0px; height: 48px;" /></font></a></td>
            </tr>
            <tr style="font-family: Arial, YaHei, 黑体, 宋体, sans-serif; color: rgb(0, 0, 0); font-size: 14px; background-image: initial; background-attachment: initial; background-size: initial; background-origin: initial; background-clip: initial; background-position: initial; background-repeat: initial;">
                <td style="width: 620px; height: 450px; padding: 40px; vertical-align: sub; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-style: none solid solid; border-right-color: rgb(220, 220, 220); border-bottom-color: rgb(220, 220, 220); border-left-color: rgb(220, 220, 220); border-bottom-left-radius: 4px; border-bottom-right-radius: 4px;">
                <p style="margin: 0px 0px 20px;"><font color="#333333" face="sans-serif, Arial, Verdana, Trebuchet MS"><span style="font-size: 13px;">尊敬的用户：</span></font></p>
    
                <p style="color: rgb(50, 50, 50); line-height: 32px;"><font color="#333333" face="sans-serif, Arial, Verdana, Trebuchet MS"><span style="font-size: 13px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;您好！附件为{company_name}的</span></font>{time}<font color="#333333" face="sans-serif, Arial, Verdana, Trebuchet MS"><span style="font-size: 13px;">的雇主责任险投保清单。后续客服人员会与您联系，对清单进行确认，敬请保持联系方式畅通！</span></font></p>
    
                <p>&nbsp;</p>
    
                <p>&nbsp;</p>
    
                <p>&nbsp;</p>
    
                <p>&nbsp;</p>
    
                <p>&nbsp;</p>
    
                <p>&nbsp;</p>
    
                <p>&nbsp;</p>
    
                <p>&nbsp;</p>
    
                <hr style="margin: 20px 0; border:none; border-top:1px solid #d2d2d2;" />
                <p style="margin-bottom: 20px; text-align: center;"><a href="http://e.2haohr.com/table/desk" style="color: rgb(255, 255, 255); display: inline-block; padding: 0px 20px; line-height: 50px; border-radius: 25px; font-size: 16px; cursor: pointer; text-decoration: none; background: rgb(24, 155, 228);">立刻访问2号人事部</a></p>
    
                <p style="margin: 0px; color: rgb(50, 50, 50); line-height: 20px; text-align: center;"><font color="#333333" face="sans-serif, Arial, Verdana, Trebuchet MS"><span style="font-size: 13px;">感谢您的使用和关注！若您有任何疑问，请直接联系我们。</span></font></p>
    
                <p style="margin: 0px; color: rgb(50, 50, 50); line-height: 20px; text-align: center;"><font color="#333333" face="sans-serif, Arial, Verdana, Trebuchet MS"><span style="font-size: 13px;">{contact_information}</span></font></p>
                </td>
            </tr>
        </tbody>
    </table>
    """
    return content.format(**email_data)



class PyEmailMessage():
    _email = 'noreply@2haohr.com'
    _password = '83vJILwNOe'
    _email_server = 'mail.2haohr.com'

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
                att.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', file_name))
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
	email_data = {
		'time': u'2017年11月',
		'company_name': u'mail.company.fullname',
		'contact_information': u'客服邮箱 support@2haohr.com，客服电话 0755-26777170。'
	}
	content = init_policy_commit_email(email_data)
	subject = '花儿为什么这样红2017年12月投保清单'
	file_name = '花儿为什么这样红2017年12月投保清单.xls'
	with open('/home/eugene/workspace/eebo.ehr.welfare/static/export/insurance_10000/参保数据批量修改模板.xls', 'rb') as f:
		file_content = f.read()
	files = [{'name':file_name, 'content':file_content}]
	PyEmailMessage(['eugene@dianmi365.com'], ['237192896@qq.com'], subject, content, files).send()
