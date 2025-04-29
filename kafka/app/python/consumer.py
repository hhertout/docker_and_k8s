from confluent_kafka import Consumer
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("KAFKA_USER")
password = os.getenv("KAFKA_PASSWORD")
kafka_endpoint = os.getenv("KAFKA_URI")

conf = {
    'bootstrap.servers': kafka_endpoint,
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(conf)
consumer.subscribe(['test-topic'])

print("🟢 Waiting for messages...")
try:
    while True:
        msg = consumer.poll(timeout=5)
        if msg is None:
            continue
        if msg.error():
            print(f"❌ Error: {msg.error()}")
            continue

        print(f"📩 Received: {msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
