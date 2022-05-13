import pika

params = pika.URLParameters('amqps://lswqptek:8pKYJcfazSYR1f9fygl5Rb4CE9b6i61j@dingo.rmq.cloudamqp.com/lswqptek')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='owner')

def callback(dh, method, properties, body):
    print('Received in owner')
    print(body)
channel.basic_consume(queue='owner', on_message_callback=callback, auto_ack=True)


print('Started consuming')

channel.start_consuming()

print('close consuming')

channel.close()