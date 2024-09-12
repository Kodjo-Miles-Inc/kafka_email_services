import unittest
from kafka_notification_service.producer import KafkaNotificationProducer


class TestKafkaNotificationProducer(unittest.TestCase):

    def test_send_notification(self):
        producer = KafkaNotificationProducer(["localhost:9092"], "test_topic")
        try:
            producer.send_notification(
                {"test": "This is a test message from the test suite"}
            )
        finally:
            producer.close()


if __name__ == "__main__":
    unittest.main()
