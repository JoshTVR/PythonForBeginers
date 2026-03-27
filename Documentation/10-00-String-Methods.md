# String Methods

Strings might seem simple — just text — but Python gives them a full toolkit of built-in methods. 🦸 You can transform, search, split, join, and validate strings without any extra libraries.

And here's something useful to know: **strings are sequences**, just like lists. That means indexing and slicing work exactly the same way:

```py
name = 'Python'

print(name[0])      # Output: P
print(name[-1])     # Output: n
print(name[1:4])    # Output: yth
```

---

# Case Methods

Transform the case of a string:

```py
username = '  jOsH_cOdEs  '

print(username.upper())        # Output:   JOSH_CODES
print(username.lower())        # Output:   josh_codes
print(username.title())        # Output:   Josh_Codes
print(username.capitalize())   # Output:   josh_codes  (only first char capitalized)
```

Super useful for normalizing user input — if someone types "BOGOTÁ" and you need "bogotá" for a database comparison, `.lower()` handles it instantly.

---

# Trimming Whitespace

When you read input from users or files, there's often invisible whitespace lurking at the edges. 👻

```py
messy = '   hello world   '

print(messy.strip())     # Output: 'hello world'   (both sides)
print(messy.lstrip())    # Output: 'hello world   '  (left only)
print(messy.rstrip())    # Output: '   hello world'  (right only)
```

`.strip()` is one of those methods you'll use constantly when processing real-world data.

---

# Searching and Replacing

## `.find()`

Returns the index of the first occurrence. Returns `-1` if not found (doesn't crash):

```py
sentence = 'I love coding in Python'

print(sentence.find('Python'))    # Output: 18
print(sentence.find('Java'))      # Output: -1
```

## `.replace()`

Replaces all occurrences of a substring:

```py
text = 'I love coffee. Coffee is life.'

print(text.replace('coffee', 'mate'))
print(text.replace('Coffee', 'Tinto'))

# Output:
# I love mate. Coffee is life.
# I love coffee. Tinto is life.
```

Note: `.replace()` is case-sensitive. `'coffee'` and `'Coffee'` are different.

## `.count()`

Counts how many times a substring appears:

```py
message = 'banana'
print(message.count('a'))    # Output: 3
```

---

# Splitting and Joining

These two are incredibly useful for processing structured text.

## `.split()`

Splits a string into a **list** by a delimiter:

```py
csv_row = 'Josh,20,Engineering,Bogotá'
fields = csv_row.split(',')
print(fields)

# Output: ['Josh', '20', 'Engineering', 'Bogotá']
```

Without an argument, `.split()` splits on any whitespace:

```py
sentence = 'The quick brown fox'
words = sentence.split()
print(words)

# Output: ['The', 'quick', 'brown', 'fox']
```

## `.join()`

The opposite of `.split()` — joins a **list** into a string with a separator:

```py
cities = ['Bogotá', 'Medellín', 'Cali', 'Barranquilla']

print(', '.join(cities))
print(' | '.join(cities))
print(''.join(cities))

# Output:
# Bogotá, Medellín, Cali, Barranquilla
# Bogotá | Medellín | Cali | Barranquilla
# BogotáMedellínCaliBarranquilla
```

The string before `.join()` is the separator that goes between each item.

---

# Checking String Contents

These return `True` or `False`:

```py
print('42'.isdigit())        # Output: True   (all digits)
print('hello'.isalpha())     # Output: True   (all letters)
print('hello42'.isalnum())   # Output: True   (letters and digits)
print('   '.isspace())       # Output: True   (all whitespace)

print('filename.py'.endswith('.py'))     # Output: True
print('https://'.startswith('https'))   # Output: True
```

---

## Instructions

Create a `username_sanitizer.py` program that:

1. Asks the user to enter a display name
2. Strips leading/trailing whitespace
3. Converts it to lowercase
4. Replaces any spaces with underscores
5. Prints the sanitized username

Example: `'  Josh Codes  '` → `'josh_codes'`

## Solved Exercise:

```py
# username_sanitizer.py

raw_name = input('Enter your display name: ')

username = raw_name.strip().lower().replace(' ', '_')

print(f'Your username: @{username}')

# Example: '  Josh Codes  '
# Output: Your username: @josh_codes
```

> [!TIP]
> Chaining methods — `raw.strip().lower().replace()` — is totally valid Python. Each method returns a new string that the next method acts on. Read it left to right.

---

## Instructions 2

Create a `csv_parser.py` program that:

1. Has a string representing a row of CSV data: `'Bogotá,Colombia,4.7110,-74.0721'`
2. Splits it into a list
3. Prints each field on its own line, labeled

## Solved Exercise:

```py
# csv_parser.py

row = 'Bogotá,Colombia,4.7110,-74.0721'
fields = row.split(',')

labels = ['City', 'Country', 'Latitude', 'Longitude']

for label, value in zip(labels, fields):
    print(f'{label}: {value}')

# Output:
# City: Bogotá
# Country: Colombia
# Latitude: 4.7110
# Longitude: -74.0721
```

---

# Quick Reference

| Method | What it does |
|--------|-------------|
| `.upper()` | All uppercase |
| `.lower()` | All lowercase |
| `.title()` | Title Case |
| `.strip()` | Remove whitespace from both ends |
| `.find(x)` | Index of first `x`, or `-1` |
| `.replace(old, new)` | Replace all occurrences |
| `.count(x)` | Count occurrences of `x` |
| `.split(sep)` | Split into list by separator |
| `sep.join(list)` | Join list into string |
| `.startswith(x)` | Starts with `x`? |
| `.endswith(x)` | Ends with `x`? |
| `.isdigit()` | All digits? |
| `.isalpha()` | All letters? |

---

# Recap

- Strings are sequences — indexing and slicing work the same as lists.
- Case: `.upper()`, `.lower()`, `.title()`, `.capitalize()`
- Whitespace: `.strip()`, `.lstrip()`, `.rstrip()`
- Search: `.find()`, `.count()`
- Modify: `.replace()`
- Split/Join: `.split()` breaks into a list, `sep.join()` joins a list back
- Validation: `.isdigit()`, `.isalpha()`, `.startswith()`, `.endswith()`

Next: **Chapter 11 — Error Handling**. Your programs will break. Here's how to handle it gracefully. 🛡️
