import sqlite3
from sqlite3.dbapi2 import Cursor, connect
import datetime


class StockModel:
    
    def __init__(self, id:int, symbol:str, name:str, enable:int) -> None:
        self.id = id
        self.symbol = symbol
        self.name = name
        self.enable = enable     
    
    def command_execute(self, query:str, params=None) -> tuple:
        connection = sqlite3.connect("stock_prices.db")
        cursor = connection.cursor()
        
        if params is None:
            cursor.execute(query)
            return cursor, connection

        cursor.execute(query,params)
        return cursor, connection

         
    
    @classmethod
    def find_by_id(cls, _id:int):
        result, connection = cls.command_execute(cls,"SELECT * FROM stock WHERE id=?",(_id))
        connection.close()
        print(result.fetchone())
        stock = cls(*result)
        return stock
    
    
    @classmethod
    def find_all_enabled(cls) -> list:
        result, connection = cls.command_execute(cls, "SELECT * FROM stock WHERE enabled=1")
        rows = result.fetchall()
        connection.close()
        return rows

    #teste apenas
    @staticmethod
    def filter(value):
        connection = sqlite3.connect("stock_prices.db")
        cursor = connection.cursor()
        r = cursor.execute("SELECT stockid FROM stock WHERE symbol = ?",(value,))
        r = r.fetchone()
        connection.close()
        return r


    
    




