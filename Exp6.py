# Creating a dictionary of student records
student_records = {
    64: {"name": "Akshat", "grade": "A"},
    68: {"name": "Ujjwal", "grade": "B"},
    84: {"name": "Rakshit", "grade": "A"},
    1: {"name": "Gaurang", "grade": "B"},
    20: {"name": "ABXY", "grade": "A"}
}

# Searching for a student record by roll number
roll_number_to_search = int(input("Enter Rollno. of the student to be searched: "))

student = student_records.get(roll_number_to_search)

if student:
    print("Student Found:")
    print(f"Name: {student['name']}")
    print(f"Roll Number: {roll_number_to_search}")
    print(f"Grade: {student['grade']}")
else:
    print("Student not found.")
