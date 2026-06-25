import os
import json
import pika
from dotenv import load_dotenv

load_dotenv()

EXCHANGE = "domainEvents"
QUEUE = "usuarios.events.queue"
ROUTING_KEYS = {
    "created": "user.events.app.created",
    "updated": "user.events.app.updated",
    "deleted": "user.events.app.deleted",
    "retrieved": "user.events.app.retrieved",
}


def get_connection():
    url = os.getenv("RABBITMQ_URL")
    return pika.BlockingConnection(pika.URLParameters(url))


def configurar_rabbit():
    connection = get_connection()
    channel = connection.channel()
    channel.exchange_declare(exchange=EXCHANGE, exchange_type="topic", durable=True)
    channel.queue_declare(queue=QUEUE, durable=True)
    for key in ROUTING_KEYS.values():
        channel.queue_bind(queue=QUEUE, exchange=EXCHANGE, routing_key=key)
    connection.close()


def publicar_evento(evento, routing_key: str):
    connection = get_connection()
    channel = connection.channel()
    channel.exchange_declare(exchange=EXCHANGE, exchange_type="topic", durable=True)
    channel.basic_publish(
        exchange=EXCHANGE,
        routing_key=routing_key,
        body=json.dumps(evento),
        properties=pika.BasicProperties(
            content_type="application/json", delivery_mode=2
        ),
    )
    connection.close()
