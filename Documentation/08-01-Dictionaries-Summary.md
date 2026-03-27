# Dictionaries — Summary

Dictionaries are one of the most-used data structures in Python. Once you get them, you start seeing them everywhere — JSON from APIs, config files, database results. 🗂️

Full recap:

- Dictionaries store data as key-value pairs: `{'key': value}`
- Created with curly braces `{}`
- Keys are unique — duplicate keys overwrite the earlier one
- Access: `dict['key']` — raises KeyError if missing
- Safe access: `dict.get('key', default)` — returns default instead of crashing
- Add/update: `dict['key'] = value`
- Delete: `del dict['key']` or `dict.pop('key')`
- Iterate keys: `for k in dict`
- Iterate pairs: `for k, v in dict.items()`
- Nested dicts: `dict['key']['nested_key']`

---

# Cheat Sheet

| Operation | Syntax | Example |
|-----------|--------|---------|
| Create | `d = {'k': v}` | `d = {'age': 20}` |
| Access | `d['key']` | `d['age']` → `20` |
| Safe access | `d.get('key')` | `d.get('name', 'N/A')` |
| Add/update | `d['key'] = v` | `d['city'] = 'Cali'` |
| Delete | `del d['key']` | `del d['age']` |
| All keys | `d.keys()` | |
| All values | `d.values()` | |
| All pairs | `d.items()` | |
| Merge | `d.update(other)` | |
| Length | `len(d)` | |

---

## Instructions

Build a phonebook! 📞

Create a `phonebook.py` program that:

1. Creates a dictionary with 5 contacts (name → phone number)
2. Asks the user to search for a contact by name
3. Prints the phone number if found, or `"Contact not found"` if not
4. Adds a new contact that the user inputs
5. Deletes a contact that the user specifies
6. Prints the final phonebook

## Solved Exercise:

```py
# phonebook.py

phonebook = {
    'Josh': '+57 310 555 0142',
    'Valentina': '+57 312 555 0198',
    'Mateo': '+51 991 555 0234',
    'Isabella': '+55 11 555 0312',
    'Sebastián': '+57 315 555 0089'
}

# Search
search = input('Search for a contact: ')
print(phonebook.get(search, 'Contact not found'))

# Add
new_name = input('New contact name: ')
new_number = input('New contact number: ')
phonebook[new_name] = new_number

# Delete
to_delete = input('Delete contact: ')
if to_delete in phonebook:
    del phonebook[to_delete]
    print(f'{to_delete} deleted.')
else:
    print('Contact not found.')

# Print final phonebook
print('\n--- Phonebook ---')
for name, number in phonebook.items():
    print(f'{name}: {number}')
```

---

Chapter 8 — complete! 🎉 Next: **Chapter 9 — Tuples and Sets**. Two more ways to store collections of data.
