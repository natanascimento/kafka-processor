import os
from datetime import datetime
from json import dumps

import dotenv
from kafka import KafkaProducer

from .TwitterApiConfig import TwitterApiConfig

class TwitterProducer(TwitterApiConfig):
  
  def __init__(self, topic: str):
    dotenv.load_dotenv(dotenv.find_dotenv())
    self.topic = topic
    self.broker_server = '{}:{}'.format(os.getenv('KAFKA_SERVER'), os.getenv('KAFKA_PORT'))
    super().__init__(topic)

  @property
  def CollectTweets(self):
    self.tweets = self.getApiData
 
    self.producer = KafkaProducer(bootstrap_servers=self.broker_server, 
                                  value_serializer=lambda v: str(v).encode('utf-8'))
    
    for tweet in self.tweets:
      phrases = str(tweet.text)
      createdAt = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
      data = {"tweet": phrases, "createdAt": createdAt}
      self.producer.send(self.topic, value=data)