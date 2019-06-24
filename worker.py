import pika
import time


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


credentials = pika.PlainCredentials('rabbit', 'password')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(queue='hello',
                      auto_ack=False,
                      on_message_callback=callback)

print(' [*] Waiting for messages. press CTRL+C to exit')
channel.start_consuming()
