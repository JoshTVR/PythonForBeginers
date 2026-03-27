# Built-in Functions

Python ships with 68 built-in functions. Like a Swiss Army knife that's always in your pocket 🔪 — they're there, ready to use, no import needed.

We've actually been using some this whole time (`print()`, `input()`, `int()`). Now let's look at the ones that work great with lists.

---

# `len()`, `max()`, `min()`

The three most common list functions:

```py
stock1_prices = [2.52, 2.44, 2.32, 2.41, 2.51, 2.50, 2.44]
stock2_prices = [8.36, 8.31, 8.21, 8.21, 8.25, 8.11, 8.13]

print(len(stock1_prices))      # Output: 7
print(max(stock1_prices))      # Output: 2.52
print(min(stock2_prices))      # Output: 8.11
```

We can find a list's length, minimum, and maximum in a split second, even if the list has 10,000 items.

---

# `sum()`

Adds up every number in a list:

```py
ventas_cafe = [15000, 28000, 32000, 19500, 41000]

total = sum(ventas_cafe)
print(total)

# Output: 135500
```

Great for totaling sales, scores, budgets — anything you'd add up manually.

---

# `sorted()`

Returns a **new** sorted list without modifying the original:

```py
scores = [88, 42, 97, 61, 75]

ranked = sorted(scores)
print(ranked)
print(scores)

# Output:
# [42, 61, 75, 88, 97]
# [88, 42, 97, 61, 75]  ← original unchanged
```

To sort in reverse:

```py
ranked_desc = sorted(scores, reverse=True)
print(ranked_desc)

# Output: [97, 88, 75, 61, 42]
```

> [!TIP]
> `sorted()` returns a new list. The list method `.sort()` (from the next chapter) modifies the list in place. Use `sorted()` when you want to keep the original untouched.

---

# `type()`

Returns the data type of any value — super useful for debugging:

```py
print(type(42))           # Output: <class 'int'>
print(type(3.14))         # Output: <class 'float'>
print(type('hola'))       # Output: <class 'str'>
print(type(True))         # Output: <class 'bool'>
print(type([1, 2, 3]))    # Output: <class 'list'>
```

When something isn't behaving the way you expect, `type()` is usually the first thing to check.

---

# `abs()`

Returns the absolute value of a number — always positive:

```py
temp_change = -7

print(abs(temp_change))     # Output: 7
print(abs(15))              # Output: 15
print(abs(-3.5))            # Output: 3.5
```

---

# `round()`

Rounds a number to the nearest integer, or to a specific number of decimal places:

```py
price_usd = 12.345678

print(round(price_usd))       # Output: 12
print(round(price_usd, 2))    # Output: 12.35
print(round(price_usd, 4))    # Output: 12.3457
```

---

# Quick Reference

| Function | What it does | Example |
|----------|-------------|---------|
| `len(list)` | Length of the list | `len([1,2,3])` → `3` |
| `max(list)` | Largest value | `max([5,2,8])` → `8` |
| `min(list)` | Smallest value | `min([5,2,8])` → `2` |
| `sum(list)` | Sum of all values | `sum([1,2,3])` → `6` |
| `sorted(list)` | New sorted copy | `sorted([3,1,2])` → `[1,2,3]` |
| `type(x)` | Data type of x | `type(42)` → `<class 'int'>` |
| `abs(n)` | Absolute value | `abs(-5)` → `5` |
| `round(n, d)` | Round to d decimals | `round(3.14159, 2)` → `3.14` |

---

## Instructions

The North Pole elves need your help! Thousands of LEGO toys need to be packed and shipped.

Create an `inventory.py` program with the following list:

```py
lego_parts = [8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1279, 679, 589]
```

Each item is the quantity of a particular LEGO part in stock.

Using built-in functions, figure out:
- Which part is running low? (use `min()`)
- Which part is overstocked? (use `max()`)
- How many different part types are there? (use `len()`)
- What's the total number of parts across all types? (use `sum()`)

Bonus: use `sorted()` to print the inventory in order from lowest to highest stock.

## Solved Exercise:

```py
# inventory.py

lego_parts = [8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1279, 679, 589]

print(f'Running low on: {min(lego_parts)} units')
print(f'Overstocked: {max(lego_parts)} units')
print(f'Total part types: {len(lego_parts)}')
print(f'Total units: {sum(lego_parts)}')
print(f'Sorted: {sorted(lego_parts)}')

# Output:
# Running low on: 589 units
# Overstocked: 92232 units
# Total part types: 12
# Total units: 222878
# Sorted: [589, 679, 1203, 1279, 2328, 5343, 7319, 7323, 8903, 8980, 82700, 92232]
```
