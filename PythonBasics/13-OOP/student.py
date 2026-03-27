"""
student.py — OOP Project
Chapter 13: OOP

Demonstrates:
- Multi-attribute class with a real-world model
- Methods that modify instance state
- __str__ for clean printing
- Creating multiple instances from one class
- min/max capping logic inside a method
"""

class Student:
    """Represents a university student."""

    def __init__(self, name, age, major, gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa          # float, 0.0 to 4.0 scale

    def introduce(self):
        """Print a greeting with the student's info."""
        print(f'Hi! I\'m {self.name}, {self.age} years old.')
        print(f'I study {self.major} — GPA: {self.gpa:.1f}')

    def study(self, hours):
        """
        Simulate studying. Each hour raises GPA by 0.05, capped at 4.0.
        hours: int — number of hours studied
        """
        gain = hours * 0.05
        self.gpa = min(4.0, self.gpa + gain)    # min() caps at 4.0
        print(f'{self.name} studied {hours}h → New GPA: {self.gpa:.2f}')

    def fail_exam(self):
        """Simulate failing an exam. GPA drops 0.3, minimum 0.0."""
        self.gpa = max(0.0, self.gpa - 0.3)
        print(f'{self.name} failed an exam... GPA: {self.gpa:.2f} 😬')

    def __str__(self):
        return f'{self.name} | {self.major} | GPA: {self.gpa:.2f}'


# ─────────────────────────────────────────
# CREATE STUDENTS
# ─────────────────────────────────────────

s1 = Student('Valentina', 20, 'Computer Science', 3.5)
s2 = Student('Lucas', 22, 'Data Engineering', 3.1)
s3 = Student('Camila', 19, 'Software Engineering', 3.8)

# Each student is independent
s1.introduce()
print()
s2.introduce()
print()

# Studying boosts GPA
s1.study(4)     # Output: Valentina studied 4h → New GPA: 3.70
s2.study(8)     # Output: Lucas studied 8h → New GPA: 3.50
s3.study(20)    # Output: Camila studied 20h → New GPA: 4.00  (capped)

print()

# Failing an exam drops it
s2.fail_exam()  # Output: Lucas failed an exam... GPA: 3.20 😬

print()

# __str__ in action
print(s1)   # Output: Valentina | Computer Science | GPA: 3.70
print(s2)   # Output: Lucas | Data Engineering | GPA: 3.20
print(s3)   # Output: Camila | Software Engineering | GPA: 4.00

# ─────────────────────────────────────────
# LIST OF STUDENTS (objects in a list!)
# ─────────────────────────────────────────

roster = [s1, s2, s3]

print('\n--- Class Roster ---')
for student in roster:
    print(student)

# Find the top student using max() with a key function
top = max(roster, key=lambda s: s.gpa)
print(f'\nTop student: {top.name} ({top.gpa:.2f})')
