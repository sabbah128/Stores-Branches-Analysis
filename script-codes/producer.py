import json
import time
from confluent_kafka import Producer
from store_simulator import simulator_data


config = {
    'bootstrap.servers': 'localhost:9092,localhost:9093,localhost:9094',
    'client.id': 'python-producer'}

producer = Producer(config)
TOPIC_NAME = 'store-data'

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()}, [{msg.partition()}]')

def produce_messages():
    try:
        for record in simulator_data.read_json_records():
            # print(f">>> Class type record {type(record)}")
            json_data = json.dumps(record)
            producer.produce(topic=TOPIC_NAME,
                            key=str(record["InvoiceNumber"]),
                            value=json_data, 
                            callback=delivery_report)
            # print(f">>> Class type json_data {type(json_data)}")
            
            print(f"Sent StoreID number: {str(record["InvoiceNumber"])}")
            producer.poll(0)
            time.sleep(0.1)
    except Exception as e:
        print(f"Error producing message: {e}")

    producer.flush()

if __name__ == '__main__':
    produce_messages()