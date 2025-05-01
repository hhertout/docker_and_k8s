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
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"Message received: {body.decode()}")
    except Exception as e:
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
        print(f"Erreur de traitement : {e}")

try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(
        queue='ma_file_quorum',
        durable=True,
        arguments={'x-queue-type': 'quorum'}
    )

    channel.basic_consume(queue='test2', on_message_callback=callback, auto_ack=True)

    print("⏳ Waiting for messages...")
    channel.start_consuming()
    
    connection.close()
except Exception as e:
    print(f"❌ Erreur de connexion à RabbitMQ: {e}")