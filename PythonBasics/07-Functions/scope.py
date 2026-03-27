"""
scope.py — Variable Scope
Chapter 7: Functions

Demonstrates:
- Local variables (only exist inside the function)
- Global variables (accessible everywhere)
- Why scope matters and how to avoid surprises
"""

# --- Global variable ---
# Defined outside any function — accessible from anywhere in the file
greeting = 'Hola'
counter = 0

def say_hi(name):
    # Can READ the global variable
    print(f'{greeting}, {name}! 👋')

say_hi('Valentina')     # Output: Hola, Valentina! 👋
say_hi('Mateo')         # Output: Hola, Mateo! 👋


# --- Local variable ---
# Defined inside a function — ONLY exists while that function runs

def make_secret():
    secret_code = 'XJ-2048'    # local variable
    print(f'Code: {secret_code}')

make_secret()   # Output: Code: XJ-2048

# Trying to access it outside the function would crash:
# print(secret_code)    # NameError: name 'secret_code' is not defined


# --- Each function call gets its own local variables ---
# They don't share memory between calls

def greet(name):
    message = f'Welcome, {name}!'    # new 'message' created each call
    print(message)

greet('Josh')       # Output: Welcome, Josh!
greet('Isabella')   # Output: Welcome, Isabella!
# These two 'message' variables never interfere with each other


# --- Modifying a global variable with 'global' keyword ---
# Without 'global', the assignment creates a NEW local variable instead

def increment():
    global counter         # tells Python: use the global 'counter'
    counter += 1

print(counter)      # Output: 0
increment()
increment()
increment()
print(counter)      # Output: 3

# NOTE: Using 'global' is generally discouraged in real code.
# Better practice: return the new value from the function and reassign outside.

def increment_clean(n):
    return n + 1

counter = increment_clean(counter)
counter = increment_clean(counter)
print(counter)      # Output: 5
