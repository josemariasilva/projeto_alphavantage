
from model.prices_model import PriceModel
import requests
from requests import Response
from model.stock_model import StockModel


def run():
    # Definição de parametros do projeto

    stocks = StockModel.find_all_enabled()
    for i in stocks:
        print(i)

    print("="*100)
    # id de inserção da tabela price
    for i in integrate():
        PriceModel.insert_table(i)
    print("=="*50)

    for i in integrate("PETR4.SAO"):
        PriceModel.insert_table(i)

    print(PriceModel.find_all(0))
    print("=="*50)
    print(PriceModel.find_all(1))
    
    

    

def integrate(symbol:str = "B3SA3.SAO") -> tuple:

    
    URL: str = "https://www.alphavantage.co/query"
    QUERY = {"function": "TIME_SERIES_DAILY",
             "symbol": symbol,
             "apikey": "P5J89M4KGGN95FLY"
             }
    test: Response = requests.get(URL, params=QUERY).json()
    stockid = StockModel.filter(test["Meta Data"]["2. Symbol"])
    data_keys = test["Time Series (Daily)"].keys()

    stockid = [stockid[0] for _ in range(len(data_keys))]

    _close = []
    _active = []

    for data in data_keys:
        _close.append(test["Time Series (Daily)"][data]["4. close"])
        _active.append(test["Time Series (Daily)"][data]["5. volume"])
    
    tutu = zip(data_keys, _active, _close, stockid)

    return tutu

    


if __name__ == "__main__":
    run()
