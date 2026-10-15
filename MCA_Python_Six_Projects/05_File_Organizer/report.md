# Project Report: File Organizer Tool

**Student name:** ____________________  
**Roll number:** ____________________  
**Course:** MCA III Semester — Python Programming

## 1. Abstract
The File Organizer sorts files into folders based on extensions. It avoids overwriting existing names, records moved files, and can undo the most recent batch using a log.

## 2. Objectives
- Categorise common file types automatically.
- Handle name conflicts safely.
- Log original and destination paths.
- Provide an undo option.
- Handle filesystem errors.

## 3. Tools and concepts
Python, `pathlib`, `shutil`, JSON, dictionaries, sets, loops, exception handling, and timestamps.

## 4. Algorithm
1. Ask the user for a folder path.
2. Verify the folder exists.
3. Take a snapshot of files directly inside it.
4. Determine each file's category from its extension.
5. Create the category folder if necessary.
6. Select a unique destination name.
7. Move the file and record its old/new path.
8. Save the operation log.
9. For undo, read the log and move files back in reverse order.

## 5. Testing
Use a disposable test folder containing a PDF, image, Python file, unknown extension, and two files with the same name in a destination category. Verify categorisation, collision handling, log creation, and undo.

## 6. Limitations
The program handles files in the selected folder's top level, not recursively. Undo can skip a file if its original location is occupied or the destination file is missing.

## 7. Conclusion
The project demonstrates filesystem operations, extension-based classification, conflict handling, logging, and reversible operations.
