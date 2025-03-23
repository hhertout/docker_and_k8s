from confluent_kafka import Consumer, KafkaException

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'latest' # 'earliest'
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
