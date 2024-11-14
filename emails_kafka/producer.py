from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')


def send_message(_message):
    message = str(_message)
    producer.send('messages.all', message.encode('utf-8'))
    producer.flush()
    print(f' [x] Sent message: {message[:40]}...\'] to messages.all.')
    topic = get_topic_by_word(message)
    if topic:
        producer.send(topic, message.encode('utf-8'))
        producer.flush()
        print(f' [x] Sent message: {message[:40]}...\'] to {topic}.')


def get_topic_by_word(message):
    if 'hostage' in message:
        return 'messages.hostage'
    if 'explos' in message:  # noqa
        return 'messages.explos'  # noqa
    return
