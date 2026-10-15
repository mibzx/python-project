# Project Report: Quiz Application

**Student name:** ____________________  
**Roll number:** ____________________  
**Course:** MCA III Semester — Python Programming

## 1. Abstract
The Quiz Application presents multiple-choice questions from a category-based question bank. It randomises questions, measures response time, applies positive and negative marks, and saves a leaderboard.

## 2. Objectives
- Select random questions from a JSON file.
- Support categories.
- Apply a time target and marking scheme.
- Persist and display leaderboard scores.

## 3. Tools and concepts
Python, JSON, random sampling, sets, lists, dictionaries, loops, functions, sorting, and monotonic time measurement.

## 4. Algorithm
1. Load the question bank or create starter questions.
2. Display available categories.
3. Filter questions based on the user's category.
4. Randomly choose up to five questions.
5. Measure time around each answer.
6. Add 4 points for a correct answer, subtract 1 for a wrong valid option, and award 0 for invalid/late answers.
7. Save and sort leaderboard entries.

## 5. Testing
Try each category, ALL, a category that does not exist, correct answers, wrong answers, invalid letters, and slow answers. Restart and verify the leaderboard remains saved.

## 6. Limitations
The standard terminal input cannot reliably be forcibly interrupted by a timer, so the app checks elapsed time after the answer. The starter question bank is intentionally small.

## 7. Conclusion
The project demonstrates random selection, file-based storage, timing, scoring, and ranking.
