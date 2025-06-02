Description:
------------
An example project of a management system for a book store. This is a Python Flask project which allows includes a table for storing book models with title, author, price,
and stock values in a MongoDB Atlas database. The app includes functionality for viewing the books, adding new books, updating existing book, and deleting existing books.
The information for adding and updating books is done via a form. The project is containerized with docker and deployed with Google Cloud Run. 

Please note:
------------
This app does not include authentication; it is intended as a demonstration of a theoretical management system.

Before Using:
-------------
A MongoDB DB_USERNAME and DB_PASSWORD are needed for the app to properly function. Please ensure the mongo connections string variables are properly implemented with MongoDB credentials.
Please ensure MongoDB environmental variables are present for:

DB_USERNAME = <your_mongodb_username>
DB_PASSWORD = <your__mongodb_password>

How To Use:
-----------
The application starts on the homepage where the user can view the books that are in the database or add a new book. 
Pressing the view books button will take the table that shows are existing books and their title, author, price, and stock as well as an update and delete button.
Pressing the add book button will take the user to an add book form where they can fill in a new books informaiton and upon hitting submit it will be added to the database.
Pressing the update button will take the user to a pre-filled update book form with the book's current informtion. The information can be updated and upon hitting submit will update the books informaiton.
The delete button will delete the book it is aligned with on the table form the database.


