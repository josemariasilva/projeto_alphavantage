import logging
from sqlite3.dbapi2 import OperationalError, connect
from tools.parse import parse_arg
from model.prices_model import PriceModel
from model.stock_model import StockModel
from tools.request_json import integrate
from tools.logger import custom_logger
from datetime import timedelta
from tools.db_manager import create_db_table, update_table

try:
    from timeloop import Timeloop
except ImportError as e:
    print(e, "pip install timeloop")


loop = Timeloop()
log = custom_logger(logging.DEBUG)


@loop.job(interval=timedelta(seconds=20))
def main():
    """
    Inicializa o processo de requisição por argumentos passados pelo terminal.

    --Analisa os argumentos inseridos na execução do script, cria o banco de dados ou\n
    altera.

    --Requisita as informações da Alphavantage_api e armazena no banco de dados ou altera caso existir o mesmo cadastro,
    com preço diferente.
    """

    try:
        parse_arg()
    except [ValueError, OperationalError] as e:
        print(
            e, "Argumentos invalidos: --create [symbol:str,name:str,enabled:int] | --update [symbol:str, enabled:int]")

    # listas de cadastros filtrado (habilitados)
    stocks = StockModel.find_all_enabled()

    log.info(f"INICIALIZANDO REQUISIÇÃO...")

    try:
        for i in stocks:

            for j in integrate(i[1]):
                PriceModel.update(j)
    except:
        log.info("FALHA NA REQUISIÇÃO, SIMBOLO INVALIDO")
        loop.stop()


if __name__ == "__main__":

    loop.start(block=True)
