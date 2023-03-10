import json
from models import LibraryDB

db = LibraryDB("./library.db")

data_json = {}
file = open("./library_api/seeds/books.json")
books = json.load(file)

# insert the books into the database and get their IDs
for book in books:
    c = db.create_book(book)
    # create some sample pages for the books
    for page in book["pages"]:
        new_page = {}
        new_page["book_id"] = c
        new_page["page_number"] = page["page_number"]
        for format in page["formats"]:
            new_page["content_type"] = format["content_type"]
            new_page["content"] = format["content"]
            d = db.create_page(new_page)


db.commit()
db.close()
