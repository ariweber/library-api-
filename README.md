# Library API

## Project Description

This project is a simple library API.

The system is built with FastAPI and MySQL.

The API can manage books and library members.
It can also borrow books, return books, and show simple reports.


## Installations Docker MySQL

To create the MySQL container, run this command:


docker run --name library-mysql \
-e MYSQL_ROOT_PASSWORD=1234 \
-e MYSQL_DATABASE=library_db \
-p 3306:3306 \
-d mysql:latest


The database name is:
library_db

## Project Structure

```
library-api/
│
│
├── main.py
├── database/
│ ├── db_connection.py
│ ├── book_db.py
│ └── member_db.py
├── routes/
│ ├── book_routes.py
│ ├── member_routes.py
│ └── report_routes.py
├── logs/
│ └── app.log
│
├── README.md
├── requirements.txt
└── .gitignore
```


## Database Tables

### Books Table

The books table saves all the books in the library.

Fields:

* id | int auto-increment primary key
* title | varchar(200)
* author | varchar(200)
* genre  |enum('Fiction', 'Non-Fiction', 'Science', 'History', 'Other')
* is_available | boolean
* borrowed_by_member_id | nullable, foreign key to members.id


### Members Table

The members table saves all the library members.

Fields:

* id | int auto-increment primary key
* name | varchar(50)
* email | varchar(50) unique
* is_active | boolean
* total_borrows | int

## System Rules

* A new book is available by default.
* A genre must be one of the following: Fiction, Non-Fiction, Science, History, Other.
* A new member is active by default.
* Email must be unique.
* An inactive member cannot borrow books.
* A borrowed book cannot be borrowed again.
* A member can borrow up to 3 books at the same time.
* A book can be returned only by the member who borrowed it.

## Endpoints

### Books

POST /books
Create a new book

GET /books
Get all books

GET /books/{id}
Get book by id

PATCH /books/{id}
Update book

PATCH /books/{id}/borrow/{member_id}
Borrow book

PATCH /books/{id}/return/{member_id}
Return book

### Members

POST /members
Create a new member

GET /members
Get all members

GET /members/{id}
Get member by id

PATCH /members/{id}
Update member

PATCH /members/{id}/deactivate
Deactivate member

PATCH /members/{id}/activate
Activate member

### Reports

GET /reports/summary
Get general summary

GET /reports/books-by-genre
Count books by genre

GET /reports/top-member 
Get top member


## System Flow

First, the user creates a member.

Then, the user creates a book.

When a member borrows a book, the system checks:

* the book exists
* the member exists
* the member is active
* the book is available
* the member has less than 3 borrowed books

If all checks are valid, the book becomes not available.

When a member returns a book, the system checks that the same member really borrowed this book.

## Logging

Logs are saved in:
app/logs/app.log

Log format:
time | level | message



## How to Run

Install packages:
pip install -r requirements.txt
Start MySQL container:
docker start library-mysql

Create a venv:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Run the server:
uvicorn main:app --reload
The API will be available at:
http://localhost:8000/docs





