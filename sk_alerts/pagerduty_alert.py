import sys
import json
import requests
import subprocess
import time
import socket
import os

#### To send pagerduty alert:
    #
    #	pdAlert = PagerdutyAlert({service_key="pagerduty_service_key"} )
    #	pdAlert.trigger_incident({'incident_key': <mykey>,[,]})
    #	pdAlert.resolve_incident( {'incident_key': <..,[,]})
    #
##

class PagerdutyAlert:
    """PagerdutyAlert class
    - It sends or resolve alert on service identified by service_key
    API_KEY_TOKEN: It's not used currently in the program but can be used to
    extend the class.
    """
    SERVICE_KEY = None
    API_KEY_TOKEN = None
    headers = {}

    def __init__(self, options):
        """ Initializing

        :param service_key:  Integration key for service
        :param api_key_token: Pagerduty api token
        """
        self.SERVICE_KEY = options['service_key']
        self.API_KEY_TOKEN = options.get('api_key_token', None)

    def get_headers(self):
        if not self.headers :
            self.headers = {
                'Authorization': 'Token token={0}'.format(self.SERVICE_KEY),
                'Content-type': 'application/json',
            }
            return self.headers

    def build_payload(self, event_type, options ):
        options['service_key'] = options.get('service_key', self.SERVICE_KEY)
        options['event_type'] = event_type
        return options

    def trigger_incident(self, payload ):
        """ Trigger alert on service
        :param payload: payload dictionary as per pagerduty trigger doc
        https://developer.pagerduty.com/documentation/integration/events/trigger
        """

        pd_payload = json.dumps( self.build_payload("trigger", payload))
        response = requests.post(
            "https://events.pagerduty.com/generic/2010-04-15/create_event.json",
            headers=self.get_headers(),
            data=pd_payload
        )
        if response.status_code != 200:
            print response
            raise Exception("pagerduty response code is not 200")
        return True

    def resolve_incident(self, payload):
        """ Resolve incident identified by incident key and  service key
        :param payload: payload dictionary as per pagerduty resolve doc
        https://developer.pagerduty.com/documentation/integration/events/resolve
        """
        pd_payload = json.dumps( self.build_payload("resolve", payload) )
        response = requests.post(
            'https://events.pagerduty.com/generic/2010-04-15/create_event.json',
            headers=self.headers,
            data=pd_payload,
        )
        if response.status_code != 200:
            raise Exception("pagerduty response code is not 200")
        return True



