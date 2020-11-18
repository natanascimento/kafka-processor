from kafka import KafkaConsumer
import os 

consumer = KafkaConsumer('kafka-python-topic',bootstrap_servers='{}:{}'.format(os.getenv('KAFKA_SERVER'), os.getenv('KAFKA_PORT')))
for message in consumer:
    print (message)