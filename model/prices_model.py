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
    def insert_table(cls, args) -> None:
        cursor, connection = cls.command_execute(cls, "INSERT INTO prices VALUES(NULL, ?, ?, ?, ?)",args)


    @classmethod
    def find_all(cls, _id:int) -> list:
        cursor, connection = cls.command_execute(cls, "SELECT * FROM prices WHERE stockid = ?", (_id,))
        result = cursor.fetchall()
        connection.close()
        return result

    @classmethod
    def update(cls, data):
        cursor, connection = cls.command_execute("SELECT * FROM prices WHERE date = ? ", (data[1],))
        row = cursor.fetchone()

        if cursor is None:
            cls.insert_table(*row)
        else:
            cursor.execute("UPDATE prices SET price = ? WHERE date = ?",(data[2], data[1]))
        
        connection.commit()
        connection.close()


        
            

            
        
        
