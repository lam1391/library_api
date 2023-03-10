import requests


# response should be ok status 200
def test_get_list_of_books():
    response = requests.get("http://127.0.0.1:8000/listofbooks")
    assert response.status_code == 200


# response should be ok status 200
def test_get_a_book():
    response = requests.get("http://127.0.0.1:8000/book/1")
    assert response.status_code == 200


# response should be NOT ok data no found error 404
def test_book_not_found():
    response = requests.get("http://127.0.0.1:8000/book/165")
    assert response.status_code == 404


# response should be ok status 200
def test_get_a_book_page():
    response = requests.get("http://127.0.0.1:8000/book/1/page/1/html")
    assert response.status_code == 200


# response should be NOT ok data no found error 404
def test_book_page_not_found():
    response = requests.get("http://127.0.0.1:8000/book/1/page/155")
    assert response.status_code == 404


# response should be NOT ok Method no found error 404
def api_method_not_found():
    response = requests.get("http://127.0.0.1:8000/list/")
    assert response.status_code == 404
