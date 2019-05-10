import psycopg2


def create_table():
    conn = psycopg2.connect(
        dbname="store", password="123456789", user="postgres", host="localhost", port="5432",)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS store(
            item TEXT,
            quantity INTEGER,
            price REAL)""")
    conn.commit()
    conn.close()


create_table()


def populate_table(item, quantity, price):
    conn = psycopg2.connect(
        dbname="store", password="123456789", user="postgres", host="localhost", port="5432",)
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES('%s','%s','%s')" %
                (item, quantity, price))
    conn.commit()
    conn.close()


populate_table('Wine Glass', 8, 750)
populate_table('Coffee Cups', 650, 110)
populate_table('Nescaffe', 1671, 7)
populate_table('Tea cups', 673, 25)
