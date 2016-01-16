# coding: utf-8
import json
import TwitterApiClient as tc

def writeFile(tweets):
	f = open("./uncategorized.tsv","a")
	for tweet in tweets["statuses"]:
		text = tweet[u"text"].encode('utf-8')
		text = text.replace("\n", "").replace(" ", "").replace("\t", "")
		f.write(text)
		f.write("\n")
	f.close()

def main():
	f = open('./secret.json')
	twkey = json.load(f)
	f.close()
	client = tc.TwitterApiClient(twkey["consumer_key"],twkey["consumer_key_secret"],twkey["access_token"],twkey["access_token_secret"])
	tweets = client.search("#")
	writeFile(tweets)

if __name__ == '__main__':
	main()