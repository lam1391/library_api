import json
import re
from models import LibraryDB

# library = LibraryDB("./library_api/library.db")
# book = library.get_book(1)
# row_dict = dict(book)
# # convert the dictionary to a JSON string
# json_string = json.dumps(row_dict)

# # print the JSON string
# print(json_string)


def use_regex(input_text):
    if input_text.endswith("/"):
        input_text = input_text[:-1]

    # get initial page
    if input_text == "":
        return ""

    # get list of book
    pattern = re.compile(r"/listofbooks+", re.IGNORECASE)
    if pattern.match(input_text):
        return "/listofbooks"

    # get a book
    pattern = re.compile(r"^/book/[0-9]+$", re.IGNORECASE)
    if pattern.match(input_text):
        return "/book"

    # get a page of a book
    pattern = re.compile(r"/book/[0-9]+/page/[0-9]?/[A-Za-z]+$", re.IGNORECASE)
    if pattern.match(input_text):
        return "/bookpage"

    return "error"


expresion = "/book/12222/page/32323/fsdfsd"
print(use_regex(expresion))
