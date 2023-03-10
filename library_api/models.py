import sqlite3


# This is a class for a library database with various methods for CRUD operations
class LibraryDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    # Method for closing the database connection
    def close(self):
        self.conn.close()

    # Method for committing changes made to the database
    def commit(self):
        self.conn.commit()

    # Method for creating a new book record in the database
    def create_book(self, book_data):
        self.cursor.execute(
            """INSERT INTO books(title, author, publisher, publication_date, isbn, description)
                               VALUES(?,?,?,?,?,?)""",
            (
                book_data["title"],
                book_data["author"],
                book_data["publisher"],
                book_data["publication_date"],
                book_data["isbn"],
                book_data["description"],
            ),
        )
        book_id = self.cursor.lastrowid
        self.conn.commit()
        return book_id

    # Method for updating an existing book record in the database
    def update_book(self, book_id, book_data):
        self.cursor.execute(
            """UPDATE books SET title = ?, author = ?, publisher = ?, publication_date = ?,
                               isbn = ?, description = ?,  WHERE id = ?""",
            (
                book_data["title"],
                book_data["author"],
                book_data["publisher"],
                book_data["publication_date"],
                book_data["isbn"],
                book_data["description"],
                book_id,
            ),
        )

    # Method for deleting a book record from the database
    def delete_book(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        self.cursor.execute("DELETE FROM pages WHERE book_id = ?", (book_id,))

    # Method for getting all book records from the database
    def get_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        return books

    # Method for getting a specific book record from the database
    def get_book(self, book_id):
        self.cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        book = self.cursor.fetchone()
        return book

    # Method for creating a new page record in the database
    def create_page(self, page_data):
        self.cursor.execute(
            """INSERT INTO pages(book_id, page_number, content_type, content)
                               VALUES(?,?,?,?)""",
            (
                page_data["book_id"],
                page_data["page_number"],
                page_data["content_type"],
                page_data["content"],
            ),
        )
        page_id = self.cursor.lastrowid
        self.conn.commit()
        return page_id

    # Method for updating an existing page record in the database
    def update_page(self, page_id, page_data):
        self.cursor.execute(
            """UPDATE pages SET book_id = ?, page_number = ?, content_type = ?, content = ? WHERE id = ?""",
            (
                page_data["book_id"],
                page_data["page_number"],
                page_data["content_type"],
                page_data["content"],
                page_id,
            ),
        )

    # Method for deleting a page record from the database
    def delete_page(self, page_id):
        self.cursor.execute("DELETE FROM pages WHERE id = ?", (page_id))

    # Method for getting a specific page record from the database based on book id, page number and content type/format
    def get_pages(self, book_id, page_number, content_type):
        self.cursor.execute(
            "SELECT * FROM pages WHERE book_id = ? AND page_number = ? AND content_type = ?",
            (book_id, page_number, content_type),
        )
        pages = self.cursor.fetchone()
        return pages


"""support to interface with other online book service providers."""


class BookService:
    def search_books(self, query):
        pass

    def get_book_content(self, book_id, format, page_number):
        pass
