from typing import Any
from library_api.models import LibraryDB


# function for handling the index page
def index() -> dict[str, Any]:
    context = {"status": "200 Ok"}
    context["data"] = "Hello, World!"

    return context


# function for getting a list of books
def get_book_list(library: LibraryDB):
    # get all the books from the library database
    books = library.get_books()
    if books:
        context = {"status": "200 Ok"}
        context["data"] = [dict(book) for book in books]
    else:
        context = {"status": "404 Ok"}
        context["data"] = {"error": "The requested data could not be found"}

    return context


# function for getting a book by ID
def get_book(environ, library: LibraryDB):
    # get the path of the current request
    path = environ.get("PATH_INFO")
    # split the path into a list of strings
    list_path = path.split("/")
    # get the book ID from the end of the path
    bookid = list_path[-1]
    # get the book from the library database using the book ID
    book = library.get_book(bookid)

    if book:
        row_dict = dict(book)
        context = {"status": "200 Ok"}
        context["data"] = row_dict
    else:
        context = {"status": "404 Ok"}
        context["data"] = {"error": "The requested data could not be found"}

    return context


# function for getting a book page by book ID, page number, and format
def get_book_page(environ, library: LibraryDB):
    # get the path of the current request
    path = environ.get("PATH_INFO")
    # split the path into a list of strings
    list_path = path.split("/")

    # get the book ID, page number and format from the path
    book_id = list_path[2]
    page_number = list_path[4]
    content_type = list_path[-1]

    # get the pages from the library database using the book ID, page number, and content type
    pages = library.get_pages(book_id, page_number, content_type)

    if pages:
        row_dict = dict(pages)
        context = {"status": "200 Ok"}
        context["data"] = row_dict["content"]
    else:
        context = {"status": "404 Ok"}
        context["data"] = {"error": "The requested data could not be found"}

    return context
