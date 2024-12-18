import pika

from rmq.connection import get_connection
from variables import QUEUE_NAME


def write_list(elements: list[str]) -> None:
    with get_connection() as connection:
        with connection.channel() as channel:
            channel.queue_declare(queue=QUEUE_NAME)

            for elem in elements:
                channel.basic_publish(exchange="", routing_key=QUEUE_NAME, body=elem)
                print(f'Ссылка {elem} записана в очередь')
