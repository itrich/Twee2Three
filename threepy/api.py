import requests

class API:
  def __init__(self, api_key, host='broadcast.threema.ch', api_root='/api/v1'):
    self.url = "https://" + host + api_root
    self.headers = { 'X-API-KEY': api_key }

  def get_profile(self):
    endpoint = self.url + "/"
    response = requests.get(endpoint, headers=self.headers)

  def get_identities(self):
    endpoint = self.url + "/identities"
    response = requests.get(endpoint, headers=self.headers)
