import sqlite3


def database_connection():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""
            CREATE TABLE IF NOT EXISTS book
                (id INTEGER PRIMARY KEY,
                title text,
                author text,
                year text,
                isbn integer
                )
            
            """)
    conn.commit()
    conn.close()


def populate_bookstore(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",
                (title, author, year, isbn))
    conn.commit()
    conn.close()


def view_book():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book ")
    rows = cur.fetchall()
    conn.close()
    return rows


def search_book(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_book(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=? ", (id,))
    conn.commit()
    conn.close()


def update_book(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=? ", (title, author, year, isbn, id))
    conn.commit()
    conn.close()


database_connection()
#populate_database("The Sun", "Hussein Machozi", 1994, 198982384)
# update_book(4, "The Underworld", 'Hussein Machozi', 1994, 198982384)
# print(view_book())
# print(search_book(author='Hussein Machozi'))
