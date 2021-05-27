import logging
from model.prices_model import PriceModel
from model.stock_model import StockModel
from tools.request_json import integrate
from tools.logger_cache import custom_logger
from datetime import timedelta

try:
    from timeloop import Timeloop
except ImportError as e:
    print(e, "pip install timeloop")



loop = Timeloop()
log = custom_logger(logging.DEBUG)


@loop.job(interval=timedelta(seconds=20))
def manager():
    log.info("INICIALIZANDO PROCESSO")

    # listas de cadastros filtrado (habilitados)
    stocks = StockModel.find_all_enabled() 
    

    for i in stocks:
        for j in integrate(i[1]):
            PriceModel.update(j)

    print(StockModel.select_join())
    

    log.info("FIM DO PROCESSO")
    


if __name__ == "__main__":

    loop.start(block=True)
