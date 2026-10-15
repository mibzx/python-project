"""Category-based quiz with random questions, timer, negative marking, leaderboard."""

import json
import os
import random
import time

QUESTIONS_FILE = "questions.json"
LEADERBOARD_FILE = "leaderboard.json"
TIME_LIMIT_SECONDS = 15
CORRECT_POINTS = 4
WRONG_PENALTY = 1


def load_json(path, default):
    """Load JSON data or return a default value when no file exists."""
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError):
        print(f"Warning: could not load {path}; using default data.")
        return default


def save_json(path, data):
    """Save data to JSON."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def default_questions():
    """Provide a small question bank for first-time use."""
    return [
        {"category": "Python", "question": "Which keyword defines a function?",
         "options": ["A. func", "B. def", "C. function", "D. make"], "answer": "B"},
        {"category": "Python", "question": "Which type stores key-value pairs?",
         "options": ["A. list", "B. tuple", "C. dictionary", "D. string"], "answer": "C"},
        {"category": "Computers", "question": "What does CPU stand for?",
         "options": ["A. Central Processing Unit", "B. Computer Power Utility",
                     "C. Central Program User", "D. Control Print Unit"], "answer": "A"},
        {"category": "Computers", "question": "Which is an output device?",
         "options": ["A. Keyboard", "B. Mouse", "C. Scanner", "D. Monitor"], "answer": "D"},
        {"category": "Python", "question": "What is the result of 3 ** 2?",
         "options": ["A. 6", "B. 9", "C. 8", "D. 5"], "answer": "B"},
        {"category": "Computers", "question": "Binary digits are called:",
         "options": ["A. bytes", "B. pixels", "C. bits", "D. files"], "answer": "C"}
    ]


def play_quiz():
    """Run a quiz round and return the player's name and score."""
    questions = load_json(QUESTIONS_FILE, default_questions())
    # Save the starter question bank on first run so students can edit it.
    if not os.path.exists(QUESTIONS_FILE):
        save_json(QUESTIONS_FILE, questions)
    categories = sorted({q["category"] for q in questions})
    print("Categories:", ", ".join(categories))
    category = input("Choose category (or ALL): ").strip()
    selected = [q for q in questions
                if category.upper() == "ALL" or q["category"].lower() == category.lower()]
    if not selected:
        print("No questions found for that category.")
        return None
    name = input("Player name: ").strip() or "Guest"
    number = min(5, len(selected))
    round_questions = random.sample(selected, number)  # Random selection without duplicates.
    score = 0
    for index, question in enumerate(round_questions, start=1):
        print(f"\nQuestion {index}/{number}: {question['question']}")
        for option in question["options"]:
            print(option)
        print(f"You have {TIME_LIMIT_SECONDS} seconds.")
        start = time.monotonic()
        answer = input("Answer (A/B/C/D): ").strip().upper()
        elapsed = time.monotonic() - start
        if elapsed > TIME_LIMIT_SECONDS:
            print("Time limit exceeded. No points awarded.")
        elif answer == question["answer"]:
            score += CORRECT_POINTS
            print("Correct! +4")
        elif answer in {"A", "B", "C", "D"}:
            score -= WRONG_PENALTY
            print("Incorrect. -1")
        else:
            print("Invalid/blank answer. No points awarded.")
        print(f"Time used: {elapsed:.1f} seconds")
    leaderboard = load_json(LEADERBOARD_FILE, [])
    leaderboard.append({"name": name, "score": score, "category": category})
    leaderboard.sort(key=lambda row: row["score"], reverse=True)
    save_json(LEADERBOARD_FILE, leaderboard)
    print(f"\n{name}, your final score is {score}.")
    print("\nLeaderboard:")
    for rank, row in enumerate(leaderboard[:10], start=1):
        print(f"{rank}. {row['name']} — {row['score']} ({row['category']})")
    return name, score


def main():
    """Main entry point."""
    while True:
        print("\n=== Quiz Application ===\n1 Start quiz\n2 View leaderboard\n0 Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            play_quiz()
        elif choice == "2":
            board = load_json(LEADERBOARD_FILE, [])
            for rank, row in enumerate(board[:10], start=1):
                print(f"{rank}. {row['name']} — {row['score']} ({row['category']})")
            if not board:
                print("Leaderboard is empty.")
        elif choice == "0":
            break
        else:
            print("Choose a valid option.")


if __name__ == "__main__":
    main()
