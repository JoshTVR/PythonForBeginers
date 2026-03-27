"""
dry.py — Built-in Functions Demo
Chapter 7: Functions

DRY = Don't Repeat Yourself.
Python has 68 built-in functions that come with the interpreter —
no import needed. This script explores a handful of them.
"""

# len() — returns the number of items in a sequence (list, string, tuple, etc.)
languages = ['Python', 'JavaScript', 'Go', 'Rust', 'TypeScript']
print(len(languages))           # Output: 5
print(len('Hello World'))       # Output: 11  (counts spaces too)

# max() — returns the largest value in a sequence
scores = [88, 42, 97, 61, 75, 100, 53]
print(max(scores))              # Output: 100

# min() — returns the smallest value
print(min(scores))              # Output: 42

# round() — rounds a number to n decimal places
pi = 3.14159265358979
print(round(pi))                # Output: 3      (rounds to nearest int)
print(round(pi, 2))             # Output: 3.14
print(round(pi, 4))             # Output: 3.1416

# abs() — returns the absolute value (always positive)
debt = -450.75
temperature_drop = -12

print(abs(debt))                # Output: 450.75
print(abs(temperature_drop))    # Output: 12

# sum() — adds up all items in a list
weekly_sales = [1500, 2300, 980, 3100, 2750]
print(sum(weekly_sales))        # Output: 10630

# sorted() — returns a NEW sorted list, original unchanged
names = ['Valentina', 'Josh', 'Mateo', 'Isabella']
sorted_names = sorted(names)

print(sorted_names)             # Output: ['Isabella', 'Josh', 'Mateo', 'Valentina']
print(names)                    # Output: ['Valentina', 'Josh', 'Mateo', 'Isabella'] — unchanged!

# type() — returns the data type of any value
print(type(42))                 # Output: <class 'int'>
print(type(3.14))               # Output: <class 'float'>
print(type('hola'))             # Output: <class 'str'>
print(type(True))               # Output: <class 'bool'>
print(type([1, 2, 3]))          # Output: <class 'list'>