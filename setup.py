from setuptools import setup, find_packages

setup(
    name="kafka_notification_service",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "kafka-python",
    ],
    entry_points={
        "console_scripts": [
            "kafka-produce=kafka_notification_service.producer:main",
            "kafka-consume=kafka_notification_service.consumer:main",
        ],
    },
    author="Jaden Kodjo Miles Ahmed",
    author_email="a.jaden.miles@gmail.com",
    description="A Kafka notification service package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Kodjo-Miles-Inc/kafka_notification_service",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
