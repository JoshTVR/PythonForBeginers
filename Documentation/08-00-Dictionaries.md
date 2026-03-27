# Dictionaries

Lists use indexes — `0`, `1`, `2`... But what if you want to label your data? Instead of asking "what's at position 0?", you want to ask "what's the price?" or "what's the username?" That's a dictionary. 📖

A dictionary stores data as **key-value pairs**. The key is the label; the value is the data.

```py
student = {
    'name': 'Josh',
    'age': 20,
    'major': 'Engineering',
    'gpa': 3.8
}
```

Compare this to the list approach:

```py
# List approach — confusing
student = ['Josh', 20, 'Engineering', 3.8]
print(student[0])    # what was index 0 again?

# Dictionary approach — readable
print(student['name'])    # Output: Josh
```

Much cleaner. Especially when your data has dozens of fields.

---

# Creating a Dictionary

Dictionaries use curly braces `{}`. Key-value pairs are separated by commas, with a colon `:` between each key and value:

```py
menu = {
    'Arepas': 8500,
    'Bandeja Paisa': 22000,
    'Sancocho': 15000,
    'Changua': 7000
}
```

Keys are usually strings, but they can be numbers or tuples too. Values can be anything — strings, numbers, lists, even other dictionaries.

---

# Accessing Values

Use the key in square brackets:

```py
print(menu['Arepas'])       # Output: 8500
print(menu['Sancocho'])     # Output: 15000
```

If the key doesn't exist, Python raises a `KeyError`. To avoid this, use `.get()` — it returns `None` (or a default you specify) instead of crashing:

```py
print(menu.get('Pizza'))           # Output: None
print(menu.get('Pizza', 'No tenemos eso 😅'))

# Output: No tenemos eso 😅
```

---

# Adding and Updating Keys

Add a new key the same way you'd assign a variable:

```py
menu['Buñuelos'] = 3500
print(menu['Buñuelos'])    # Output: 3500
```

Update an existing key the same way — just assign a new value:

```py
menu['Arepas'] = 9000    # price went up 🤷
print(menu['Arepas'])    # Output: 9000
```

---

# Deleting Keys

Two ways to remove a key:

```py
del menu['Changua']              # removes the key entirely

removed = menu.pop('Sancocho')   # removes and returns the value
print(removed)                   # Output: 15000
```

---

# Dictionary Methods

| Method | What it does |
|--------|-------------|
| `.keys()` | Returns all keys |
| `.values()` | Returns all values |
| `.items()` | Returns all key-value pairs as tuples |
| `.get(key, default)` | Returns value, or default if key missing |
| `.update(other_dict)` | Merges another dict in |
| `.pop(key)` | Removes and returns a value |
| `.clear()` | Removes everything |

```py
print(menu.keys())      # Output: dict_keys(['Arepas', 'Bandeja Paisa', 'Buñuelos'])
print(menu.values())    # Output: dict_values([9000, 22000, 3500])
```

---

# Iterating Over a Dictionary

Loop over keys:

```py
for item in menu:
    print(item)

# Output:
# Arepas
# Bandeja Paisa
# Buñuelos
```

Loop over key-value pairs with `.items()` — this is the most useful pattern:

```py
for item, price in menu.items():
    print(f'{item}: ${price} COP')

# Output:
# Arepas: $9000 COP
# Bandeja Paisa: $22000 COP
# Buñuelos: $3500 COP
```

---

# Nested Dictionaries

Dictionary values can be other dictionaries. This is how you model more complex data:

```py
contacts = {
    'Josh': {
        'phone': '310-555-0142',
        'city': 'Bogotá'
    },
    'Valentina': {
        'phone': '312-555-0198',
        'city': 'Medellín'
    }
}

print(contacts['Josh']['city'])    # Output: Bogotá
```

You'll see this pattern everywhere in APIs and JSON data from the web.

---

## Instructions

Build a coffee shop menu for a small café in Bogotá. ☕

Create a `coffee_shop.py` program that:

1. Creates a dictionary called `menu` with at least 5 items (names as keys, prices in COP as values)
2. Prints a full formatted menu using a loop and `.items()`
3. Asks the user to order 3 items
4. Calculates and prints the total in COP

## Solved Exercise:

```py
# coffee_shop.py

menu = {
    'Café Americano': 4500,
    'Cappuccino': 6000,
    'Tinto': 2500,
    'Agua de Panela': 3000,
    'Croissant': 5500
}

print('--- Menú del Día ☕ ---')
for item, price in menu.items():
    print(f'{item}: ${price:,} COP')

order = [
    input('\nPrimera orden: '),
    input('Segunda orden: '),
    input('Tercera orden: ')
]

total = sum(menu[item] for item in order if item in menu)
print(f'\nTotal: ${total:,} COP')

# Example output:
# --- Menú del Día ☕ ---
# Café Americano: $4,500 COP
# Cappuccino: $6,000 COP
# Tinto: $2,500 COP
# Agua de Panela: $3,000 COP
# Croissant: $5,500 COP
# Total: $14,500 COP
```

> [!TIP]
> The `{price:,}` format in f-strings adds thousands separators — `4500` becomes `4,500`. Looks way cleaner for prices.

---

# Recap

- Dictionaries store key-value pairs: `{'key': value}`.
- Access values with `dict['key']` or safely with `.get('key')`.
- Add/update: `dict['key'] = value`
- Delete: `del dict['key']` or `dict.pop('key')`
- Iterate with `for key, value in dict.items()`
- Values can be any data type — including other dictionaries.
- Dictionaries are unordered in older Python, but maintain insertion order in Python 3.7+.

Next: **Chapter 8.1 — Dictionaries Summary** + final project. 🗂️
