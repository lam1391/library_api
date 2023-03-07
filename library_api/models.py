import sqlite3


class LibraryDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

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

    def delete_book(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        self.cursor.execute("DELETE FROM pages WHERE book_id = ?", (book_id,))

    def get_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        return books

    def get_book(self, book_id):
        self.cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        book = self.cursor.fetchone()
        return book

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

    def delete_page(self, page_id):
        self.cursor.execute("DELETE FROM pages WHERE id = ?", (page_id,))

    def get_pages(self, book_id):
        self.cursor.execute(
            "SELECT * FROM pages WHERE book_id = ? ORDER BY page_number ASC", (book_id,)
        )
        pages = self.cursor.fetchall()
        return pages


class BookService:
    def convert_to_plain_text(self, content):
        # implementation to convert HTML, EPUB, PDF to plain text
        pass

    def convert_to_epub(self, content):
        # implementation to convert HTML, plain text, PDF to EPUB
        pass

    def convert_to_pdf(self, content):
        # implementation to convert HTML, plain text, EPUB to PDF
        pass

    # other format conversion methods
