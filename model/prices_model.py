from os import curdir
import sqlite3
import datetime
from sqlite3.dbapi2 import Cursor
from model.stock_model import StockModel



class PriceModel(StockModel):

    def __init__(self, _id:int, date:datetime, active:float, price:float) -> None:
        self._id = _id
        self.date = date
        self.active  = active
        self.price = price



    @classmethod
    def find_by_date(cls, date:datetime):
        query = """SELECT *"""
        result, connection = cls.command_execute("")
    
    @classmethod
    def insert_table(cls, args) -> None:
        cursor, connection = cls.command_execute(cls, "INSERT INTO prices VALUES(NULL, ?, ?, ?, ?)",args)
        connection.commit()
        connection.close()

        

    @classmethod
    def find_specifie_table(cls, symbol:str):
        cursor, connection = cls.command_execute()

    @classmethod
    def find_all(cls, _id:int) -> list:
        cursor, connection = cls.command_execute(cls, "SELECT * FROM prices WHERE stockid = ?", (_id,))
        result = cursor.fetchall()
        connection.close()
        return result
        
