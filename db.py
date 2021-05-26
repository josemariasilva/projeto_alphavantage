import sqlite3


def createDb() -> None:

    connect = sqlite3.connect("stock_prices.db")
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE stock (
                            stockid INTEGER PRIMARY KEY AUTOINCREMENT,
                            symbol VARCHAR(20),
                            name VARCHAR(20),
                            enabled BOOLEAN)""")


    
    cursor.execute("INSERT INTO stock VALUES(0,'B3SA3.SAO', 'Brasil, Bolsa Balcão', 1)")
    cursor.execute("INSERT INTO stock VALUES(1,'PETR4.SAO', 'Petroleo Brasileiro SA Petrobras', 1)")


    cursor.execute("""CREATE TABLE prices (
                            priceAid INTEGER PRIMARY KEY AUTOINCREMENT,
                            date DATETIME,
                            active INTEGER,
                            price DOUBLE,
                            stockid INTEGER,
                            FOREIGN KEY(stockid) REFERENCES stock(stockid)
                            )""")



    connect.commit()
    connect.close()

if __name__ == "__main__":
    createDb()
    
