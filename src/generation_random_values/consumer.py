import os

import dotenv 
from kafka import KafkaConsumer

dotenv.load_dotenv(dotenv.find_dotenv())

consumer = KafkaConsumer('kafka-python-topic',bootstrap_servers='{}:{}'.format(os.getenv('KAFKA_SERVER'), os.getenv('KAFKA_PORT')))

for message in consumer:
    print (message.value.decode('utf-8'))