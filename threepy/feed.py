import requests

from threepy.api import API

class Feed:
  def __init__(self, api: API, broadcast_uid, feed_uid):
    self.broadcast_uid = broadcast_uid
    self.feed_uid = feed_uid
    self.endpoint = "/identities/" + self.broadcast_uid + "/feeds/" + self.feed_uid

  def post(self, message):
    url = config.url_root + self.endpoint + "/chat"
    response = requests.post(url, headers=self.headers, json=message)
