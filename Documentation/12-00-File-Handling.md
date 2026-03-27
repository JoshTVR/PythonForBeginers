# File Handling

So far, when your program ends, *everything disappears*. Variables, data, user input — all gone. 💨

Files let us save things permanently. This is how real applications work — user profiles, settings, game saves, logs. Everything is ultimately stored somewhere on disk.

---

# Opening Files: `open()`

The `open()` function creates a connection between your Python program and a file. It takes two main arguments: the file path and the **mode**:

| Mode | Meaning |
|------|---------|
| `'r'` | Read — opens an existing file for reading |
| `'w'` | Write — creates a new file (or **overwrites** an existing one) |
| `'a'` | Append — adds to the end of an existing file |
| `'x'` | Create — creates a new file, fails if it already exists |

---

# The `with` Statement

The modern way to work with files is the `with` statement. It automatically closes the file when you're done — even if an error occurs:

```py
with open('hello.txt', 'w') as f:
    f.write('Hola desde Python! 🐍')
```

The `as f` part gives you a variable to work with inside the block. When the block ends, the file closes automatically.

> [!TIP]
> Always use `with open(...)` instead of just `open()`. If you forget to call `.close()` on a file opened the old way, you can corrupt it or lock it from other programs.

---

# Writing Files

`.write()` writes a string to the file:

```py
with open('journal.txt', 'w') as f:
    f.write('March 27, 2026\n')
    f.write('Today I finally understood file handling.\n')
    f.write('Small win! 🎉\n')
```

The `\n` is a newline character — it moves to the next line. Without it, everything runs together.

To write multiple lines at once from a list:

```py
lines = ['line 1\n', 'line 2\n', 'line 3\n']

with open('output.txt', 'w') as f:
    f.writelines(lines)
```

---

# Appending to Files

Use `'a'` mode to add content without overwriting:

```py
with open('journal.txt', 'a') as f:
    f.write('\nMarch 28, 2026\n')
    f.write('Wrote another entry. Getting the hang of this.\n')
```

If the file doesn't exist, `'a'` creates it. If it does exist, it adds to the end.

---

# Reading Files

Three ways to read:

**`.read()`** — reads the entire file as one big string:

```py
with open('journal.txt', 'r') as f:
    content = f.read()
    print(content)
```

**`.readlines()`** — reads into a list, one line per item:

```py
with open('journal.txt', 'r') as f:
    lines = f.readlines()
    print(lines[0])    # first line
```

**Iterating line by line** — most memory-efficient for big files:

```py
with open('journal.txt', 'r') as f:
    for line in f:
        print(line.strip())    # strip() removes the trailing \n
```

---

# File + Error Handling

Combine Chapters 11 and 12 — what if the file doesn't exist?

```py
try:
    with open('data.txt', 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print('File not found! Check the path.')
```

---

## Instructions

Build a simple journal app. 📓

Create a `journal.py` program that:

1. Shows the user all previous entries (read from `journal.txt` if it exists)
2. Asks the user to type a new entry
3. Saves the entry to `journal.txt` with today's date, using append mode
4. Confirms the entry was saved

Use `FileNotFoundError` handling so it doesn't crash if the journal file doesn't exist yet.

## Solved Exercise:

```py
# journal.py

import datetime

journal_file = 'journal.txt'

# Show previous entries
print('--- Previous Entries ---')
try:
    with open(journal_file, 'r') as f:
        content = f.read()
        if content:
            print(content)
        else:
            print('(No entries yet)')
except FileNotFoundError:
    print('(No journal file yet — starting fresh!)')

# Write new entry
entry = input('\nNew entry: ')
today = datetime.date.today()

with open(journal_file, 'a') as f:
    f.write(f'\n{today}\n')
    f.write(f'{entry}\n')
    f.write('---\n')

print('Entry saved! ✅')

# Example output (first run):
# --- Previous Entries ---
# (No journal file yet — starting fresh!)
# New entry: Learned file handling today!
# Entry saved! ✅
```

<!-- TODO: add screenshot of journal.txt open in VS Code -->

---

## Instructions 2

Create a `csv_writer.py` program that:

1. Asks the user for 3 student records (name, grade)
2. Writes them to a `students.csv` file in CSV format
3. Reads the file back and prints all entries

## Solved Exercise:

```py
# csv_writer.py

# Write
with open('students.csv', 'w') as f:
    f.write('name,grade\n')
    for _ in range(3):
        name = input('Student name: ')
        grade = input('Grade: ')
        f.write(f'{name},{grade}\n')

# Read back
print('\n--- Student Records ---')
with open('students.csv', 'r') as f:
    for line in f:
        print(line.strip())
```

---

# Recap

- `open(file, mode)` opens a file. Always use `with` so it closes automatically.
- Modes: `'r'` read, `'w'` write (overwrites!), `'a'` append, `'x'` create new.
- Write: `.write(string)` — don't forget `\n` for newlines.
- Read: `.read()` (whole file), `.readlines()` (list of lines), or loop line by line.
- Combine with `try/except FileNotFoundError` for safe file access.
- Paths are relative to where you run the script from.

Next: **Chapter 13 — OOP and Classes**. Final boss. 🏗️
