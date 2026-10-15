"""Library Management System using JSON persistence and due-date fine calculation."""

import json
import os
from datetime import date, timedelta

DATA_FILE = "library.json"
FINE_PER_DAY = 2  # Example fine in rupees per late day; adjust to college rules.


def load_data():
    """Load book and issue records, or create empty collections on first run."""
    if not os.path.exists(DATA_FILE):
        return {"books": [], "issues": []}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not read saved data: {error}")
        return {"books": [], "issues": []}


def save_data(data):
    """Write the current collections to JSON with readable indentation."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def add_book(data):
    """Add a book with a unique book ID."""
    book_id = input("Book ID: ").strip()
    if not book_id or any(b["book_id"] == book_id for b in data["books"]):
        print("ID is blank or already exists.")
        return
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    if not title or not author:
        print("Title and author are required.")
        return
    data["books"].append({"book_id": book_id, "title": title, "author": author})
    save_data(data)
    print("Book added.")


def list_books(data):
    """Show all books and whether each is available or issued."""
    if not data["books"]:
        print("No books found.")
        return
    issued_ids = {issue["book_id"] for issue in data["issues"] if not issue["returned"]}
    for book in data["books"]:
        status = "Issued" if book["book_id"] in issued_ids else "Available"
        print(f'{book["book_id"]} | {book["title"]} | {book["author"]} | {status}')


def search_books(data):
    """Search title or author without case sensitivity."""
    query = input("Search title or author: ").strip().lower()
    matches = [b for b in data["books"]
               if query in b["title"].lower() or query in b["author"].lower()]
    if not matches:
        print("No matching books.")
    for book in matches:
        print(f'{book["book_id"]} | {book["title"]} | {book["author"]}')


def issue_book(data):
    """Issue an available book and calculate a due date."""
    book_id = input("Book ID to issue: ").strip()
    book = next((b for b in data["books"] if b["book_id"] == book_id), None)
    already_issued = any(i["book_id"] == book_id and not i["returned"] for i in data["issues"])
    if book is None:
        print("Book not found.")
        return
    if already_issued:
        print("That book is already issued.")
        return
    borrower = input("Borrower's name: ").strip()
    if not borrower:
        print("Borrower name is required.")
        return
    issue_date = date.today()
    due_date = issue_date + timedelta(days=14)
    data["issues"].append({
        "book_id": book_id, "borrower": borrower,
        "issue_date": issue_date.isoformat(), "due_date": due_date.isoformat(),
        "returned": False, "return_date": None
    })
    save_data(data)
    print(f"Issued. Due date: {due_date.isoformat()}")


def return_book(data):
    """Mark a current issue as returned and calculate any late fine."""
    book_id = input("Book ID to return: ").strip()
    issue = next((i for i in reversed(data["issues"])
                  if i["book_id"] == book_id and not i["returned"]), None)
    if issue is None:
        print("No active issue found for that book.")
        return
    return_date = date.today()
    due_date = date.fromisoformat(issue["due_date"])
    late_days = max(0, (return_date - due_date).days)
    fine = late_days * FINE_PER_DAY
    issue["returned"] = True
    issue["return_date"] = return_date.isoformat()
    save_data(data)
    print(f"Returned on {return_date.isoformat()}. Late days: {late_days}. Fine: ₹{fine}")


def backup_data():
    """Copy the JSON data file to a simple backup filename."""
    if not os.path.exists(DATA_FILE):
        print("No data file to back up yet.")
        return
    with open(DATA_FILE, "r", encoding="utf-8") as source:
        content = source.read()
    with open("library_backup.json", "w", encoding="utf-8") as target:
        target.write(content)
    print("Backup saved as library_backup.json.")


def restore_data(data):
    """Restore from the backup after confirming it is valid JSON."""
    if not os.path.exists("library_backup.json"):
        print("Backup file not found.")
        return data
    try:
        with open("library_backup.json", "r", encoding="utf-8") as file:
            restored = json.load(file)
        if "books" not in restored or "issues" not in restored:
            raise ValueError("Backup structure is invalid.")
        save_data(restored)
        print("Backup restored.")
        return restored
    except (json.JSONDecodeError, OSError, ValueError) as error:
        print(f"Restore failed: {error}")
        return data


def main():
    """Main menu loop."""
    data = load_data()
    while True:
        print("\n1 Add book  2 List books  3 Search  4 Issue  5 Return  6 Backup  7 Restore  0 Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_book(data)
        elif choice == "2":
            list_books(data)
        elif choice == "3":
            search_books(data)
        elif choice == "4":
            issue_book(data)
        elif choice == "5":
            return_book(data)
        elif choice == "6":
            backup_data()
        elif choice == "7":
            data = restore_data(data)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Choose a valid menu number.")


if __name__ == "__main__":
    main()
