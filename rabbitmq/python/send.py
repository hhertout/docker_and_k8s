from dotenv import load_dotenv
import pika
import os
import time

load_dotenv()

rabbitmq_host = os.getenv("MQ_ENDPOINT")
rabbitmq_port = os.getenv("MQ_PORT")
credentials = pika.PlainCredentials(os.getenv("MQ_USER"), os.getenv("MQ_PASSWORD"))

parameters = pika.ConnectionParameters(
    host=rabbitmq_host,
    port=rabbitmq_port,
    credentials=credentials,
    heartbeat=60,
    virtual_host="/",
)

def on_open(connection):
    channel = connection.channel()

    # Activer le mode de confirmation
    channel.confirm_select()

    # Déclaration de la queue
    channel.queue_declare(queue='test2', passive=True)

    # Envoi du message
    channel.basic_publish(
        exchange='',
        routing_key='test2',
        body='Hello from Python!',
        properties=pika.BasicProperties(delivery_mode=2),
        mandatory=True
    )
    print("✅ Message sent successfully")

    # Fermeture propre de la connexion après l'envoi
    connection.close()

def on_open_error(connection, exception):
    print(f"❌ Failed to open connection: {exception}")
    connection.close()

try:
    # Connexion avec SelectConnection pour permettre la confirmation de message
    connection = pika.SelectConnection(parameters, on_open_callback=on_open, on_open_error_callback=on_open_error)

    print("🔌 Waiting for connection...")
    connection.ioloop.start()

except Exception as e:
    print(f"❌ An error occurred: {e}")