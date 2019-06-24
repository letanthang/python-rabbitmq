import pika
credentials = pika.PlainCredentials('rabbit', 'password')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello world!'")
connection.close()
