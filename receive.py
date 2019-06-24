import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


credentials = pika.PlainCredentials('rabbit', 'password')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. press CTRL+C to exit')
channel.start_consuming()
