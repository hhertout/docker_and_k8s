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

def callback(ch, method, properties, body):
    try:
        print(f"Message received: {body.decode()}")
    except Exception as e:
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
        print(f"Erreur de traitement : {e}")

try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='test', durable=True)

    channel.basic_consume(queue='test', on_message_callback=callback, auto_ack=True)

    print("⏳ Waiting for messages...")
    channel.start_consuming()
    
    connection.close()
except Exception as e:
    print(f"❌ Erreur de connexion à RabbitMQ: {e}")