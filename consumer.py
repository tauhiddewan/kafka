from confluent_kafka import Consumer, KafkaError
from configs import local_server_address, topic_name, consumer_group_id

consumer = Consumer({
    'bootstrap.servers': local_server_address,
    'group.id': consumer_group_id,
    'auto.offset.reset': 'earliest' 
})

consumer.subscribe([topic_name])
while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Reached end of partition')
        else:
            print(f'Error: {msg.error()}')
    else:
        print(f'Received message: key={msg.key()}, value={msg.value()}')

consumer.close()
