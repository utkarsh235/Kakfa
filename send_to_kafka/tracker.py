from confluent_kafka import Consumer
import json
consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "order-tracker",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)

consumer.subscribe(topics=["orders"])

print("Consumer is Running and Subscribed to orders topic...")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("ERROR when reading message -> ", msg.error())
            continue

        value = msg.value().decode("utf-8")
        order = json.loads(value)

        print("New message RECEIVED: -> ", order)

except KeyboardInterrupt:
    print("Connection innterupted by Keyboard")
finally:
    consumer.close()