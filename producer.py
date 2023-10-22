import time 
from datetime import datetime,timezone
from confluent_kafka import Producer
from configs import local_server_address, topic_name

producer = Producer({"bootstrap.servers": local_server_address})
while True:
    now_utc = datetime.now(timezone.utc)
    message = f"sending msg {now_utc}"
    producer.produce(topic_name, key=str(now_utc), value=message)
    time.sleep(1)

producer.flush()

