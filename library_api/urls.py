import json
import re

# Importing custom functions and database class
from library_api.handlers import get_book_list, get_book, get_book_page, index
from library_api.models import LibraryDB


def url_handlers(environ, start_reponse, library: LibraryDB):
    # Get the path from the request URL using the url_validation() function
    path = url_validation(environ.get("PATH_INFO"))
    # Get the request method
    method = environ.get("REQUEST_METHOD")

    if path == "":
        # If the path is empty, call the index() function to get the home page data
        context = index()
        # Convert the data to JSON or plain text, depending on the status code
        data = (
            json.dumps(context.get("data"))
            if context.get("data")
            else json.dumps(context.get("error"))
        )
        # Get the status code from the context dictionary
        status = context["status"]
        # Set the content type to JSON if the status code is less than 400, otherwise plain text
        content_type = (
            "application/json" if int(status.split(" ")[0]) < 400 else "text/plain"
        )

    elif path == "/listofbooks" and method == "GET":
        # If the path is "/listofbooks" and the method is "GET", call the get_book_list() bring all books avaible back
        context = get_book_list(library)
        data = (
            json.dumps(context.get("data"))
            if context.get("data")
            else json.dumps(context.get("error"))
        )
        status = context["status"]
        content_type = (
            "application/json" if int(status.split(" ")[0]) < 400 else "text/plain"
        )

    elif path == "/book" and method == "GET":
        # If the path is "/book" and the method is "GET", call the get_book() function that bring all the book informacion
        context = get_book(environ, library)
        data = (
            json.dumps(context.get("data"))
            if context.get("data")
            else json.dumps(context.get("error"))
        )
        status = context["status"]
        content_type = (
            "application/json" if int(status.split(" ")[0]) < 400 else "text/plain"
        )

    elif path == "/bookpage" and method == "GET":
        # If the path is "/bookpage" and the method is "GET", call the get_book_page() function that bring the page in a specific format
        context = get_book_page(environ, library)
        data = (
            json.dumps(context.get("data"))
            if context.get("data")
            else json.dumps(context.get("error"))
        )
        status = context["status"]
        content_type = "text/html" if int(status.split(" ")[0]) < 400 else "text/plain"

    elif path == "/bookServiceProvider" and method == "GET":
        # If the path is "/bookServiceProvider" and the method is "GET", should call a API provider services
        pass

    else:
        # if any method match will response error 404 not found
        data, status = json.dumps({"error": "404 URI Not Found"}), "404 URI Not Found"
        content_type = (
            "application/json" if int(status.split(" ")[0]) < 400 else "text/plain"
        )

    # Encode the data as UTF-8 and set the response headers
    data = data.encode("utf-8")
    response_headers = [
        ("Content-Type", content_type),
        ("Content-Length", str(len(data))),
    ]
    # Call the start_response function with the status code and response headers, and return the data
    start_reponse(status, response_headers)
    return data


def url_validation(input_text):
    if input_text.endswith("/"):
        input_text = input_text[:-1]

    # get initial page
    if input_text == "":
        return ""

    # get list of books
    pattern = re.compile(r"^/listofbooks$", re.IGNORECASE)
    if pattern.match(input_text):
        return "/listofbooks"

    # get a book
    pattern = re.compile(r"^/book/[0-9]+$", re.IGNORECASE)
    if pattern.match(input_text):
        return "/book"

    # get a page of a book
    pattern = re.compile(r"/book/[0-9]+/page/[0-9]+/[A-Za-z]+$", re.IGNORECASE)
    if pattern.match(input_text):
        return "/bookpage"

    return "error"
