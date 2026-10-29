# Student Management System - Python CLI

A beginner-friendly Python Command-Line Interface (CLI) application for managing student records using Object-Oriented Programming (OOP).

## Features

✅ **Object-Oriented Design** - Uses classes (Student and StudentManager)
✅ **Add Students** - Add new students with unique IDs
✅ **View All Students** - Display all students in a formatted table
✅ **Search Students** - Find students by their ID
✅ **Update Students** - Modify student information
✅ **Delete Students** - Remove students with confirmation
✅ **JSON File Storage** - Automatically saves and loads data
✅ **Validation** - Prevents duplicate student IDs and validates inputs
✅ **Error Handling** - Gracefully handles common errors
✅ **Beginner-Friendly** - Well-commented code with clear structure

## Project Structure

```
Student Management System sambit/
│
├── main.py                 # Main application file (all code in one file)
├── students.json          # JSON file storing student records (auto-created/updated)
└── README.md             # This file
```

## How to Run the Project

### Step 1: Open Terminal in VS Code

1. Open VS Code
2. Open the folder: `d:\Student Management System sambit`
3. Press `Ctrl + `` (backtick) to open the integrated terminal
   - Or go to **View** → **Terminal**

### Step 2: Run the Application

Type the following command in the terminal:

```bash
python main.py
```

**Alternative command (if `python` is not recognized):**

```bash
python3 main.py
```

### Step 3: Use the Menu

Once the application starts, you'll see the main menu:

```
================================================
===== STUDENT MANAGEMENT SYSTEM =====
================================================
1. Add Student
2. View All Students
3. Search Student by ID
4. Update Student
5. Delete Student
6. Exit
================================================
```

## Usage Examples

### 1. Add a Student

```
Enter your choice (1-6): 1

--- Add New Student ---
Enter Student ID: S101
Enter Student Name: John Doe
Enter Student Grade: 12th Grade

✓ Student 'John Doe' added successfully with ID 'S101'.
```

### 2. View All Students

```
Enter your choice (1-6): 2

=================================================================
Student ID      Name                      Grade
=================================================================
S001            Alice Johnson             10th Grade
S002            Bob Smith                 9th Grade
S003            Carol Williams            11th Grade
S004            David Brown               10th Grade
S005            Emma Davis                9th Grade
S101            John Doe                  12th Grade
=================================================================
Total Students: 6
```

### 3. Search Student by ID

```
Enter your choice (1-6): 3

--- Search Student ---
Enter Student ID to search: S001

=================================================================
Student Found:
=================================================================
ID: S001 | Name: Alice Johnson | Grade: 10th Grade
================================================================
```

### 4. Update Student

```
Enter your choice (1-6): 4

--- Update Student ---
Enter Student ID to update: S001
(Leave blank to keep current value)
Enter new name (or press Enter to skip): Alice J. Johnson
Enter new grade (or press Enter to skip): 11th Grade

✓ Student 'S001' updated successfully.
```

### 5. Delete Student

```
Enter your choice (1-6): 5

--- Delete Student ---
Enter Student ID to delete: S005
Are you sure you want to delete student 'S005'? (yes/no): yes

✓ Student 'S005' deleted successfully.
```

### 6. Exit

```
Enter your choice (1-6): 6

✓ Thank you for using Student Management System!
Goodbye!
```

## Code Structure

### 1. **Student Class** (Lines 7-47)
   - Represents a single student
   - Attributes: `student_id`, `name`, `grade`
   - Methods: `__init__()`, `to_dict()`, `__str__()`

### 2. **StudentManager Class** (Lines 54-189)
   - Manages all student operations
   - Key methods:
     - `load_students()` - Load data from JSON
     - `save_students()` - Save data to JSON
     - `add_student()` - Add new student
     - `view_all_students()` - Display all students
     - `search_student_by_id()` - Find student by ID
     - `update_student()` - Modify student info
     - `delete_student()` - Remove student
     - `student_id_exists()` - Validate unique ID

### 3. **StudentManagementApp Class** (Lines 196-307)
   - Handles the CLI menu and user interactions
   - Key methods:
     - `display_menu()` - Show menu options
     - `handle_add_student()` - Process add operation
     - `handle_search_student()` - Process search operation
     - `handle_update_student()` - Process update operation
     - `handle_delete_student()` - Process delete operation
     - `run()` - Main application loop

### 4. **Entry Point** (Lines 314-317)
   - Starts the application

## Key Programming Concepts Used

1. **Classes and Objects** - Student and StudentManager classes
2. **Methods and Constructors** - `__init__()`, instance methods
3. **Lists** - Store multiple students
4. **Dictionaries** - Convert objects to JSON format
5. **Loops** - For and while loops for iteration
6. **Conditional Statements** - If-elif-else for logic
7. **Functions** - Methods for modular code
8. **JSON File Handling** - `json.load()` and `json.dump()`
9. **Error Handling** - Try-except blocks for file operations
10. **String Formatting** - Clean output display

## Sample students.json

The `students.json` file stores all student records in JSON format:

```json
[
    {
        "student_id": "S001",
        "name": "Alice Johnson",
        "grade": "10th Grade"
    },
    {
        "student_id": "S002",
        "name": "Bob Smith",
        "grade": "9th Grade"
    }
]
```

**Note:** This file is created automatically when you first add a student. You can start fresh by deleting this file.

## Data Persistence

- **Automatic Loading**: When the program starts, it loads all student records from `students.json`
- **Automatic Saving**: Every time you add, update, or delete a student, the changes are immediately saved to `students.json`
- **No Manual Save**: You don't need to manually save your data!

## Validation & Error Handling

### Validation Features:
- ✓ Student IDs must be unique (no duplicates allowed)
- ✓ All fields (ID, Name, Grade) must not be empty
- ✓ Duplicate ID detection before adding

### Error Handling:
- ✓ File not found → Starts fresh with empty list
- ✓ Corrupted JSON → Starts fresh with empty list
- ✓ Invalid menu choice → Prompts user to enter valid option (1-6)
- ✓ Student not found → Shows error message with guidance
- ✓ Empty input → Validates and asks user to try again

## PEP 8 Compliance

This code follows Python's PEP 8 style guide:
- ✓ Proper indentation (4 spaces)
- ✓ Clear variable and function names
- ✓ Comments explaining each section
- ✓ Docstrings for classes and methods
- ✓ Consistent formatting and spacing

## Troubleshooting

### Issue: "Python not found" or "python: command not found"

**Solution:** Try using `python3` instead:
```bash
python3 main.py
```

### Issue: "No such file or directory: main.py"

**Solution:** Make sure you're in the correct directory:
```bash
cd "d:\Student Management System sambit"
python main.py
```

### Issue: "FileNotFoundError" when running

**Solution:** The program will create `students.json` automatically when you add your first student. This is normal!

## Learning Outcomes

By studying and using this project, you'll learn:
- How to design classes with clear responsibilities
- How to manage object collections
- How to persist data using JSON files
- How to create user-friendly CLI applications
- How to validate and handle user input
- How to write well-documented, beginner-friendly code

## Future Enhancements (Optional)

If you want to extend this project later, consider:
- Add student grades/marks tracking
- Export student list to CSV
- Search by name or grade
- Sort students by name or ID
- Add confirmation prompts before critical operations
- Create a GUI version using tkinter

---

**Happy Learning! 🚀**

This project is designed to teach Python programming fundamentals in a practical, real-world context.
