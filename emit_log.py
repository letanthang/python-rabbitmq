import pika
import sys
credentials = pika.PlainCredentials('rabbit', 'password')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')
# channel.queue_declare(queue='hello')

channel.basic_publish(exchange='logs',
                      routing_key='hello',
                      body=sys.argv[1])

print(" [x] Sent '%s'" % (sys.argv[1]))
connection.close()
