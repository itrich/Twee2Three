import requests
import threepy.config

class Feed:
  def __init__(self, api_key, broadcast_uid, feed_uid):
    self.broadcast_uid = broadcast_uid
    self.feed_uid = feed_uid
    self.endpoint = "/identities/" + self.broadcast_uid + "/feeds/" + self.feed_uid
    self.headers = { 'X-API-KEY' : api_key }

  def post(self, message):
    url = threepy.config.url_root + self.endpoint + "/chat"
    response = requests.post(url, headers=self.headers, json=message)
