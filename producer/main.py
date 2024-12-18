import sys

from parser import check_url, parser
from rmq.rabbit import write_list


def run(args: list):
    if check_url(args[1]):
        print('Введён корректный URL')
        internal_links = parser(args[1])
        write_list(internal_links)
    else:
        print('Введён некорректный URL')
        return 0


if __name__ == '__main__':
    run(sys.argv)
