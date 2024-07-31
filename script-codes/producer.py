from time import sleep
from json import dumps
from kafka import KafkaProducer
from store_simulator import simulator_data
from kafka.errors import KafkaError


TOPIC_NAME = 'store-data'

# producer = KafkaProducer(bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'],
#                         value_serializer=lambda x: dumps(x).encode('utf-8'),
#                         key_serializer=str.encode)

try:
    producer = KafkaProducer(bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'],
                             value_serializer=lambda x: dumps(x).encode('utf-8'),
                             key_serializer=str.encode)
except KafkaError as e:
    print(f"Failed to connect to Kafka: {e}")


for num in range(100):
    data = simulator_data.read_json_records()
    producer.send(TOPIC_NAME, value=data, key=data["InvoiceNumber"])
    print(f"Sending Store ID data : {data['StoreID']}")
    sleep(1)
