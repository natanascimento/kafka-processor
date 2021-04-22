import os
from datetime import datetime
import json

from kafka import KafkaConsumer
import dotenv

class TwitterConsumer:
  
  def __init__(self, topic):
    dotenv.load_dotenv(dotenv.find_dotenv())
    self.topic = topic
    self.broker_server = '{}:{}'.format(os.getenv('KAFKA_SERVER'), os.getenv('KAFKA_PORT'))
    
  @property
  def ConsumerTweets(self):
    
    consumer = KafkaConsumer(self.topic, bootstrap_servers=self.broker_server)
    for tweet in consumer:
      print(tweet.value.decode('utf-8'))
      