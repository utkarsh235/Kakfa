from confluent_kafka import Producer
import uuid
import json

producer_config = {
        'bootstrap.servers': 'localhost:9092'
    }
producer = Producer(producer_config)

def delivery_report(err, msg):
    if err: 
        print('Delivery Report ERROR! -> ', err)
    else:
        print("Delivery SUCCEEDED! -> ", {msg.value().decode('utf-8')})

order = {
    "order_id": str(uuid.uuid4()),
    "user": "Sapna",
    "item": "Double cheese Margarita Pizza",
    "quantity": 3
}

json_str = json.dumps(order).encode("utf-8")

producer.produce(
    topic="orders", 
    key="",
    value=json_str,
    callback=delivery_report
)

producer.flush()