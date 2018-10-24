import pymongo #librarry to comunicate with mongodb
import requests #library to get request
from collections import OrderedDict
from hashlib import sha512

api_url="https://api.coinmarketcap.com/v1/ticker/"

#Connection
def get_db_connection(uri):
    client= pymongo.MongoClient(uri)
    return client.cryptongo

#get data of api
def get_cryptocurrecies_from_api():
    r=requests.get(api_url)
    if r.status_code==200:
        result=r.json()
        return result

    raise exception('Api error')

# Validation
def firts_element(elements):
     return elements[0]

def get_hash(value):
        return sha512(
        value.encode('utf-8')
    ).hexdigest()

def get_ticker_hash(ticker_data):
    ticker_data= OrderedDict(
        sorted(
            ticker_data.items(),
            key=firts_element
        )
    )

    ticker_value=''
    for _, value in ticker_data.items():
        ticker_value += str(value)
    return get_hash(ticker_value)

def check_if_exists(db_connection,ticker_data):
    ticker_hash = get_ticker_hash(ticker_data)

    if db_connection.tickers.find_one({"ticker_hash": ticker_hash}):
        return True
    return False
# save
def save_ticker(db_connection, ticker_data=None):
    if not ticker_data:
        return False
    if check_if_exists(db_connection,ticker_data):
        return False
    ticker_hash=get_ticker_hash (ticker_data)
    ticker_data['ticker_hash']=ticker_hash
    ticker_data['rank']=int(ticker_data['rank'])
    ticker_data['last_updated']=int(ticker_data['last_updated'])

    db_connection.tickers.insert_one(ticker_data)
    return True

if  __name__=='__main__':
    Connection = get_db_connection('mongodb://localhost:27017')
    tickers= get_cryptocurrecies_from_api()
    for ticker in tickers:
        save_ticker(Connection, ticker)
    print("done")
