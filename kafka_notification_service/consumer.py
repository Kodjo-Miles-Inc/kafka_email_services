from kafka import KafkaConsumer
import json


class KafkaNotificationConsumer:
    def __init__(self, bootstrap_servers, topic, group_id):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        )

    def consume_notifications(self):
        for message in self.consumer:
            print(f"Received message: {message.value}")


def main():
    consumer = KafkaNotificationConsumer(
        bootstrap_servers=["localhost:9092"],
        topic="notification",
        group_id="notification_group",
    )
    consumer.consume_notifications()


if __name__ == "__main__":
    main()
