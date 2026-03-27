"""
csv_writer.py — Writing and Reading CSV Files
Chapter 12: File Handling

Demonstrates:
- Writing a CSV file with a header row
- .writelines() vs .write()
- Reading back line by line with a for loop
- .strip() to remove trailing newlines when reading
- Combining file handling with user input
"""

OUTPUT_FILE = 'students.csv'

# --- Write student records ---
print('--- Enter 3 Student Records ---')

with open(OUTPUT_FILE, 'w') as f:
    # Write the header row first
    f.write('name,grade,city\n')

    for i in range(1, 4):
        print(f'\nStudent {i}:')
        name = input('  Name: ')
        grade = input('  Grade (0-100): ')
        city = input('  City: ')

        # Each row is one line in the CSV
        f.write(f'{name},{grade},{city}\n')

print(f'\nSaved to {OUTPUT_FILE} ✅')

# --- Read back the file ---
print('\n--- Student Records ---')

with open(OUTPUT_FILE, 'r') as f:
    for i, line in enumerate(f):
        line = line.strip()          # removes trailing \n
        if i == 0:
            # Header row — print differently
            print(f'{"NAME":<20} {"GRADE":>6}  CITY')
            print('-' * 35)
        else:
            # Data rows — unpack the CSV
            parts = line.split(',')
            if len(parts) == 3:
                name, grade, city = parts
                print(f'{name:<20} {grade:>6}  {city}')

# --- Example output:
# NAME                  GRADE  CITY
# -----------------------------------
# Valentina                95  Bogotá
# Lucas                    82  São Paulo
# Camila                   88  Lima
