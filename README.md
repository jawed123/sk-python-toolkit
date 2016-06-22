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
    --Todo--

```
