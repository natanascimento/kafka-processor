import json
import time

from confluent_kafka import Producer, KafkaError
from confluent import ccloud

from mock.customer import CustomerDataProducer


if __name__ == '__main__':

    args = ccloud.parse_args()
    config_file = args.config_file
    topic = args.topic
    conf = ccloud.read_ccloud_config(config_file)

    producer_conf = ccloud.pop_schema_registry_params_from_config(conf)
    producer = Producer(producer_conf)

    delivered_records = 0

    def acked(err, msg):
        global delivered_records
        """Delivery report handler called on
        successful or failed delivery of message
        """
        if err is not None:
            print("Failed to deliver message: {}".format(err))
        else:
            delivered_records += 1
            print("Produced record to topic {} partition [{}] @ offset {}"
                  .format(msg.topic(), msg.partition(), msg.offset()))

    n_events = 5000
    
    startAt = time.time()
    
    for n in range(n_events):
        record_key = "customer"
        mock_customer_data = CustomerDataProducer()
        record_value = json.dumps(mock_customer_data.generateCustomer)
        print("Producing record: {}\t{}".format(record_key, record_value))
        producer.produce(topic, key=record_key, value=record_value, on_delivery=acked)
        producer.poll(0)
        
    producer.flush()

    print("{} messages were produced to topic {}!".format(delivered_records, topic))
    print(f"Execution Time: {time.time() - startAt}")