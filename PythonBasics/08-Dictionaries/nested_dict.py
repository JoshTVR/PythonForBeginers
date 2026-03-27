"""
nested_dict.py — Nested Dictionaries
Chapter 8: Dictionaries

Demonstrates:
- Dictionaries inside dictionaries (nested)
- Accessing nested values with chained keys
- Iterating over nested structures
- Real-world example: a contacts list with multiple fields per contact
"""

# --- Nested dictionary ---
# Each contact has sub-fields (a dict as the value)

contacts = {
    'Valentina': {
        'phone': '+57 312 555 0198',
        'city': 'Medellín',
        'email': 'vale@example.com'
    },
    'Lucas': {
        'phone': '+55 11 555 0312',
        'city': 'São Paulo',
        'email': 'lucas@example.com'
    },
    'Camila': {
        'phone': '+51 991 555 0234',
        'city': 'Lima',
        'email': 'camila@example.com'
    }
}

# --- Accessing nested values ---
# First key gets the contact dict, second key gets the specific field

print(contacts['Valentina']['city'])    # Output: Medellín
print(contacts['Lucas']['email'])       # Output: lucas@example.com

# --- Iterating over nested structure ---
print('\n--- Contact List ---')
for name, info in contacts.items():
    print(f'\n{name}')
    for field, value in info.items():
        print(f'  {field}: {value}')

# Output:
# Valentina
#   phone: +57 312 555 0198
#   city: Medellín
#   email: vale@example.com
#
# Lucas
#   phone: +55 11 555 0312
#   city: São Paulo
#   email: lucas@example.com
# ...

# --- Adding a new nested entry ---
contacts['Mateo'] = {
    'phone': '+57 310 555 0099',
    'city': 'Bogotá',
    'email': 'mateo@example.com'
}

print(f'\nTotal contacts: {len(contacts)}')    # Output: Total contacts: 4

# --- Updating a nested field ---
contacts['Valentina']['city'] = 'Cartagena'   # moved cities
print(contacts['Valentina']['city'])           # Output: Cartagena
