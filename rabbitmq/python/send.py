from dotenv import load_dotenv
import pika
import os

load_dotenv()

rabbitmq_host = os.getenv("MQ_ENDPOINT")
rabbitmq_port = os.getenv("MQ_PORT")
credentials = pika.PlainCredentials(os.getenv("MQ_USER"), os.getenv("MQ_PASSWORD"))

parameters = pika.ConnectionParameters(
    host=rabbitmq_host,
    port=rabbitmq_port,
    credentials=credentials
)

try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='test2', passive=True)

    channel.basic_publish(
        exchange='',
        routing_key='test2',
        body='Hello from Python!',
        properties=pika.BasicProperties(delivery_mode=2)
    )

    print("✅ Message sent")
except pika.exceptions.ChannelClosedByBroker as e:
    print(f"La file n'existe pas : {e}")
    # Optionnel : relancer le canal si tu veux continuer
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
except Exception as e:
    print(f"❌ Erreur de connexion à RabbitMQ: {e}")
finally:
    connection.close()
