Building a simple Django REST API for managing a library of books. The API should allow
users to perform CRUD operations (Create, Read, Update, Delete) on books stored in a database. Each book
should have the following attributes: title, author, publication date, and ISBN number.
IMPLEMENTATION:
1. Create a Django project named "LibraryAPI" with a Django app named "books".
2. Define a model named Book in the "books" app with the necessary fields (title, author, publication
date, ISBN).
3. Implement REST API endpoints for the following operations:
• List all books
• Retrieve a single book by its ID
• Create a new book
• Update an existing book
• Delete a book
4. Ensure that the API responses conform to RESTful standards.
5. Implement proper input validation and error handling.
6. Use Django's built-in authentication and authorization system to restrict access to certain endpoints:
• Only authenticated users should be able to create, update, and delete books.
• All users (authenticated or not) should be able to list books and retrieve a single book.
7. Write unit tests to validate the functionality of your API.
8. Implement filtering, searching, or pagination functionality for listing books.
9. Add support for user authentication using Django's token authentication and JWT.
