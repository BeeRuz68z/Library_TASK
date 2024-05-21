Book API
This API allows you to manage a collection of books.

Getting Started
To use the API, you can follow these steps:

Clone the repository: https://github.com/BeeRuz68z/Library_TASK.git

Install the required dependencies: pip install -r requirements.txt

Run the development server: python manage.py runserver

API Endpoints
1. Retrieve All Books
URL: /books/allbooks/
Method: GET
Success Response:
Code: 200
Content:
[
    {
        "id": 1,
        "title": "Example Book",
        "author": "John Doe",
        "publicationDate": "2022-01-01",
        "ISBN": "1234567890123"
    },
    {
        "id": 2,
        "title": "Another Book",
        "author": "Jane Smith",
        "publicationDate": "2022-02-01",
        "ISBN": "9876543210987"
    }
]
Error Response:
Code: 404
Content: { "message": "No books found" }
2. Retrieve a Book by ID
URL: /books/idbook/<int:id>/
Method: GET
Success Response:
Code: 200
Content:
{
    "id": 1,
    "title": "Example Book",
    "author": "John Doe",
    "publicationDate": "2022-01-01",
    "ISBN": "1234567890123"
}
Error Response:
Code: 404
Content: { "message": "Book not found" }
3. Create a New Book
URL: /books/createbook/
Method: POST
Input Format:
{
   "title": "New Book",
   "author": "New Author",
   "publicationDate": "2022-03-01",
   "ISBN": "1111111111111"
}


--**Success Response:**
Code: 201
Content:
{
    "id": 3,
    "title": "New Book",
    "author": "New Author",
    "publicationDate": "2022-03-01",
    "ISBN": "1111111111111"
}


Error Response:
Code: 400
Content: { "message": "Invalid data provided" }

--**Authentication**
Some API endpoints require authentication. You can obtain a token by sending a POST request to /api/token/ with your username and password in the request body.

--**Testing**
You can run tests by running: