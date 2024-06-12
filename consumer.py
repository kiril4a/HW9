import pika
import json
from models import Contact

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Створення черги
channel.queue_declare(queue='email_queue')

def send_email(contact):
    # Функція-заглушка для надсилання email
    print(f"Sending email to {contact.email}...")
    # Імітація затримки для реального надсилання email
    import time
    time.sleep(2)
    print(f"Email sent to {contact.email}.")

def callback(ch, method, properties, body):
    data = json.loads(body)
    contact_id = data['contact_id']
    contact = Contact.objects(id=contact_id).first()
    
    if contact:
        send_email(contact)
        contact.email_sent = True
        contact.save()

channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
