import requests
import simplejson as json

url = "http://www.makemymails.com/sms/api-single-sms/ "
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def sendsms(sms_to, sms_body, MMM_API_KEY, DEVICE_ID):
    data = {
        'sms_to': sms_to,
        'sms_body': sms_body,
        'MMM_API_KEY': MMM_API_KEY,
        'device_id': DEVICE_ID,
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)

