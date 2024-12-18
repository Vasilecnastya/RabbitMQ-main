from pika import ConnectionParameters, PlainCredentials, BlockingConnection

from variables import RMQ_HOST, RMQ_PORT, RMQ_USER, RMQ_PASSWORD


def get_connection() -> BlockingConnection:
    return BlockingConnection(
        ConnectionParameters(host=RMQ_HOST, port=RMQ_PORT, credentials=PlainCredentials(RMQ_USER, RMQ_PASSWORD)))
