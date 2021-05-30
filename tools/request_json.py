import logging
from typing import Iterable
import requests
from requests import Response
from model.stock_model import StockModel
from tools.parse import parse_last_week


def integrate(api_key: str, symbol: str = "B3SA3.SAO") -> Iterable:
    """
    requisita os dados da api, encapsula os dados em uma lista e filtra os dados pela ultima semana do mes

        Parametros:
        ----------
             symbol:str -> identificador de ação do mercado

        Retorno:
        -------- 
            retorna uma lista de tuplas com os dados
    """

    URL: str = "https://www.alphavantage.co/query"
    QUERY = {"function": "TIME_SERIES_DAILY",
             "symbol": symbol,
             "apikey": api_key
             }

    data_request: Response = requests.get(URL, params=QUERY).json()
    data_keys = data_request["Time Series (Daily)"].keys()

    stockid = StockModel.filter(symbol)

    stockid = [stockid[0] for _ in range(len(data_keys))]

    _close = []
    _active = []

    for data in data_keys:
        _close.append(data_request["Time Series (Daily)"][data]["4. close"])
        _active.append(data_request["Time Series (Daily)"][data]["5. volume"])

    store = list(zip(data_keys, _active, _close, stockid))
    filtered_store = list(filter(parse_last_week, store))

    return filtered_store
