import os
from dotenv import load_dotenv


load_dotenv()


# Переменные для подключения к RabbitMQ
RMQ_HOST = os.getenv("RMQ_HOST")
RMQ_PORT = os.getenv("RMQ_PORT")
RMQ_USER = os.getenv("RMQ_USER")
RMQ_PASSWORD = os.getenv("RMQ_PASSWORD")

# Название очереди
QUEUE_NAME = os.getenv("QUEUE_NAME")
