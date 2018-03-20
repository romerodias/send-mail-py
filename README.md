# send-mail-py
Python Class to Send E-mail


### usage
#### send e-mail with no authentication 
```python
from sendemail import SendMail

sm = SendMail()
sm.smtp_use_auth=False
sm.smtp_server='smtp.domain.com.br'
sm.smtp_port=25
sm.smtp_from='acount@domain.com.br'

sm.send_mail('romero@omnilink.com.br', "Subject", "Message")
```


#### send e-mail with authentication
```python
from sendemail import SendMail

sm = SendMail()
sm.smtp_use_auth=True
sm.smtp_server='smtp.gmail.com'
sm.smtp_port=587
sm.smtp_password='password'
sm.smtp_from='username'

sm.send_mail('romero.dias@omnilink.com.br', "Subject", "Message")
```
