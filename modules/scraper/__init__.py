#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from time import sleep


def cmc_exchange_generator():
    cmc_url = 'https://coinmarketcap.com/'
    url_prefix = 'https://coinmarketcap.com/rankings/exchanges/'

    for page_number in range(1, 4):
        url = url_prefix + str(page_number)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        a_tags = soup.find_all('a')
        for a in a_tags:
            try:
                if re.match(r'^/exchanges/.*/$', a['href']) and a.text.strip() != '' and 'Ranking' not in a.text:
                    yield (urllib.parse.urljoin(cmc_url, a['href']))
            except KeyError:
                pass


def _render_exchange_info(cmc_exchange_url):
    r = requests.get(cmc_exchange_url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        exchange_name = soup.find('h1').text.strip()
        exchange_info_items = soup.find('ul', class_='list-unstyled').find_all('span')
        exchange_info_urls = soup.find('ul', class_='list-unstyled').find_all('a')
        keys = [item.get('title').lower() for item in exchange_info_items[:len(exchange_info_urls)]]
        values = [item.get('href') for item in exchange_info_urls]
        exchange_info = dict(zip(keys, values))
        exchange_info['exchange_name'] = exchange_name.lower()
        return exchange_info
    else:
        return None


def get_cmc_exchange_info():
    """
    generator
    :return: top 300 exchanges ranked by CoinMarketCap.com
    """
    # exchange_array = []
    exchanges = cmc_exchange_generator()
    for exchange in exchanges:
        # exchange_array.append(_render_exchange_info(exchange))
        # print(_render_exchange_info(exchange))
        sleep(10)
        yield _render_exchange_info(exchange)
    # return exchange_array
