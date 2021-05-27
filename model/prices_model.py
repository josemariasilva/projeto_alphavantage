import logging
from os import curdir
import sqlite3
import datetime
from sqlite3.dbapi2 import Cursor
from typing import Iterable
from model.stock_model import StockModel
from tools.logger_cache import custom_logger


class PriceModel(StockModel):

    

    """Classe modelo para o gerenciamento do banco de dados na tabela de preços das ações

    Parametros
    ----------
    _id : int
        identificador da ação

    date : datetime
        data da ação

    active : float
        ativos da ação

    price : float
        preço ou fechamento da ação

    Atributos
    ----------
    _id : int,
    date : datetime,
    active : float,
    price : float

    armazenados na classe
    """

    def __init__(self, _id: int, date: datetime, active: float, price: float) -> None:
        self._id = _id
        self.date = date
        self.active = active
        self.price = price

    @classmethod
    def insert_table(cls, args: Iterable) -> None:
        """
        Método da classe responsavel por inserir os dados na tabela (prices) do banco de dados.

        Parametros
        ----------
        args : Iterable
            conjunto de dados a serem inseridos na tabela (n=5)

        Retorno
        ----------
            None
        """

        cursor, connection = cls.command_execute(
            cls, "INSERT INTO prices(date, active, price, stockid) VALUES(?, ?, ?, ?)", args)
        connection.commit()
        connection.close()

    @classmethod
    def find_all(cls, _id: int) -> Iterable:
        """
        Método da classe responsavel por pegar todos os dados respectivo ao [id] da tabela(prices).

        Parametros
        ----------
        _id : int
            identificador do tipo de ação

        Retorno
        ----------
        uma lista contendo as linhas filtradas pelo respectivo [id]
        """

        cursor, connection = cls.command_execute(
            cls, "SELECT * FROM prices WHERE stockid = ?", (_id,))
        result = cursor.fetchall()
        connection.close()
        return result

    @classmethod
    def update(cls, data: Iterable) -> None:
        """
        Metodo da classe que atualiza a tabela verificando se esta cadastrado apartir da date, 
        caso contrario sera inserido ou o preço sera atualizado.

        Parametros
        ----------
        data : Iterable
            conjunto de dados a serem inseridos na tabela (n=4)

        Retorno
        ----------
            None
        """

        cursor, connection = cls.command_execute(
            cls, "SELECT * FROM prices WHERE date = ? AND stockid = ?", (data[0],data[3]))
        row = cursor.fetchone()

        if row is not None:
            cursor.execute(
                "UPDATE prices SET price = ? WHERE date = ? AND stockid = ?", (data[2], data[0], data[3]))
            connection.commit()
            connection.close()
            
        else:
            cls.insert_table(data)
            
