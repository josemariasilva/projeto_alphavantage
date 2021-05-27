import logging
import sqlite3
from sqlite3.dbapi2 import Cursor, connect
import datetime
from typing import Any, Iterable
from tools.logger_cache import custom_logger


class StockModel:

    """Classe modelo para o gerenciamento do banco de dados na tabela de stock das ações

    Parametros
    ----------
    _id : int
        indice da ação

    symbol : str
        identificador da ação

    name : str
        nome da ação

    enabled : float
        marcador de utlização

    Atributos
    ----------
    _id : int,
    symbol : datetime,
    name : float,
    enabled : float

    armazenados na classe
    """

    def __init__(self, id: int, symbol: str, name: str, enable: bool) -> None:
        self.id = id
        self.symbol = symbol
        self.name = name
        self.enable = enable

    def command_execute(self, query: str, params: Any = None) -> Iterable:
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

    @classmethod
    def find_by_id(cls, _id: int):
        result, connection = cls.command_execute(
            cls, "SELECT * FROM stock WHERE id=?", (_id))
        connection.close()
        print(result.fetchone())
        stock = cls(*result)
        return stock

    @classmethod
    def find_all_enabled(cls) -> Iterable:
        """
        Filtra apenas os cadatros hablitados no banco de dados.

        Retorno
        --------
            retorna uma lista de cadastros habilitados
        """

        result, connection = cls.command_execute(
            cls, "SELECT * FROM stock WHERE enabled=1")
        rows = result.fetchall()
        connection.close()
        return rows

    @staticmethod
    def filter(value: str) -> Iterable:
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
            "SELECT stockid FROM stock WHERE symbol = ?", (value,))
        r = r.fetchone()
        connection.close()
        return r

    @staticmethod
    def select_join() -> Iterable:
        connection = sqlite3.connect("stock_prices.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM prices")
        result = cursor.fetchall()
        connection.close()
        return result
