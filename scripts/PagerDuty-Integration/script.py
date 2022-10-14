#!/usr/bin/env python

import json
import requests
from pathlib import Path
from dotenv import load_dotenv
env_path=Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


#This Key should be available in .env file
ROUTING_KEY = os.environ['ROUTING_KEY'] # ENTER EVENTS V2 API INTEGRATION KEY HERE 


# This function takes the payload info from the user and can be put in the right format

def trigger_incident(payload):
    # Triggers a PagerDuty incident without a previously generated incident key
    # Uses Events V2 API - documentation: https://v2.developer.pagerduty.com/docs/send-an-event-events-api-v2
    
    header = {
        "Content-Type": "application/json"
    }

    payload = { # Payload is built with the least amount of fields required to trigger an incident
        "routing_key": ROUTING_KEY, 
        "event_action": "trigger",
        "payload": {
            "summary": "Azure Resource is expereiencing issues",
            "source": f"{payload['resource_id']}",
            "severity": "critical",
            "component":f"{payload['tags']}",
            "class":f"{payload['error_code']}",
            "custom_details":f"{payload['system_data']}"

            


        }
    }

    response = requests.post('https://events.pagerduty.com/v2/enqueue', 
                            data=json.dumps(payload),
                            headers=header)
	
    if response.json()["status"] == "success":
        print('Incident created with with dedup key (also known as incident / alert key) of ' + '"' + response.json()['dedup_key'] + '"') 
    else:
        print(response.text) # print error message if not successful

if __name__ == '__main__':
    trigger_incident()
