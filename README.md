# bookstore_v

Book Management Application
This Django application provides functionality for managing books and includes a view function for handling GET and POST requests related to adding books.

Installation and Setup
Clone the Repository:


git clone https://github.com/your_username/your_repository.git
cd your_repository
Install Dependencies:


pip install -r requirements.txt
Run Database Migrations:


python manage.py migrate
Run the Development Server:


python manage.py runserver
The application will run at http://localhost:8000/.

Usage Example
Add a Book
Endpoint: /add_book/

Methods:

GET: Retrieve a list of all books.
POST: Add a new book.
Request Body Example:


{
  "author": "Author Name",
  "title": "Book Title",
  "price": 19.99
}
Note:

Author name must not exceed 50 characters and can only contain letters and spaces.
Book title must not exceed 100 characters and must consist of printable characters.
Success Response:


{
  "status": "success"
}
Error Response:


{
  "status": "error",
  "message": "Invalid data format"
}
Contributing
Feel free to open issues, report bugs, or suggest improvements. Contributions are welcome via GitHub's Issue system.

License
This project is licensed under the MIT License.
