from confluent_kafka import Producer

producer_conf = {
    "bootstrap.servers": "localhost:9094"
}

producer = Producer(producer_conf)


def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

producer.produce(
    topic="confluent-kafka",
    key='cf-1-key',
    value='Hello-kafka',
    callback=delivery_report
)

producer.flush()