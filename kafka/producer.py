from models.videoChunkingEvent import VideoChunkingEvent
import json
from kafka import KafkaProducer
from config.setting import settings

class KafkaProducer:
    def __init__(self, broker_url):
        self.producer = KafkaProducer(
            bootstrap_servers=broker_url,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def send_message(self, topic: str, event_data: VideoChunkingEvent):

        message = dict(event_data)
        future = self.producer.send(topic, value=message)
        try:
            future.get(timeout=10)
            print(f"Message sent to {topic}")
        except Exception as e:
            print(f"Failed to send message: {e}")

    def close(self):
        self.producer.close()

