# Tuples

You know lists. Lists are **mutable** — you can add, remove, and change items whenever you want. But sometimes you *don't want* something to change. Coordinates, RGB colors, dates, card suits. Enter the tuple: a list that's locked. 🔒

---

# Tuple Syntax

Tuples use **parentheses** `()` instead of square brackets:

```py
coordinates = (4.7110, -74.0721)    # Bogotá, Colombia (lat, lon)
rgb_red = (255, 0, 0)
playing_card = ('Ace', 'Spades')
```

They work exactly like lists for accessing items:

```py
print(coordinates[0])    # Output: 4.711
print(rgb_red[-1])       # Output: 0
```

But try to modify one:

```py
coordinates[0] = 10    # 💥 TypeError: 'tuple' object does not support item assignment
```

Python won't let you. That's the point — immutability is a feature, not a limitation.

---

# Why Tuples?

A few reasons to reach for a tuple instead of a list:

1. **Intentional immutability** — when the data shouldn't change (GPS coordinates, color constants, HTTP status codes)
2. **Performance** — slightly faster than lists for read-only data
3. **Dictionary keys** — lists can't be dictionary keys (they're mutable), but tuples can
4. **Multiple return values** — functions often return tuples when giving back more than one value

```py
# Tuples as dict keys
capital_coords = {
    (4.7110, -74.0721): 'Bogotá',
    (-12.0464, -77.0428): 'Lima',
    (-23.5505, -46.6333): 'São Paulo'
}
```

---

# Tuple Unpacking

One of the coolest Python features — you can assign tuple values to multiple variables in one line:

```py
coordinates = (4.7110, -74.0721)

lat, lon = coordinates

print(lat)    # Output: 4.711
print(lon)    # Output: -74.0721
```

This is called **unpacking**. It's super common in Python — you'll see it everywhere, especially when iterating with `.items()`:

```py
for key, value in my_dict.items():
    # key and value are unpacked automatically
```

You can also unpack during the loop itself:

```py
cities = [('Bogotá', 4.7110, -74.0721), ('Lima', -12.0464, -77.0428)]

for city, lat, lon in cities:
    print(f'{city}: ({lat}, {lon})')

# Output:
# Bogotá: (4.711, -74.0721)
# Lima: (-12.0464, -77.0428)
```

---

# Tuple Methods

Tuples only have two methods (because they're immutable — you can't modify them, so most list methods don't apply):

```py
t = (1, 2, 3, 2, 2, 4)

print(t.count(2))    # Output: 3  (how many times 2 appears)
print(t.index(3))    # Output: 2  (index of first occurrence of 3)
```

---

# Converting Between List and Tuple

Easy to switch back and forth:

```py
my_list = [1, 2, 3]
my_tuple = tuple(my_list)      # convert list → tuple
back_to_list = list(my_tuple)  # convert tuple → list

print(type(my_tuple))          # Output: <class 'tuple'>
```

---

## Instructions

Create a `capitals.py` program that:

1. Stores the (latitude, longitude) of 5 Latin American capitals as tuples in a list
2. Loops over the list, unpacking each tuple into variables
3. Prints each capital's name and coordinates in a formatted way

Use these:
- Bogotá, Colombia: (4.7110, -74.0721)
- Lima, Peru: (-12.0464, -77.0428)
- São Paulo, Brazil: (-23.5505, -46.6333)
- Buenos Aires, Argentina: (-34.6037, -58.3816)
- Santiago, Chile: (-33.4569, -70.6483)

## Solved Exercise:

```py
# capitals.py

capitals = [
    ('Bogotá', 4.7110, -74.0721),
    ('Lima', -12.0464, -77.0428),
    ('São Paulo', -23.5505, -46.6333),
    ('Buenos Aires', -34.6037, -58.3816),
    ('Santiago', -33.4569, -70.6483)
]

for city, lat, lon in capitals:
    print(f'{city}: lat {lat}, lon {lon}')

# Output:
# Bogotá: lat 4.711, lon -74.0721
# Lima: lat -12.0464, lon -77.0428
# São Paulo: lat -23.5505, lon -46.6333
# Buenos Aires: lat -34.6037, lon -58.3816
# Santiago: lat -33.4569, lon -70.6483
```

> [!TIP]
> When you need a collection that should never change, use a tuple. When you need flexibility, use a list. The choice communicates your intent to anyone reading the code.

---

# Recap

- Tuples use `()` and are **immutable** — you can't modify them after creation.
- Access items the same as lists: `tuple[0]`, `tuple[-1]`, `tuple[1:3]`
- **Unpacking**: `a, b, c = (1, 2, 3)` — assigns each value to a variable.
- Only two methods: `.count()` and `.index()`
- Convert: `tuple(my_list)` and `list(my_tuple)`
- Tuples can be dictionary keys; lists cannot.

Next: **Chapter 9.1 — Sets**. What if you want a collection with zero duplicates? 🎯
