import requests
from bs4 import BeautifulSoup, Tag

from urllib.parse import urlparse

from logs import write_parser_logs


def get_domain(url: str) -> str:
    domain = urlparse(url).netloc
    return domain


def get_protocol(url: str) -> str:
    protocol = url.split(':')[0]
    return protocol


def get_internal_links(links: list, domain: str, protocol: str) -> list:
    internal_links = []
    for link in links:
        href = link.get('href')
        if (href.startswith(f'{protocol}://{domain}') or href.startswith('/') or href.startswith(r'[a-zA-Z0-9-_]+/'))\
                and not href.startswith('//'):
            internal_links.append(link)
    return internal_links


def parser(url: str) -> list[str]:
    domain = get_domain(url)
    protocol = get_protocol(url)

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    internal = get_internal_links([link for link in soup.find_all('a') if link.has_attr('href')], domain, protocol)

    title = soup.find('title')
    write_parser_logs(url, title.string, internal, protocol, domain)

    internal = [get_url_from_tag(link, protocol, domain) for link in internal]

    return internal


def check_url(url: str) -> bool:
    return urlparse(url).scheme is not None


def get_url_from_tag(link: Tag, protocol: str, domain: str) -> str:
    href = link.get('href')
    return href if href.startswith(f'{protocol}://{domain}') else f'{protocol}://{domain}{href}'
