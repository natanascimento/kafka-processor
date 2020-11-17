# bibliotecas
from datetime import datetime
import requests
from json import dumps
from kafka import KafkaProducer
import os

# chaves de autenticação da Meraki API
meraki_api_key = os.getenv('MERAKI_API_KEY')

# configuração do kafka
broker = '192.168.254.230:9092'
topico = 'artigo-medium'
producer = KafkaProducer(bootstrap_servers=[broker],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

