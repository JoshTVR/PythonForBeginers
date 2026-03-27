"""
journal.py — Reading and Writing Files
Chapter 12: File Handling

Demonstrates:
- open() with 'r' (read), 'w' (write), 'a' (append) modes
- The 'with' statement (auto-closes the file)
- .read() to read the whole file as a string
- .write() to write to a file
- FileNotFoundError handling (first run, no file yet)
- datetime module for timestamps
"""

import datetime

JOURNAL_FILE = 'journal.txt'

# --- Show previous entries ---
# Try to read the file — it might not exist yet on the first run

print('📓 MY JOURNAL')
print('=' * 30)
print('\n--- Previous Entries ---')

try:
    with open(JOURNAL_FILE, 'r') as f:
        content = f.read()
        if content.strip():
            print(content)
        else:
            print('(Journal is empty)')
except FileNotFoundError:
    # First time running — the file doesn't exist yet
    print('(No journal file yet — starting fresh!)')

# --- Write a new entry ---
print()
entry = input('New entry: ')

if entry.strip():  # don't save empty entries
    today = datetime.date.today()   # e.g. 2026-03-27

    with open(JOURNAL_FILE, 'a') as f:
        # 'a' = append — adds to the end without overwriting
        f.write(f'\n{today}\n')
        f.write(f'{entry}\n')
        f.write('─' * 30 + '\n')

    print('Entry saved! ✅')
else:
    print('Nothing to save.')

# --- Example flow on first run:
# --- Previous Entries ---
# (No journal file yet — starting fresh!)
#
# New entry: Today I learned how to write files in Python!
# Entry saved! ✅

# --- Example flow on second run:
# --- Previous Entries ---
# 2026-03-27
# Today I learned how to write files in Python!
# ──────────────────────────────
#
# New entry: Getting the hang of this.
# Entry saved! ✅
