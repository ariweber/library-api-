# Library API

## Project Description

This project is a simple library API.

The system is built with FastAPI and MySQL.

The API can manage books and library members.
It can also borrow books, return books, and show simple reports.


## Docker MySQL

To create the MySQL container, run this command:


docker run --name library-mysql \
-e MYSQL_ROOT_PASSWORD=1234 \
-e MYSQL_DATABASE=library_db \
-p 3306:3306 \
-d mysql:latest


The database name is:


library_db

## Project Structure

```text
library-api/
│
├── app/
│   ├── main.py
│   ├── database/
│   │   ├── db_connection.py
│   │   ├── book_db.py
│   │   └── member_db.py
│   ├── routes/
│   │   ├── book_routes.py
│   │   ├── member_routes.py
│   │   └── report_routes.py
│   └── logs/
│       └── app.log
│
├── README.md
├── requirements.txt
└── .gitignore


## Database Tables

### Books Table

The books table saves all the books in the library.

Fields:

* id
* title
* author
* genre
* is_available
* borrowed_by_member_id

Allowed genres:


Fiction
Non-Fiction
Science
History
Other


### Members Table

The members table saves all the library members.

Fields:

* id
* name
* email
* is_active
* total_borrows

## System Rules

* A new book is available by default.
* A new member is active by default.
* Email must be unique.
* An inactive member cannot borrow books.
* A borrowed book cannot be borrowed again.
* A member can borrow up to 3 books at the same time.
* A book can be returned only by the member who borrowed it.

## Endpoints

## Books

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
* the book is available
* the member is active
* the member has less than 3 borrowed books

If all checks are valid, the book becomes not available.

When a member returns a book, the system checks that the same member really borrowed this book.

## Logging

Logs are saved in:

app/logs/app.log


Log format:


time | level | message

Example:

2026-06-07 10:30:12 | INFO | POST /books called
2026-06-07 10:30:13 | ERROR | Book not found: 42


## How to Run

Install packages:


pip install -r requirements.txt


Start MySQL container:

docker start library-mysql


Run the server:


uvicorn app.main:app --reload

Open Swagger:


http://127.0.0.1:8000/docs

## Project Goal

The goal of this project is to build a simple API server with FastAPI and MySQL.

The project should have clean code, clear files, logging, and all required endpoints.
