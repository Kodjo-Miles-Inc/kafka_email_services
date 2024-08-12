from kafka import KafkaProducer
import json


class KafkaNotificationProducer:
    def __init__(self, bootstrap_servers, topic):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        self.topic = topic

    def send_notification(self, message):
        self.producer.send(self.topic, message)
        self.producer.flush()

    def close(self):
        self.producer.close()


def main():
    import sys

    producer = KafkaNotificationProducer(
        bootstrap_servers=["localhost:9092"], topic="notification"
    )
    producer.send_notification({"message": sys.argv[1]})
    producer.close()


if __name__ == "__main__":
    main()
