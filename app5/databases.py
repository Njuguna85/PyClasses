"""
    Interacting with databases follows these steps
    1. Connecting to a database
    2. Create a cursor object (pointer)
    3. Write an SQL query
    4. Commit changes
    5. Close the connection

"""
import sqlite3


def create_table():
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS store")
    cur.execute("""
        CREATE TABLE store(
            item TEXT,
            quantity INTEGER,
            price REAL)""")
    conn.commit()
    conn.close()


def populate_table(item, quantity, price):
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


create_table()
populate_table('Wine Glass', 8, 750)
populate_table('Coffee Cups', 650, 110)
populate_table('Nescaffe', 1671, 7)
populate_table('Tea cups', 673, 25)


def view_data():
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    cur.execute(
        """
            SELECT * FROM store
        """
    )
    rows = cur.fetchall()
    conn.close()

    return rows


def update_store(quantity, price, item):
    conn = sqlite3.connect("store.db")
    curs = conn.cursor()
    curs.execute("UPDATE store SET quantity=?, price=? WHERE item=?",
                 (quantity, price, item))
    conn.commit()
    conn.close()


update_store(630, 6.5, 'Nescaffe')


print(view_data())
