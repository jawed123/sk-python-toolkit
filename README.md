Packages
--------


###  **sk-alerts**
    
### sk-alerts.email_alert
   

``` python
    from sk-alerts.email_alert import EmailAlert
    newAlert = EmailAlert({ "mime_type": EmailAlert.MIME_HTML} )
    me = "testing@sonu.com"
    you = "sonukr.meena@cronexus.com" 
    subject = "dummy subject goes here"

    newAlert.build(subject,me,you, "<h1>Hello world </h1>")
    newAlert.dispatch()
```

### sk-alerts.pagerduty_alert


``` python
    from sk-alerts.pagerduty_alert import PagerdutyAlert
    service_key = os.environ.get("SERVICE_KEY")
    pdAlert = PagerdutyAlert({'service_key': service_key } )
    pdAlert.trigger_incident({'incident_key': "sonu_custom_alert",'description':"sonu custom alert description" })
    print "sleeping for 20 second before resolving incident"
    time.sleep(10)
    pdAlert.resolve_incident( {'incident_key': "sonu_custom_alert", 'description':'sonu custom alert resolved'})

```


## Tests

Edit and Set enviornemnt

    . ./set_env.sh

Run file
    
    python sk_alerts_test.py

