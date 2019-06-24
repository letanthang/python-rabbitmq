import sys
import pika

credentials = pika.PlainCredentials('rabbit', 'password')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')

message = ' '.join(sys.argv[1:]) or "hello world!"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)

print(" [x] Sent %r" % message)
connection.close()
