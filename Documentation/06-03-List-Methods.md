# List Methods

Besides built-in functions, Python lists come with their own built-in methods. The difference? Methods use **dot notation** — you attach them directly to the list variable:

```py
my_list.method()    # method
len(my_list)        # function
```

Methods only work on lists. Functions work on many things.

---

# Adding Items

## `.append()`

Adds an item to the **end** of the list:

```py
playlist = ['Bad Bunny - Tití Me Preguntó', 'J Balvin - Con Calma']

playlist.append('Karol G - CAIRO')
print(playlist)

# Output: ['Bad Bunny - Tití Me Preguntó', 'J Balvin - Con Calma', 'Karol G - CAIRO']
```

## `.insert()`

Adds an item at a **specific index**. Everything from that index onwards shifts right:

```py
dna = ['AUG', 'AUC', 'UCG']

dna.insert(2, 'GAU')
print(dna)

# Output: ['AUG', 'AUC', 'GAU', 'UCG']
```

The first argument is the index position, the second is the item to insert.

---

# Removing Items

## `.remove()`

Removes an item by **value**. Finds the first occurrence and deletes it:

```py
books = ['Harry Potter', '1984', 'The Fault in Our Stars']

books.remove('1984')
print(books)

# Output: ['Harry Potter', 'The Fault in Our Stars']
```

If the value doesn't exist, Python raises a `ValueError`. Make sure the item is actually in the list first.

## `.pop()`

Removes an item by **index** and returns the removed item:

```py
fruits = ['apple', 'banana', 'cherry']

removed = fruits.pop(1)
print(removed)    # Output: banana
print(fruits)     # Output: ['apple', 'cherry']
```

If you call `.pop()` with no argument, it removes and returns the **last** item:

```py
fruits.pop()      # removes 'cherry'
```

> [!TIP]
> `.remove()` targets by *value*. `.pop()` targets by *index*. This is the most common point of confusion with list methods — it clicked for me after making the wrong one work exactly zero times 😅

---

# Sorting and Reversing

## `.sort()`

Sorts the list **in place** — modifies the original directly:

```py
scores = [88, 42, 97, 61, 75]

scores.sort()
print(scores)

# Output: [42, 61, 75, 88, 97]
```

To sort in reverse order: `scores.sort(reverse=True)`

## `.reverse()`

Reverses the list in place (not the same as sorting descending — it just flips the current order):

```py
steps = ['wake up', 'shower', 'coffee', 'code']

steps.reverse()
print(steps)

# Output: ['code', 'coffee', 'shower', 'wake up']
```

---

# Searching

## `.count()`

Returns how many times a value appears in the list:

```py
grades = [90, 85, 90, 72, 90, 88]

print(grades.count(90))    # Output: 3
```

## `.index()`

Returns the index of the first occurrence of a value:

```py
colors = ['red', 'green', 'blue', 'green']

print(colors.index('green'))    # Output: 1  (first occurrence)
```

---

# Other Methods

## `.extend()`

Merges another list into the current one:

```py
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
print(list1)

# Output: [1, 2, 3, 4, 5, 6]
```

## `.clear()`

Removes all items from the list (but keeps the list variable):

```py
cart = ['shoes', 'jacket', 'hat']
cart.clear()
print(cart)

# Output: []
```

---

# All 11 Methods

| Method | Description |
|--------|-------------|
| `.append(x)` | Add item `x` to the end |
| `.insert(i, x)` | Insert `x` at index `i` |
| `.remove(x)` | Remove first occurrence of `x` |
| `.pop(i)` | Remove and return item at index `i` (default: last) |
| `.sort()` | Sort in place |
| `.reverse()` | Reverse in place |
| `.count(x)` | Count occurrences of `x` |
| `.index(x)` | Return index of first `x` |
| `.extend(list)` | Merge another list in |
| `.copy()` | Return a shallow copy |
| `.clear()` | Remove all items |

---

## Instructions

Let's start a book club! 📚

Create a `reading_list.py` program that stores the following books:

- `'Harry Potter'`
- `'1984'`
- `'The Fault in Our Stars'`
- `'The Mom Test'`
- `'Life in Code'`

Then:
1. Add `'Pachinko'` to the list using `.append()`
2. Remove `'The Fault in Our Stars'` using `.remove()`
3. Remove `'1984'` using `.pop()` (hint: what index is it at after step 2?)
4. Print the final list

## Solved Exercise:

```py
# reading_list.py

books = ['Harry Potter', '1984', 'The Fault in Our Stars', 'The Mom Test', 'Life in Code']

books.append('Pachinko')
books.remove('The Fault in Our Stars')
books.pop(1)   # '1984' is now at index 1

print(books)

# Output: ['Harry Potter', 'The Mom Test', 'Life in Code', 'Pachinko']
```
