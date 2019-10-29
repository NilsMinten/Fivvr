import requests
import json


class PaymentApi:
    api_key = ''
    api_url = ''

    def make_payment(self):
        print('make payment ' + self.api_url)

    def connect(self, data):
        data['apikey'] = self.api_key
        response = requests.post(self.api_url, data)

        return json.dumps(response)
