from typing import Iterator

from library_api.models import LibraryDB
from library_api.urls import url_handlers


def app(environ, start_reponse) -> Iterator[bytes]:
    library = LibraryDB()
    return iter([url_handlers(environ, start_reponse, library)])
