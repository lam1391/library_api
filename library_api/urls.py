import json
from library_api.handlers import get_book_list, get_book, get_book_page, index
from library_api.models import Book


def url_handlers(environ, start_reponse, library):
    path = environ.get("PATH_INFO")

    if path.endswith("/"):
        path = path[:-1]

    if path == "":
        context = index(environ)
        data = (
            json.dumps(context.get("data"))
            if context.get("data")
            else json.dumps(context.get("error"))
        )
        status = context["status"]

    elif path == "/allbooks":
        context = get_book_list(environ, library)
        data = (
            json.dumps(context.get("data"))
            if context.get("data")
            else json.dumps(context.get("error"))
        )
        status = context["status"]

    else:
        data, status = json.dumps({"error": "404 Not Found"}), "400 Not FOund"

    data = data.encode("utf-8")
    content_type = (
        "application/json" if int(status.split(" ")[0]) < 400 else "text/plain"
    )
    response_headers = [
        ("Content-Type", content_type),
        ("Content-Length", str(len(data))),
    ]

    start_reponse(status, response_headers)
    return data
