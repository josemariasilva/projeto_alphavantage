import logging
from sqlite3.dbapi2 import OperationalError
import threading
from tools.parse import parse_arg
from model.prices_model import PriceModel
from model.stock_model import StockModel
from tools.request_json import integrate
from tools.logger import custom_logger


log = custom_logger(logging.DEBUG)


def main():
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

            for j in integrate(i[1]):
                PriceModel.update(j)
    except:
        log.info("FALHA NA REQUISIÇÃO, SIMBOLO INVALIDO")
        
    log.info("REQUISIÇÃO COMPLETA.")


if __name__ == "__main__":

    #
    if parse_arg():
        log.info("ALTERAÇÃO COMPLETA.")
    else:
        t1 = threading.Timer(20, main())
        t1.start()
    