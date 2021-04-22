import os

import dotenv
import tweepy

class TwitterApiConfig:
  
  def __init__(self, topic):
    dotenv.load_dotenv(dotenv.find_dotenv())
    self.__topíc = topic
    self.__twitter_consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
    self.__twitter_consumer_key_secret = os.getenv('TWITTER_CONSUMER_KEY_SECRET')
    self.__twitter_access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    self.__twitter_access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    self.__auth = tweepy.OAuthHandler(self.__twitter_consumer_key, self.__twitter_consumer_key_secret)
    self.__auth.set_access_token(self.__twitter_access_token, self.__twitter_access_token_secret)

  @property
  def getApiData(self):
    self.api = tweepy.API(self.__auth)
    self.api = self.api.search(self.__topíc)
    
    return self.api