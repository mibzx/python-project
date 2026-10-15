"""Student Management System: beginner console project using CSV storage."""

import csv                 # Reads and writes CSV files.
import os                  # Checks whether the data file already exists.
from statistics import mean  # Calculates average marks.

DATA_FILE = "students.csv"  # The program stores student records in this file.
ADMIN_USERNAME = "admin"    
ADMIN_PASSWORD = "python123"  


def load_students():
    """Return all saved students as a list of dictionaries."""
    if not os.path.exists(DATA_FILE):  # A first run will not have a CSV file yet.
        return []
    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))  # Each CSV row becomes a dictionary.


def save_students(students):
    """Save the full student list to CSV."""
    fields = ["student_id", "name", "marks"]
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()  # Writes column names at the top of the file.
        writer.writerows(students)  # Writes each student's dictionary as a row.


def login():
    """Ask for demo admin credentials and return True only when correct."""
    print("=== Student Management System ===")
    username = input("Admin username: ").strip()
    password = input("Admin password: ").strip()
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login successful.")
        return True
    print("Invalid username or password.")
    return False


def add_student(students):
    """Validate and add one student."""
    student_id = input("Student ID: ").strip()
    if not student_id:
        print("ID cannot be empty.")
        return
    if any(s["student_id"] == student_id for s in students):
        print("That student ID already exists.")
        return
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    try:
        marks = float(input("Marks (0 to 100): "))
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be from 0 to 100.")
    except ValueError as error:
        print(f"Invalid marks: {error}")
        return
    students.append({"student_id": student_id, "name": name, "marks": f"{marks:.2f}"})
    save_students(students)
    print("Student added.")


def list_students(students):
    """Print all student records in a readable format."""
    if not students:
        print("No student records found.")
        return
    print("\nID | Name | Marks")
    print("-" * 35)
    for student in students:
        print(f'{student["student_id"]} | {student["name"]} | {student["marks"]}')


def search_student(students):
    """Search by exact ID or partial name."""
    query = input("Enter student ID or part of name: ").strip().lower()
    matches = [s for s in students
               if s["student_id"].lower() == query or query in s["name"].lower()]
    if matches:
        list_students(matches)
    else:
        print("No matching student found.")


def update_student(students):
    """Update a student's name and/or marks by ID."""
    student_id = input("ID to update: ").strip()
    student = next((s for s in students if s["student_id"] == student_id), None)
    if student is None:
        print("Student not found.")
        return
    new_name = input(f'New name [{student["name"]}]: ').strip()
    new_marks = input(f'New marks [{student["marks"]}]: ').strip()
    if new_name:
        student["name"] = new_name
    if new_marks:
        try:
            value = float(new_marks)
            if not 0 <= value <= 100:
                raise ValueError("Marks must be from 0 to 100.")
            student["marks"] = f"{value:.2f}"
        except ValueError as error:
            print(f"Invalid marks; update cancelled: {error}")
            return
    save_students(students)
    print("Student updated.")


def delete_student(students):
    """Delete a student after a confirmation prompt."""
    student_id = input("ID to delete: ").strip()
    student = next((s for s in students if s["student_id"] == student_id), None)
    if student is None:
        print("Student not found.")
        return
    confirm = input(f'Delete {student["name"]}? (y/n): ').strip().lower()
    if confirm == "y":
        students.remove(student)
        save_students(students)
        print("Student deleted.")
    else:
        print("Deletion cancelled.")


def sort_students(students):
    """Display records sorted by name or marks without changing saved order."""
    print("1 Sort by name  2 Sort by marks (highest first)")
    choice = input("Choose sort order: ").strip()
    if choice == "1":
        ordered = sorted(students, key=lambda s: s["name"].lower())
    elif choice == "2":
        ordered = sorted(students, key=lambda s: float(s["marks"]), reverse=True)
    else:
        print("Invalid sort option.")
        return
    list_students(ordered)


def reports(students):
    """Show topper and average marks."""
    if not students:
        print("Add students before generating a report.")
        return
    topper = max(students, key=lambda s: float(s["marks"]))
    average = mean(float(s["marks"]) for s in students)
    print(f'Topper: {topper["name"]} ({topper["marks"]} marks)')
    print(f"Average marks: {average:.2f}")


def main():
    """Program entry point: login, then repeat menu until user exits."""
    if not login():
        return
    students = load_students()
    while True:
        print("\n1 Add  2 List  3 Search  4 Update  5 Delete  6 Reports  0 Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            reports(students)
        elif choice == "7":
            sort_students(students)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Choose a valid menu number.")


if __name__ == "__main__":
    main()
