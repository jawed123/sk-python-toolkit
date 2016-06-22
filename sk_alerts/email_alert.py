import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

##
######################################
## To send email alert.:
#
# Example:
# 	newAlert = EmailAlert({ "mime_type": EmailAlert.MIME_HTML} )
# 	me = "testing@sonu.com"
# 	you = "sonukr.meena@cronexus.com"
# 	subject = "dummy subject goes here"
#
# 	newAlert.build(subject,me,you, "<h1>Hello world </h1>")
# 	newAlert.dispatch()
#######################################

class EmailAlert:
	""" Send plain/html email
	"""

	MIME_TEXT="text mime type"
	MIME_HTML="html mime type"

	Subject = None
	To = None
	From = None
	Body = None
	Mime_type = MIME_TEXT

	def __init__(self, options):
		if options.get('mime_type',None) == None:
			raise Exception("mime_type filed not present")
		self.Mime_type = options['mime_type']

	def build(self, mail_subject, mail_from, mail_to, mail_body):
		self.set_subject(mail_subject)
		self.set_from(mail_from)
		self.set_to(mail_to)
		self.set_body(mail_body)

	def dispatch(self):
		msg = None
		if self.Mime_type == self.MIME_TEXT:
			msg = MIMEText(self.Body, 'plain')
		elif self.Mime_type == self.MIME_HTML:
			msg = MIMEText(self.Body, 'html')
		else:
		     raise "Unsupported mime type provided"

		msg['Subject'] = self.Subject;
		msg['From'] = self.From
		msg['To'] = self.To

		s = smtplib.SMTP('localhost')
		s.sendmail( self.From, self.To, msg.as_string() )
		s.quit()

	def set_subject(self, mail_subject):
		self.Subject = mail_subject

	def set_to(self, mail_to):
		self.To = mail_to

	def set_from(self, mail_from):
		self.From = mail_from

	def set_body(self, mail_body):
		self.Body = mail_body

