from typing import Iterator

from library_api.models import LibraryDB
from library_api.urls import url_handlers


def app(environ, start_reponse) -> Iterator[bytes]:
    # Creating an instance of the LibraryDB class and initializing it with the path to the database file
    library = LibraryDB("library.db")
    # Returning an iterator of bytes which contains the output from the url_handlers function
    # by passing the environment, start_response and library objects as parameters
    return iter([url_handlers(environ, start_reponse, library)])
