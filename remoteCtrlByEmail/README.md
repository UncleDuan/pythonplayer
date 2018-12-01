
# remotectrlbyemail
remote shoudown computer by monitoring email.<br>
用到的模块:<br>
smtplib：<br>
连接到SMTP服务器<br>
poplib：<br>
连接到POP服务器<br>
time<br>
email<br>

os<br>
MIMEText,这个在email.mime.text里面<br>

### 1.提取最新邮件
先连接到到pop服务器：
```python
def pop_connect(self):
        try:
           self.reademail = poplib.POP3_SSL(self._pop_server)
           self.reademail.user(self._addr)
           self.reademail.pass_(self._password)
           self.allemail = self.reademail.stat()
        except:
            print('读取邮件登录失败')
            exit()
```
找到最新的邮件：
```python
        self.pop_connect()
        topemail = self.reademail.top(self.allemail[0], 0)
```
提取标题信息
### 2.根据信息解析出指令，利用os模块设置指令
```python
#延时关机
command = 'shutdown -s -t ' + sd_time
#定时关机
command = 'schtasks /create /TN %s /ST %s /sc DAILY /TR "shutdown /s"' %(sd_type, sd_time) 
os.system(command)
```
### 3.再自动发邮件覆盖指令，否则会重复检测到统一指令
连接到SMTP服务器：
```python
def smtp_connect(self):
        try:
           self.sendemail = smtplib.SMTP_SSL(self._smtp_server, 465)
           self.sendemail.login(self._addr, self._password)
        except:
            print('发送邮件登录失败')
            exit()
```
发送邮件，可以作为发邮件范例：
```pyhhon
def send_email(self):
        self.smtp_connect()
        msg = MIMEText('')
        msg['Subject'] = '设置完毕'
        msg['From'] = self._from_addr
        msg['To'] = self._addr
        self.sendemail.sendmail(self._from_addr, self._addr, msg.as_string())
        self.sendemail.close()
```

ps：注意邮箱要开通POP3/SMTP服务，有一个授权码
#### 感谢微信公众号：大白学Python