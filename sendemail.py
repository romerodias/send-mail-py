import smtplib

class SendMail:
	
	smtp_server=''
	smtp_port=25
	smtp_password=''
	smtp_from=''
	smtp_use_auth=True

	def send_mail(self, toaddr, subject, msg):
		server = smtplib.SMTP(self.smtp_server,self.smtp_port)
		try:
			if(self.smtp_use_auth == True):
				server.ehlo()
				server.starttls()
				server.ehlo()
				server.login(self.smtp_from, self.smtp_password)
			message = "Subject: " + subject + "\n\n" + msg
			server.sendmail(self.smtp_from, toaddr, message)
		except Exception as inst:
			print(type(inst))     
			print(inst.args)     
			print(inst)
		finally:
				server.close()				