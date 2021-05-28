import sqlite3
from typing import Any, Iterable



class StockModel:

    """Classe modelo para o gerenciamento do banco de dados na tabela de stock das ações"""

    @staticmethod
    def command_execute(query: str, params: Any = None) -> Iterable:
        """
        simplifica as chamadas e conexões com o banco de dados.

        Parametros
        ----------
        query : str
            instrução da query passada para o banco de dados

        params : Any
            parametros passados como argumento de uma query

        Retorno
        ----------
            None
        """

        connection = sqlite3.connect("stock_prices.db")
        cursor = connection.cursor()

        if params is None:
            cursor.execute(query)
            return cursor, connection

        cursor.execute(query, params)
        return cursor, connection

    @staticmethod
    def find_all_enabled() -> Iterable[Any]:
        """
        Filtra apenas os cadatros hablitados no banco de dados.

        Retorno
        --------
            retorna uma lista de cadastros habilitados
        """

        result, connection = StockModel.command_execute(
            "SELECT * FROM stock WHERE enabled=1")
        rows = result.fetchall()
        connection.close()
        return rows

    @staticmethod
    def filter(value: str) -> Iterable[int]:
        """
        Filtra os cadastros pelo simbolo.

        Parametros
        ---------
            value : Iterable



        Retorno
        --------
            retorna o indice do cadastro atraves do simbolo
        """
        connection = sqlite3.connect("stock_prices.db")
        cursor = connection.cursor()
        r = cursor.execute(
            "SELECT stockid FROM stock WHERE symbol = ?", (value,)).fetchone()

        connection.close()
        return r
