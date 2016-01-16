# coding: utf-8
from requests_oauthlib import OAuth1Session
import json

class TwitterApiClient(object):
	"""Connect by TwitterAPI"""

	def __init__(self, consumerKey,consumerSecret,accessToken,accessTokenSecret):
		self.consumerKey = consumerKey
		self.consumerSecret = consumerSecret
		self.accessToken = accessToken
		self.accessTokenSecret  = accessTokenSecret


	def create_oath_session(self):
		oath = OAuth1Session(self.consumerKey,self.consumerSecret,self.accessToken,self.accessTokenSecret)
		return oath

	def search(self,keyword):
		url = "https://api.twitter.com/1.1/search/tweets.json"
		params = {
        "q": unicode(keyword),
        "lang": "ja",
        "result_type": "recent",
        "count": "100"
        }
		oath = self.create_oath_session()
		responce = oath.get(url, params = params)
		print(responce.status_code)
		if responce.status_code != 200:
			print "Error code: %d" %(responce.status_code)
			return None
		tweets = json.loads(responce.text)
		return tweets