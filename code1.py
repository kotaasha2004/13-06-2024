# Number of students
n = int(input())

# Initialize the list to store student data
students = []

# Read student names and grades
for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

# Find the second lowest grade
grades = sorted({student[1] for student in students})
second_lowest_grade = grades[1]

# Find all students with the second lowest grade
second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

# Sort the names alphabetically
second_lowest_students.sort()

# Print each student's name on a new line
for student in second_lowest_students:
    print(student)
