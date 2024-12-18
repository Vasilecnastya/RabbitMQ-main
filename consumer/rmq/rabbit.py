from rmq.connection import get_connection
from variables import QUEUE_NAME, TIMEOUT
from parser import parser


links_count = 0


def write_list(elements: list[str]) -> None:
    with get_connection() as connection:
        with connection.channel() as channel:
            channel.queue_declare(queue=QUEUE_NAME)

            for elem in elements:
                channel.basic_publish(exchange="", routing_key=QUEUE_NAME, body=elem)
                print(f'Ссылка {elem} записана в очередь')


def process_message(channel, method, properties, body):
    global links_count

    print('Сообщение прочитано')
    internal_links = parser(body.decode())
    write_list(internal_links)

    channel.basic_ack(delivery_tag=method.delivery_tag)


def read_queue_elem() -> None:
    with get_connection() as connection:
        with connection.channel() as channel:
            for method, properties, body in channel.consume(QUEUE_NAME, inactivity_timeout=TIMEOUT):
                if method is None:
                    break
                process_message(channel, method, properties, body)
