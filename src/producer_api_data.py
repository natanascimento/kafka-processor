# bibliotecas
from datetime import datetime
import requests
from json import dumps
import json
from kafka import KafkaProducer
import os

# 37c44cbc96731cbf8619a731c53b6e9ae4f200da
class producerApiData():
    
    def __init__(self):
        self._meraki_api_key = os.getenv('MERAKI_API_KEY')
        self.server = ''
        self.port =  '9092'
        self.broker = '{}:{}'.format(self.server, self.port)
        self.headers = {'X-Cisco-Meraki-API-Key': self._meraki_api_key}
        self.api_uri = 'https://api.meraki.com/api/v0/'

    def kafkaConfig(self):
        self.producer = KafkaProducer(bootstrap_servers='192.168.254.230:9092',
                                value_serializer=lambda x:
                                dumps(x).encode('utf-8'))
        return self.producer
    
    def getOrganizations(self):
        url = self.api_uri + 'organizations'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
    
    def getNetworksByOrganization(self, org_id):
        for org in org_id:
            response = requests.get('{}{}/{}{}'.format(self.api_uri, 'organizations', org, '/networks/'), headers=self.headers)
            if response.status_code == 200:
                return response.json()
            else:
                return response.status_code  

    def getClientsByNetwork(self, networks_id):
        for networkid in networks_id:
            response = requests.get('{}{}/{}{}'.format(self.api_uri, 'networks', networkid, '/clients/'), headers=self.headers)
            if response.status_code == 200:
                if response.json():
                    return response.json()
            else:
                return response.status_code
    
    def setNetworkId(self):
        networks = self.getNetworksByOrganization(self.setOrgByName('Betha'))
        networks_id = []
        for network in networks:
            networks_id.append(network.get('id'))
        return networks_id
    
    def setOrgByName(self, name):
        organizations = self.getOrganizations()
        org_id = []
        for org in organizations:
            if name.lower() in org.get('name').lower():
                org_id.append(org.get('id'))
        return org_id
    
    def producerData(self, topic, clients):
        producer = self.kafkaConfig()
        for client in clients:
            #data = {'id':client.get('id'), 'mac': client.get('mac'), 'description':client.get('description')}
            producer.send(topic,value=client, partition=0)
            print(client)
            
if __name__ == '__main__':
    while True:
        main = producerApiData()
        main.producerData('merakiApi',main.getClientsByNetwork(main.setNetworkId()))