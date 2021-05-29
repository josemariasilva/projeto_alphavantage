import logging
from tools.logger import custom_logger
from typing import Any, Iterable
from model.stock_model import StockModel


log = custom_logger(logging.DEBUG)


class PriceModel(StockModel):

    """Classe modelo para o gerenciamento do banco de dados na tabela de preços das ações"""

    @staticmethod
    def insert_table(args: Iterable[Any]) -> None:
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

        cursor, connection = PriceModel.command_execute(
            "INSERT INTO prices(date, active, price, stockid) VALUES(?, ?, ?, ?)", args)
        connection.commit()
        connection.close()

    @staticmethod
    def find_all(_id: int) -> Iterable[Any]:
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

        cursor, connection = PriceModel.command_execute(
            "SELECT * FROM prices WHERE stockid = ?", (_id,))
        result = cursor.fetchall()
        connection.close()
        return result

    @staticmethod
    def update(data: Iterable[Any]) -> None:
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

        cursor, connection = PriceModel.command_execute(
            "SELECT * FROM prices WHERE date = ? AND stockid = ?", (data[0], data[3]))
        row = cursor.fetchone()

        if row is not None:
            cursor.execute(
                "UPDATE prices SET price = ? WHERE (date = ? AND stockid = ? AND price != ?)", (data[2], data[0], data[3], data[2]))

            connection.commit()
            connection.close()

        else:
            PriceModel.insert_table(data)
