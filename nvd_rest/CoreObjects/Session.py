import json, requests, urllib3

class Session:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://services.nvd.nist.gov/rest/json'
    
    def get(self, api_endpoint, json=None, verify=False):
        if not isinstance(api_endpoint, str):
            raise TypeError(api_endpoint)
        request_url = self.base_url + api_endpoint
        print(request_url)
        response = requests.get(request_url, headers={"apiKey":self.api_key}, verify=verify)
        return response.json()
