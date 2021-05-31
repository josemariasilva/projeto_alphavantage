import argparse
import logging
import threading
from tools.parse import parse_arg
from model.prices_model import PriceModel
from model.stock_model import StockModel
from tools.request_json import integrate
from tools.logger import custom_logger


log = custom_logger(logging.DEBUG)

def main(api_key):
    """
    Inicializa o processo de requisição por argumentos passados pelo terminal.

    --Analisa os argumentos inseridos na execução do script, cria o banco de dados ou\n
    altera.

    --Requisita as informações da Alphavantage_api e armazena no banco de dados ou altera caso existir o mesmo cadastro,
    com preço diferente.
    """

    
    # listas de cadastros filtrado (habilitados)
    stocks = StockModel.find_all_enabled()

    log.info(f"INICIALIZANDO REQUISIÇÃO...")

    try:
        for i in stocks:

            for j in integrate(api_key, i[1]):
                PriceModel.update(j)
    except:
        log.info("FALHA NA REQUISIÇÃO, SIMBOLO INVALIDO OU APIKEY INVALIDA")
        
    log.info("REQUISIÇÃO COMPLETA.")


if __name__ == "__main__":



    result = parse_arg()
    if result[0]:
        log.info("ALTERAÇÃO COMPLETA.")
    else:
        t1 = threading.Timer(168, main(result))
        t1.start()
    