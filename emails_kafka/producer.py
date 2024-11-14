from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')


def send_message(_message):
    message = str(_message)
    producer.send('messages.all', message.encode('utf-8'))
    producer.flush()
    print(f' [x] Sent message: {message[:40]}...\'] to messages.all.')
