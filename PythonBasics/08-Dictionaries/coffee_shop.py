"""
coffee_shop.py — Dictionary Basics
Chapter 8: Dictionaries

Demonstrates:
- Creating a dictionary with string keys and numeric values
- Accessing values by key
- Adding and updating keys
- Iterating over key-value pairs with .items()
- f-string formatting with thousands separators
"""

# --- Creating a dictionary ---
# Keys are strings (item names), values are ints (prices in COP)

menu = {
    'Café Americano': 4500,
    'Cappuccino': 6000,
    'Tinto': 2500,
    'Agua de Panela': 3000,
    'Croissant': 5500,
    'Buñuelo': 2000
}

# --- Accessing a value by key ---
print(menu['Tinto'])        # Output: 2500
print(menu['Cappuccino'])   # Output: 6000

# --- Safe access with .get() ---
# Returns None (or a custom default) instead of crashing on missing keys
print(menu.get('Pizza'))                        # Output: None
print(menu.get('Pizza', 'No tenemos eso 😅'))   # Output: No tenemos eso 😅

# --- Adding a new item ---
menu['Empanada'] = 1800
print(menu['Empanada'])     # Output: 1800

# --- Updating an existing item (price went up 💸) ---
menu['Cappuccino'] = 6500

# --- Print the full menu ---
print('\n--- ☕ Menú del Día ---')
for item, price in menu.items():
    print(f'{item:<20} ${price:>6,} COP')

# Output:
# --- ☕ Menú del Día ---
# Café Americano       $ 4,500 COP
# Cappuccino           $ 6,500 COP
# Tinto                $ 2,500 COP
# Agua de Panela       $ 3,000 COP
# Croissant            $ 5,500 COP
# Buñuelo              $ 2,000 COP
# Empanada             $ 1,800 COP

# --- Take an order ---
print()
order = []
print('Selecciona 3 items del menú:')
for _ in range(3):
    item = input('> ')
    if item in menu:
        order.append(item)
    else:
        print(f'"{item}" no está en el menú, lo ignoramos.')

total = sum(menu[item] for item in order)
print(f'\nPedido: {", ".join(order)}')
print(f'Total: ${total:,} COP')
