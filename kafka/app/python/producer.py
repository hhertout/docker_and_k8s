from confluent_kafka import Producer

# Configuration du producer Kafka
conf = {
    'bootstrap.servers': 'localhost:9092'
}

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
