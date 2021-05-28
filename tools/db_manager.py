import sqlite3
from sqlite3.dbapi2 import Cursor
from typing import Iterable

def create_db_table(values:Iterable):

    "Cria  banco de dados e as tabelas, insere na tabela stock se tiver argumentos"
    print(values)
    cdb = sqlite3.connect("stock_prices.db")
    cursor = cdb.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS stock (
                            stockid INTEGER PRIMARY KEY AUTOINCREMENT,
                            symbol VARCHAR(20),
                            name VARCHAR(20),
                            enabled BOOLEAN)
                            """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS prices (
                            priceid INTEGER PRIMARY KEY AUTOINCREMENT,
                            date DATETIME,
                            active INTEGER,
                            price DOUBLE,
                            stockid INTEGER,
                            FOREIGN KEY(stockid) REFERENCES stock(stockid)
                            )""")
    if len(values) == 3: 
        cursor.execute("INSERT INTO stock(symbol, name, enabled) VALUES(?, ?, ?)", (values[0], values[1], int(values[2])))

    cdb.commit()
    cdb.close()

def update_table(values:Iterable):
    "Atualiza modo de operação do cadastro."

    if len(values) == 2:
        udb = sqlite3.connect("stock_prices.db")
        cursor = udb.cursor()
        udb.execute("UPDATE stock SET enabled = ? WHERE symbol = ? ", (int(values[1]), values[0]))

        udb.commit()
        udb.close()

    
    

    
