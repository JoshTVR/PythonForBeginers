"""
phonebook.py — Dictionary Project
Chapter 8: Dictionaries

Demonstrates:
- Building a dictionary from user data
- Searching by key with .get()
- Adding new entries
- Deleting entries with del and checking membership with 'in'
- Iterating to display all records
"""

# --- Starting phonebook ---
phonebook = {
    'Josh': '+57 310 555 0142',
    'Valentina': '+57 312 555 0198',
    'Mateo': '+51 991 555 0234',
    'Isabella': '+55 11 555 0312',
    'Sebastián': '+57 315 555 0089'
}

print('📞 PHONEBOOK')
print('=' * 30)

# --- Search ---
search = input('Search for a contact: ')
result = phonebook.get(search)

if result:
    print(f'{search}: {result}')
else:
    print('Contact not found.')

# --- Add a new contact ---
print()
new_name = input('Add new contact — Name: ')
new_number = input('Phone number: ')
phonebook[new_name] = new_number
print(f'{new_name} added! ✅')

# --- Delete a contact ---
print()
to_delete = input('Delete a contact — Name: ')
if to_delete in phonebook:
    del phonebook[to_delete]
    print(f'{to_delete} deleted.')
else:
    print(f'{to_delete} not found in phonebook.')

# --- Print final phonebook ---
print('\n--- Updated Phonebook ---')
for name, number in phonebook.items():
    print(f'{name:<15} {number}')
