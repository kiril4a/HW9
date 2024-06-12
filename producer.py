import pika
import json
from models import Contact
from faker import Faker

fake = Faker()

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Створення черги
channel.queue_declare(queue='email_queue')

def send_to_queue(contact_id):
    channel.basic_publish(
        exchange='',
        routing_key='email_queue',
        body=json.dumps({'contact_id': str(contact_id)})
    )

# Генерація фейкових контактів та запис до бази даних
def generate_contacts(n):
    for _ in range(n):
        contact = Contact(
            fullname=fake.name(),
            email=fake.email()
        )
        contact.save()
        send_to_queue(contact.id)

if __name__ == '__main__':
    generate_contacts(10)  # Генерація 10 фейкових контактів
    connection.close()
