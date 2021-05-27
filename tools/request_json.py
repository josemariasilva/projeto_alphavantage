import logging
from typing import Iterable
import requests
from requests import Response
from model.stock_model import StockModel
from tools.parse_week import parse_last_week




def integrate(symbol:str = "B3SA3.SAO") -> Iterable:

    """Esta função é responsavel por integrar o sistema de requisição e encapsular os dados em uma lista

        parametros: symbol:str -> identificador de ação do mercado
        
        retorno: -> retorna uma lista de tuplas com os dados"""

    
    URL: str = "https://www.alphavantage.co/query"
    QUERY = {"function": "TIME_SERIES_DAILY",
             "symbol": symbol,
             "apikey": "P5J89M4KGGN95FLY"
             }

    
    data_request: Response = requests.get(URL, params=QUERY).json()
    data_symbol = data_request["Meta Data"]["2. Symbol"]
    data_keys = data_request["Time Series (Daily)"].keys()


    stockid = StockModel.filter(data_symbol)

    stockid = [stockid[0] for _ in range(len(data_keys))]

    _close = []
    _active = []

    for data in data_keys:
        _close.append(data_request["Time Series (Daily)"][data]["4. close"])
        _active.append(data_request["Time Series (Daily)"][data]["5. volume"])

    

    store = list(zip(data_keys, _active, _close, stockid))
    filtered_store = list(filter(parse_last_week, store))

    return filtered_store