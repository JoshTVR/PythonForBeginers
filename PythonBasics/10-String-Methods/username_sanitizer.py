"""
username_sanitizer.py — String Methods
Chapter 10: String Methods

Demonstrates:
- .strip() to remove leading/trailing whitespace
- .lower() to normalize case
- .replace() to swap characters
- Method chaining (calling multiple methods in sequence)
- .startswith(), .endswith(), .isalpha(), .isdigit()
"""

# --- Method chaining ---
# Each method returns a new string that the next method acts on.
# Read left to right.

raw_name = input('Enter your display name: ')

username = raw_name.strip().lower().replace(' ', '_')

print(f'Your username: @{username}')

# Examples:
# '  Josh Codes  '  →  '@josh_codes'
# '  VALENTINA 2024  ' →  '@valentina_2024'


# --- Individual string methods demo ---
sample = '  Hello From Python!  '

print(sample.upper())        # Output: '  HELLO FROM PYTHON!  '
print(sample.lower())        # Output: '  hello from python!  '
print(sample.strip())        # Output: 'Hello From Python!'
print(sample.strip().title()) # Output: 'Hello From Python!'

# --- .replace() ---
announcement = 'The event is on Saturday. Saturday is confirmed.'
print(announcement.replace('Saturday', 'Sunday'))
# Output: 'The event is on Sunday. Sunday is confirmed.'
# Replaces ALL occurrences

# --- .find() and .count() ---
sentence = 'I love coding in Python, Python is great!'

pos = sentence.find('Python')
print(f'First "Python" at index: {pos}')    # Output: 17

count = sentence.count('Python')
print(f'"Python" appears {count} times')   # Output: 2

# .find() returns -1 if not found (doesn't crash like .index() does)
print(sentence.find('Java'))               # Output: -1

# --- Checking string content ---
print('42'.isdigit())           # Output: True
print('hello'.isalpha())        # Output: True
print('hello42'.isalnum())      # Output: True
print('   '.isspace())          # Output: True

print('notes.py'.endswith('.py'))       # Output: True
print('https://x.com'.startswith('https'))  # Output: True
