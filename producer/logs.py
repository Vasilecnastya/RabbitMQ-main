from bs4 import Tag


def write_parser_logs(url: str, title: str, links: list[Tag], protocol: str, domain: str) -> None:
    print(f'Введена страница "{title}", полная ссылка "{url}". Внутренние ссылки:')
    for link in links:
        full_link = link.get('href') if link.get('href').startswith(f'{protocol}://{domain}') else f'{protocol}://{domain}{link.get("href")}'
        print(f'\tВнутренняя ссылка "{full_link}", содержимое "{link.string}"')
    print('\n' * 3)
