import os
from dotenv import load_dotenv
from tweepy import OAuth1UserHandler, Client

from utils.Singleton import Singleton

load_dotenv()

ckey = os.getenv('TWITTER_API_KEY')
csecret = os.getenv('TWITTER_SECRET_API_KEY')
atoken = os.getenv('TWITTER_ACCESS_TOKEN')
asecret = os.getenv('TWITTER_SECRET_ACCESS_TOKEN')
btoken=os.getenv('TWITTER_BEARER_TOKEN')

@Singleton
class TwitterAuth:
    def __init__(self):
        # API v1.x .. Then call with => api = API(auth)
        self.auth = OAuth1UserHandler(
            ckey, csecret, atoken, asecret
        )
        
        # API v2.x+
        self.app_client = Client(bearer_token=btoken)
        self.user_client = Client(
            consumer_key=ckey,
            consumer_secret=csecret,
            access_token=atoken,
            access_token_secret=asecret,
        )
