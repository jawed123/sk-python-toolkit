from  sk_alerts.pagerduty_alert import PagerdutyAlert
from  sk_alerts.email_alert import EmailAlert

import os
import time

service_key = os.environ.get("SERVICE_KEY")

print service_key

pdAlert = PagerdutyAlert({'service_key': service_key } )
pdAlert.trigger_incident({'incident_key': "sonu_custom_alert",'description':"sonu custom alert description" })
print "sleeping for 20 second before resolving incident"
time.sleep(10)
pdAlert.resolve_incident( {'incident_key': "sonu_custom_alert", 'description':'sonu custom alert resolved'})


newAlert = EmailAlert({ "mime_type": EmailAlert.MIME_HTML} )
me = "testing@sonu.com"
you = "sonukr.meena@cronexus.com"
subject = "dummy subject goes here"

newAlert.build(subject,me,you, "<h1>Hello world </h1>")
newAlert.dispatch()
