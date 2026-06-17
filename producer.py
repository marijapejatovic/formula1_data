from kafka import KafkaProducer
import json
import requests

bootstrap_servers=['localhost:9092']
topic='f1-data'

producer=KafkaProducer(bootstrap_servers=bootstrap_servers,
                       value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def fetch_and_send():
    response = requests.get('https://api.openf1.org/v1/weather')
    data=response.json()

    for record in data:
        producer.send(topic, value=record)
        print('Sent:', record)

    producer.flush()

fetch_and_send()
