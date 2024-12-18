import asyncio

from rmq.rabbit import read_queue_elem


if __name__ == '__main__':
    read_queue_elem()
    print('Работа завершена')
