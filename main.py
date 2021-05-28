import logging
from model.prices_model import PriceModel
from model.stock_model import StockModel
from tools.request_json import integrate
from tools.logger import custom_logger
from datetime import timedelta

try:
    from timeloop import Timeloop
except ImportError as e:
    print(e, "pip install timeloop")



loop = Timeloop()
log = custom_logger(logging.DEBUG)


@loop.job(interval=timedelta(seconds=168))
def main():
    

    # listas de cadastros filtrado (habilitados)
    stocks = StockModel.find_all_enabled() 
    
    log.info(f"INICIALIZANDO REQUISIÇÃO...")

    for i in stocks:
        
        for j in integrate(i[1]):
            PriceModel.update(j)

    log.info("ARMAZENAMENTO COMPLETO, FIM DO PROCESSO.!")

    
    


if __name__ == "__main__":

    loop.start(block=True)
