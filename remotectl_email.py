#__codeing__ 'UTF-8'
import smtplib
import email
from email.mime.text import MIMEText
import poplib
import time
import os
ADDR = '1280354657@qq.com'
PASSWORD = 'opfvbiujenrygjbb'
FROM_ADDR = '1280354657@qq.com'   
POP_SERVER = 'pop.qq.com'
SMTP_SERVER = 'smtp.qq.com'
class Email(object):
    #初始化参数
    def __init__(self):
        self._addr = ADDR
        self._password = PASSWORD
        self._smtp_server = SMTP_SERVER
        self._pop_server = POP_SERVER
        self._from_addr = FROM_ADDR
    #连接到POP服务器
    def pop_connect(self):
        try:
           self.reademail = poplib.POP3_SSL(self._pop_server)
           self.reademail.user(self._addr)
           self.reademail.pass_(self._password)
           self.allemail = self.reademail.stat()
        except:
            print('读取邮件登录失败')
            exit()
    #提取最新邮件，解码
    def receive_email(self):
        self.pop_connect()
        topemail = self.reademail.top(self.allemail[0], 0)
        emaillist = []
        for item in topemail[1]:
           try:
               emaillist.append(item.decode('utf8'))
           except:
                try:
                   emaillist.append(item.decode('gbk'))
                except:
                   emaillist.append(item.decode('big5'))
        emailmsg = email.message_from_string('\n'.join(emaillist))
        emailsub = email.header.decode_header(emailmsg['subject'])
        if emailsub[0][1]:
           submsg = emailsub[0][0].decode(emailsub[0][1])
        else:
           submsg = emailsub[0][0]
        return submsg
    #发送邮件
    #连接SMTP服务器
    def smtp_connect(self):
        try:
           self.sendemail = smtplib.SMTP_SSL(self._smtp_server, 465)
           self.sendemail.login(self._addr, self._password)
        except:
            print('发送邮件登录失败')
            exit()
    #发送邮件
    def send_email(self):
        self.smtp_connect()
        msg = MIMEText('')
        msg['Subject'] = '设置完毕'
        msg['From'] = self._from_addr
        msg['To'] = self._addr
        self.sendemail.sendmail(self._from_addr, self._addr, msg.as_string())
        self.sendemail.close()
    def check_shutdown(self):
               submsg_list = self.receive_email().split(' ')
               print('最新邮件主题:', ' '.join(submsg_list))
               sd_type = submsg_list[0]
               if sd_type == '延时关机':
                   sd_time = '60'
                   if len(submsg_list) > 1:
                           sd_time = submsg_list[1]
                   command = 'shutdown -s -t ' + sd_time
               elif sd_type == '定时关机':
                   sd_time = '00:00'
                   if len(submsg_list) > 1:
                           sd_time = submsg_list[1]
                   command = 'schtasks /create /TN %s /ST %s /sc DAILY /TR "shutdown /s"' %(sd_type, sd_time) 
               if '关机' in sd_type:
                   os.system(command)
                   print('执行命令:', command)
                   self.reademail.quit()
                   return True
               else:
                   return False
if __name__=='__main__':
        mail = Email()
        while True:
            time.sleep(5)
            print('等待关机信号.....')
            if mail.check_shutdown():
                mail.send_email()
