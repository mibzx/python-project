# Project Report: Student Management System

**Student name:** ____________________  
**Roll number:** ____________________  
**Course:** MCA III Semester — Python Programming  
**Institution:** ____________________  
**Submitted to:** ____________________

## 1. Abstract
The Student Management System is a menu-driven Python application for maintaining student IDs, names, and marks. It uses CSV storage so that records remain available after the program closes.

## 2. Problem statement
Maintaining student marks manually can make searching, updating, and calculating class summaries repetitive. This project demonstrates how a small program can organise those operations.

## 3. Objectives
- Perform create, read, update, and delete operations.
- Search student records by ID or name.
- Sort records by name or marks.
- Validate input and handle invalid marks.
- Store data in a CSV file.
- Report the topper and average marks.

## 4. Tools and concepts
Python, CSV files, functions, lists, dictionaries, loops, conditional statements, exception handling, and the `statistics` module.

## 5. Algorithm
1. Ask the administrator to log in.
2. Load existing rows from `students.csv`.
3. Display the menu repeatedly.
4. Run the selected function.
5. Save changes after a successful modification.
6. Calculate topper and average when requested.
7. Exit when the user chooses 0.

## 6. Testing
Test with fictional records. Check duplicate IDs, blank names, invalid text for marks, marks below 0 or above 100, searching for a missing record, deleting with confirmation, and restarting to verify persistence. Record actual results after running the program.

## 7. Limitations
The login is a demonstration only; credentials are hard-coded. CSV is appropriate for a small assignment, not concurrent multi-user access. Data validation and authentication would need strengthening for real use.

## 8. Conclusion
The project demonstrates basic record management, file persistence, modular programming, and simple statistical reporting in Python.

## 9. Future scope
Add sorting, exportable reports, stronger authentication, a database, and a graphical interface.
