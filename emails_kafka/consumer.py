from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'messages.all',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group'
)

for message in consumer:
    print(f' [x] Received message: {message.value.decode("utf-8")[:40]}...\']')
