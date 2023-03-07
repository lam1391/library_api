import sqlite3

# create a connection to the database
conn = sqlite3.connect("library.db")

# create a cursor object to execute SQL queries
c = conn.cursor()

# create the books table
c.execute(
    "CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, publisher TEXT, publication_date DATE, isbn TEXT, description TEXT)"
)

# create the pages table
c.execute(
    "CREATE TABLE pages (id INTEGER PRIMARY KEY, book_id INTEGER, page_number INTEGER, content_type TEXT, content TEXT)"
)

conn.commit()
conn.close()
