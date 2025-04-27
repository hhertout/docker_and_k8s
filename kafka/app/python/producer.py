from confluent_kafka import Producer
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("KAFKA_USER")
password = os.getenv("KAFKA_PASSWORD")
kafka_endpoint = os.getenv("KAFKA_URI")

# Configuration du producer Kafka
conf = {
    'bootstrap.servers': kafka_endpoint,
    'receive.message.max.bytes': 2000000000,
}

try: 
    producer = Producer(conf)

    # Fonction de callback pour la confirmation d'envoi
    def delivery_report(err, msg):
        if err:
            print(f"❌ Erreur lors de l'envoi du message: {err}")
        else:
            print(f"✅ Message envoyé à {msg.topic()} [{msg.partition()}]")

    # Envoi de quelques messages
    for i in range(5):
        producer.produce("test-topic", key=str(i), value=f"Hello Kafka {i}", callback=delivery_report)

    # Attendre que tous les messages soient envoyés
    producer.flush()

except Exception as e: 
    print(e)

