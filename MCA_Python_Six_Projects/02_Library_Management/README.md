# 2. Library Management System

## Aim
Track books, borrowers, issue/return dates, late fines, availability, and JSON backup/restore.

## Requirements
Python 3.10+; no extra packages.

## Run
`python main.py`

## Features
- Add books with unique IDs.
- Search by title or author.
- Display available and issued books.
- Issue books for 14 days and record due dates.
- Calculate late-return fine at ₹2 per day (example rule).
- Persist data in `library.json`; back up to `library_backup.json` and restore.

## Files
`main.py` is the application. `library.json` is created on first save. The backup file is created when you choose menu item 6.

## Note
The due period and fine are examples. Replace them with your college/library's actual policy if required.
