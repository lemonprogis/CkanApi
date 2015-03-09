import requests
import json

class Action(object):
    ACTION_PACKAGE_CREATE = "api/action/package_create"
    ACTION_RESOURCE_CREATE = "api/action/resource_create"

class CkanApi(object):
    """ CkanApi for talking to our CKAN instance """
    def __init__(self, url,api_key):
        self.url = url
        self.api_key = api_key

        self.headers = {
            'Authorization': self.api_key,
            'content-type': 'application/json'
        }
        
    def create_package(self, data):
        return requests.post('{}/{}'.format(self.url, Action.ACTION_PACKAGE_CREATE), 
            data=json.dumps(data), 
            headers=self.headers)

    def create_resource(self, data, f_path):
        return requests.post('{}/{}'.format(self.url, Action.ACTION_RESOURCE_CREATE),
            data=json.dumps(data),
            headers=self.headers,
            file=[('upload',file(f_path))])