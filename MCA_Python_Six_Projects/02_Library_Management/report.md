# Project Report: Library Management System

**Student name:** ____________________  
**Roll number:** ____________________  
**Course:** MCA III Semester — Python Programming

## 1. Abstract
This application manages a small library catalogue and book issue/return records. JSON is used to preserve data between program runs, while Python's `datetime` tools support due dates and late fine calculation.

## 2. Problem statement
A library needs a clear way to know which books are available, who borrowed a book, when it is due, and whether a late fine applies.

## 3. Objectives
- Maintain book records.
- Search books by title or author.
- Issue and return books.
- Calculate late days and fines.
- Back up and restore saved data.

## 4. Tools and concepts
Python, JSON, lists, dictionaries, functions, sets, generator expressions, date arithmetic, and exception handling.

## 5. Algorithm
1. Load the JSON data or start with empty lists.
2. Show a menu.
3. For an issue, check that the book exists and is not already issued.
4. Set the due date to 14 days after issue date.
5. For a return, compare the return date with the due date.
6. Calculate fine as late days multiplied by the example daily rate.
7. Save changes to JSON.

## 6. Testing
Test adding duplicate IDs, searching for a title, issuing an available book, trying to issue the same book twice, returning on time, returning late (you may temporarily edit a test due date), and restoring a backup. Record actual results after testing.

## 7. Limitations
This is a single-user local application. It does not manage member IDs, concurrent access, or a database. The fine rate is an example.

## 8. Conclusion
The project demonstrates file persistence, data validation, date arithmetic, and basic library workflows.

## 9. Future scope
Add member registration, reservation queues, reports, a GUI, and database support.
