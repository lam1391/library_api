
# Library API (without framework)

Build a REST API which will allow our clients to consume the list of available books, as well as to read those books page by page in the desired formats.

For this first iteration the books will be available (page by page) in plain text and HTML. In future iterations, we would like to add support for more reading formats, as well as support to interface with other online book service providers.  

### Considerations
The following tools were used to build this project

| Consideration | Description     | 
| :-------- | :------- | 
| `Lenguage` | `Python 3.10.6` |
| `Operative System` | `Ubuntu` |
|`Server`  | `Gunicorn ` |

**If you don't have or use Ubuntu operating system you can install WSL for windows**







## Run Locally

Clone the project

```bash
  https://gitlab.com/gbh-candidates/luis-martinez-lam1391-2023-2-28-dev-backend-coding-challenge-library-api.git
```

Go to the project directory

```bash
  cd luis-martinez-lam1391-2023-2-28-dev-backend-coding-challenge-library-api
```

Create virtual enviroment
```bash
$: python3 -m venv virtualenv

$: source virtualenv/bin/activate
```

Install dependencies

```bash
(virtualenv)$pip install -r requirements.txt
```

Create Data base and tables and add seeds
```bash
(virtualenv)$python3 library_api/migration/migration.py
(virtualenv)$python3 library_api/loadSeeds.py
```

Start the server

```bash
gunicorn library_api.server:app --reload -w 5
```


## API Reference

#### Get all books avaible in library

```http
  GET /api/listofbook
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `any` | `none` | **Any** requeriment |

#### Get a book information

```http
  GET /api/book/{book_id} from the library
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `book_id`      | `number` | **Required**. Id of book to fetch |

#### Get a book page from the library

```http
  GET /api/book/{book_id}/page/{page_number}/{format}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `book_id`      | `number` | **Required** |
| `page_number`      | `number` | **Required** |
| `format`      | `string` | **Optional** if format is not specified, HTML will be returned by default. |




## Running Tests

to perform the test the server has to be running
To run tests, run the following command

```bash
  pytest tests/test_api.py
```