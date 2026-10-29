import json
import os
from datetime import datetime

class Student:
    """
    A class to represent a student in the management system.
    
    Attributes:
        student_id (str): Unique identifier for the student
        name (str): Full name of the student
        grade (str): Academic grade/year of the student
    """
    
    def __init__(self, student_id, name, grade):
        """
        Initialize a new Student object.
        
        Args:
            student_id (str): Unique identifier for the student
            name (str): Full name of the student
            grade (str): Academic grade/year of the student
        """
        self.student_id = student_id
        self.name = name
        self.grade = grade
    
    def to_dict(self):
        """
        Convert student object to dictionary (for JSON serialization).
        
        Returns:
            dict: Dictionary representation of the student
        """
        return {
            'student_id': self.student_id,
            'name': self.name,
            'grade': self.grade
        }
    
    def __str__(self):
        """
        String representation of the student for display purposes.
        
        Returns:
            str: Formatted string of student details
        """
        return f"ID: {self.student_id} | Name: {self.name} | Grade: {self.grade}"

class StudentManager:
    """
    A class to manage all student-related operations.
    
    This class handles adding, updating, deleting, viewing, and searching students.
    It also manages loading and saving student data to a JSON file.
    
    Attributes:
        filename (str): Name of the JSON file to store student records
        students (list): List to store Student objects
    """
    
    def __init__(self, filename='students.json'):
        """
        Initialize the StudentManager and load existing student records.
        
        Args:
            filename (str): Name of the JSON file (default: 'students.json')
        """
        self.filename = filename
        self.students = []
        self.load_students()
    
    def load_students(self):
        """
        Load student records from the JSON file.
        
        If the file doesn't exist, it will be created when students are saved.
        Handles FileNotFoundError gracefully.
        """
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    data = json.load(file)
                    # Convert dictionaries from JSON back to Student objects
                    self.students = [
                        Student(student['student_id'], student['name'], student['grade'])
                        for student in data
                    ]
                print(f"✓ Loaded {len(self.students)} existing student(s).\n")
            else:
                print(f"✓ No existing records found. Starting fresh.\n")
                self.students = []
        except FileNotFoundError:
            print(f"✗ Error: File '{self.filename}' not found. Starting fresh.\n")
            self.students = []
        except json.JSONDecodeError:
            print(f"✗ Error: Corrupted JSON file. Starting fresh.\n")
            self.students = []
    
    def save_students(self):
        """
        Save all student records to the JSON file.
        
        Converts Student objects to dictionaries and writes them to the file.
        """
        try:
            with open(self.filename, 'w') as file:
                data = [student.to_dict() for student in self.students]
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"✗ Error saving to file: {e}\n")
    
    def student_id_exists(self, student_id):
        """
        Check if a student ID already exists in the system.
        
        Args:
            student_id (str): The student ID to check
        
        Returns:
            bool: True if ID exists, False otherwise
        """
        return any(student.student_id == student_id for student in self.students)
    
    def add_student(self, student_id, name, grade):
        """
        Add a new student to the system.
        
        Validates that the student ID is unique before adding.
        
        Args:
            student_id (str): Unique identifier for the student
            name (str): Full name of the student
            grade (str): Academic grade/year of the student
        
        Returns:
            bool: True if student was added successfully, False otherwise
        """
        # Check if student ID already exists (validation for unique ID)
        if self.student_id_exists(student_id):
            print(f"✗ Error: Student ID '{student_id}' already exists!\n")
            return False
        
        # Create new student and add to list
        student = Student(student_id, name, grade)
        self.students.append(student)
        self.save_students()
        print(f"✓ Student '{name}' added successfully with ID '{student_id}'.\n")
        return True
    
    def view_all_students(self):
        """
        Display all students in a formatted table.
        
        Shows all student records in a clean, readable format with borders.
        """
        if not self.students:
            print("✗ No students found in the system.\n")
            return
        
        # Display students in a formatted table
        print("\n" + "=" * 65)
        print(f"{'Student ID':<15} {'Name':<25} {'Grade':<15}")
        print("=" * 65)
        
        for student in self.students:
            print(f"{student.student_id:<15} {student.name:<25} {student.grade:<15}")
        
        print("=" * 65)
        print(f"Total Students: {len(self.students)}\n")
    
    def search_student_by_id(self, student_id):
        """
        Search for a student by their ID.
        
        Args:
            student_id (str): The student ID to search for
        
        Returns:
            Student: The Student object if found, None otherwise
        """
        # Loop through all students and return matching student
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def update_student(self, student_id, new_name=None, new_grade=None):
        """
        Update a student's information.
        
        Args:
            student_id (str): The student ID to update
            new_name (str): New name for the student (optional)
            new_grade (str): New grade for the student (optional)
        
        Returns:
            bool: True if student was updated, False otherwise
        """
        # Find the student with the given ID
        student = self.search_student_by_id(student_id)
        
        if student is None:
            print(f"✗ Error: Student with ID '{student_id}' not found!\n")
            return False
        
        # Update only provided fields
        if new_name:
            student.name = new_name
        if new_grade:
            student.grade = new_grade
        
        self.save_students()
        print(f"✓ Student '{student_id}' updated successfully.\n")
        return True
    
    def delete_student(self, student_id):
        """
        Delete a student from the system.
        
        Args:
            student_id (str): The student ID to delete
        
        Returns:
            bool: True if student was deleted, False otherwise
        """
        # Find the student with the given ID
        student = self.search_student_by_id(student_id)
        
        if student is None:
            print(f"✗ Error: Student with ID '{student_id}' not found!\n")
            return False
        
        # Remove student from list and save
        self.students.remove(student)
        self.save_students()
        print(f"✓ Student '{student_id}' deleted successfully.\n")
        return True


# ============================================================================
# MAIN APPLICATION CLASS - Handles the CLI menu
# ============================================================================

class StudentManagementApp:
    """
    Main application class that handles the CLI menu and user interactions.
    
    This class provides the user interface and handles all menu operations.
    """
    
    def __init__(self):
        """Initialize the application with a StudentManager instance."""
        self.manager = StudentManager()
    
    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "=" * 45)
        print("===== STUDENT MANAGEMENT SYSTEM =====")
        print("=" * 45)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("=" * 45)
    
    def handle_add_student(self):
        """Handle the process of adding a new student."""
        print("\n--- Add New Student ---")
        student_id = input("Enter Student ID: ").strip()
        
        # Validate student ID is not empty
        if not student_id:
            print("✗ Error: Student ID cannot be empty!\n")
            return
        
        name = input("Enter Student Name: ").strip()
        
        # Validate name is not empty
        if not name:
            print("✗ Error: Student name cannot be empty!\n")
            return
        
        grade = input("Enter Student Grade: ").strip()
        
        # Validate grade is not empty
        if not grade:
            print("✗ Error: Student grade cannot be empty!\n")
            return
        
        # Call manager to add student
        self.manager.add_student(student_id, name, grade)
    
    def handle_search_student(self):
        """Handle the process of searching for a student."""
        print("\n--- Search Student ---")
        student_id = input("Enter Student ID to search: ").strip()
        
        if not student_id:
            print("✗ Error: Student ID cannot be empty!\n")
            return
        
        # Search for student
        student = self.manager.search_student_by_id(student_id)
        
        if student:
            print("\n" + "=" * 65)
            print("Student Found:")
            print("=" * 65)
            print(student)
            print("=" * 65 + "\n")
        else:
            print(f"✗ Error: Student with ID '{student_id}' not found!\n")
    
    def handle_update_student(self):
        """Handle the process of updating a student's information."""
        print("\n--- Update Student ---")
        student_id = input("Enter Student ID to update: ").strip()
        
        if not student_id:
            print("✗ Error: Student ID cannot be empty!\n")
            return
        
        # Check if student exists
        if not self.manager.search_student_by_id(student_id):
            print(f"✗ Error: Student with ID '{student_id}' not found!\n")
            return
        
        print("(Leave blank to keep current value)")
        new_name = input("Enter new name (or press Enter to skip): ").strip()
        new_grade = input("Enter new grade (or press Enter to skip): ").strip()
        
        # Only update if at least one field is provided
        if not new_name and not new_grade:
            print("✗ Error: Please enter at least one field to update!\n")
            return
        
        # Call manager to update student
        self.manager.update_student(student_id, new_name or None, new_grade or None)
    
    def handle_delete_student(self):
        """Handle the process of deleting a student."""
        print("\n--- Delete Student ---")
        student_id = input("Enter Student ID to delete: ").strip()
        
        if not student_id:
            print("✗ Error: Student ID cannot be empty!\n")
            return
        
        # Confirm deletion before proceeding
        confirm = input(f"Are you sure you want to delete student '{student_id}'? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            self.manager.delete_student(student_id)
        else:
            print("✗ Deletion cancelled.\n")
    
    def run(self):
        """Main application loop - handles all user interactions."""
        # Display welcome message
        print("\n╔════════════════════════════════════════════════╗")
        print("║   WELCOME TO STUDENT MANAGEMENT SYSTEM        ║")
        print("╚════════════════════════════════════════════════╝")
        
        # Main loop - keeps running until user chooses to exit
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ").strip()
            
            # Handle menu choices using if-elif-else
            if choice == '1':
                self.handle_add_student()
            elif choice == '2':
                self.manager.view_all_students()
            elif choice == '3':
                self.handle_search_student()
            elif choice == '4':
                self.handle_update_student()
            elif choice == '5':
                self.handle_delete_student()
            elif choice == '6':
                print("\n✓ Thank you for using Student Management System!")
                print("Goodbye!\n")
                break
            else:
                print("✗ Error: Invalid choice! Please enter a number between 1 and 6.\n")


# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    # Create an instance of the application and run it
    app = StudentManagementApp()
    app.run()
