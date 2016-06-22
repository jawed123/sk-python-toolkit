import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

##
######################################
## To send email alert.:
#
# Example:
# 	newAlert = EmailAlert({ "mime_type": EmailAlert.MIME_HTML} )
#       newAlert.build({
#           "from": "sonukr.meena@testserver.com",
#           "to": "sonukr666@gmail.com",
#           "subject": "dummy subject goes here",
#           "body": "<h1>my mail body goes here </h1>",
#           "reply-to": "sahil@testserver.com"
#       })
# 	newAlert.dispatch()
# With smtp server
#       newAlert = EmailAlert({"mime_type": EmailAlert.MIME_HTML,
#       'smtp': {
#        'server': <server>,
#        'port': <port>,
#        'username': <username>,
#        'password': <password>
#       } } )
#######################################

class EmailAlert:
	""" Send plain/html email
	"""

	MIME_TEXT="text mime type"
	MIME_HTML="html mime type"

	Mime_type = MIME_TEXT
        smtpserver = None
        message = None

	def __init__(self, options):
		if options.get('mime_type',None) == None:
			raise Exception("mime_type filed not present")
		self.Mime_type = options['mime_type']
                if options.get('smtp', None) == None:
                    print "using localhost smtp"
                    self.smtpserver = smtplib.SMTP('localhost')
                else:
                    smtp = options.get('smtp')
                    server = smtp.get('server')
                    port = smtp.get('port')
                    username = smtp.get('username')
                    password = smtp.get('password')

                    self.smtpserver = smtplib.SMTP( server, port )
                    self.smtpserver.ehlo()
                    self.smtpserver.starttls()
                    self.smtpserver.ehlo()
                    self.smtpserver.login(username, password )


        def build(self, mailObject):
		if self.Mime_type == self.MIME_TEXT:
			self.message = MIMEText( mailObject['body'], 'plain')
		elif self.Mime_type == self.MIME_HTML:
			self.message = MIMEText( mailObject['body'], 'html')
		else:
                    raise "Unsupported mime type provided"

                self.message['From'] = mailObject.get('from')
                self.message['To'] = mailObject['to']
                self.message['Subject'] = mailObject['subject']
                self.message['Cc'] = mailObject.get('cc', '')
                self.message['Bcc'] = mailObject.get('bcc', '')
                self.message['Reply-To'] = mailObject.get('reply-to', '')


	def dispatch(self):
		self.smtpserver.sendmail( self.message['From'], self.message['To'], self.message.as_string() )
		self.smtpserver.quit()



