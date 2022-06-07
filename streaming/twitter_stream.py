import os
from dotenv import load_dotenv

from tweepy import Stream, OAuth1UserHandler

load_dotenv()

ckey = os.getenv('TWITTER_API_KEY')
csecret = os.getenv('TWITTER_SECRET_API_KEY')
atoken = os.getenv('TWITTER_ACCESS_TOKEN')
asecret = os.getenv('TWITTER_SECRET_ACCESS_TOKEN')

class Listener(Stream):
    def on_data(self, data):
        print(data)

    def on_error(self, status):
        print(status)

auth = OAuth1UserHandler(ckey, csecret, atoken, asecret)

twitterStream = Stream(ckey, csecret, atoken, asecret)
twitterStream.filter(track=["car"])
