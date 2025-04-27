from confluent_kafka import Consumer, KafkaException
import os

user = os.getenv("KAFKA_USER")
password = os.getenv("KAFKA_PASSWORD")
kafka_endpoint = os.getenv("KAFKA_URI")

consumer = Consumer({
    'bootstrap.servers': kafka_endpoint,
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest' # 'earliest'
})

consumer.subscribe(["test-topic"])
print("🔌 Successfully connected to kafka")

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())

        print(f"📩 Message received: {msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    print("\n🛑 Consumer stopped... exiting")
finally:
    consumer.close()
