import os
from datetime import datetime
import time

import dotenv
import random

from faker import Faker
from kafka import KafkaProducer

class OLTPProducer:
  
  def __init__(self, topic: str):
    dotenv.load_dotenv(dotenv.find_dotenv())
    self.topic = topic
    self.broker_server = '{}:{}'.format(os.getenv('KAFKA_SERVER'), os.getenv('KAFKA_PORT'))
    self.producer = KafkaProducer(bootstrap_servers=self.broker_server, 
                                  value_serializer=lambda v: str(v).encode('utf-8'))
    self.__fake = Faker()
    self.__createdAt = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    self.__customer_name = self.__fake.name()
    self.__customer_address = self.__fake.address().replace('\n', ' - ')
    self.__customer_buy_price = self.__fake.pricetag()

  @property
  def CustomerPurchase(self):
    self.__data = {'customer_name':self.__customer_name, \
        'customer_address': self.__customer_address, \
        'customer_buy_price': self.__customer_buy_price, \
        'createdAt': self.__createdAt}
    return self.__data
  
  @property
  def DumpData(self):
    data = self.CustomerPurchase
    print(data)
    self.producer.send(self.topic, value=data)
      