#!/usr/bin/env python
# Download CoinMarketCap.com exchanges' info and upload them to mongodb
import os
from modules.scraper import get_cmc_exchange_info
from configparser import ConfigParser
from pymongo import MongoClient

def main():

    # Load the initial configuration
    cwd = os.path.split(__file__)[0]
    config_file = os.path.join(cwd, 'config.ini')

    # Get exchanges' info
    exchanges = get_cmc_exchange_info()

    # bulk insert to mongodb
    config = ConfigParser()
    config.read(config_file)
    mongodb_username = config['mongodb']['username']
    mongodb_password = config['mongodb']['password']
    mongodb_ip = config['mongodb']['ip']
    database_name = config['mongodb']['database_name']
    collection_name = config['mongodb']['collection_name']
    mongodb_uri = 'mongodb://{}:{}@{}:27017/'.format(
        mongodb_username,
        mongodb_password,
        mongodb_ip
    )

    client = MongoClient(mongodb_uri)
    database = client[database_name]
    collection = database[collection_name]

    for exchange in exchanges:
        print(exchange)
        exchange_name = exchange['exchange_name']
        collection.replace_one({'exchange_name': exchange_name}, exchange, True)
        # collection.insert_one(exchange)

    client.close()


if __name__ == "__main__":
    main()
