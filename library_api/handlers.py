from typing import Any
from urllib import parse
from models import LibraryDB


def index(environ) -> dict[str, Any]:
    """Display the in-memory data to users."""
    request_params = dict(parse.parse_qsl(parse.urlsplit(environ.get("RAW_URI")).query))

    context = {"status": "200 Ok"}
    context["data"] = "Hello, World!"

    return context


def get_book_list(environ, library: LibraryDB):
    """Use query parameters to transfer money from a user to another."""
    if parse.parse_qsl(parse.urlsplit(environ.get("RAW_URI")).query) == "":
        return {"error": "405 Method Not Allowed", "status": "405 Method Not Allowed"}
    request_meta_query = dict(
        parse.parse_qsl(parse.urlsplit(environ.get("RAW_URI")).query)
    )
    if not request_meta_query:
        return {"error": "Query must be provided.", "status": "405 Method Not Allowed"}

    return library.get_books()


# def get_book(self, query):
#     results = []
#     # search local library
#     for book in self.library.books:
#         if query in book.title or query in book.author:
#             results.append({"title": book.title, "author": book.author})
#     # search external book providers
#     provider_results = self.book_provider.search_books(query)
#     for result in provider_results:
#         results.append({"title": result["title"], "author": result["author"]})
#     return results


# def get_book_page(self, title, page_number, format):
#     book = self.library.get_book_by_title(title)
#     if book:
#         return book.get_page(page_number, format)
