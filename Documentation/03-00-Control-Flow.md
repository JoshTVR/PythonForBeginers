# Control Flow

What if Python could make decisions? Good news: it can. 🚦

So far our programs run top-to-bottom, line by line, every single time. Control flow changes that — it lets the program take different paths depending on what's true or false. Think of it like a Choose Your Own Adventure book 📖: the same story, but different routes.

---

# The `if` Statement

The most basic decision in Python:

```py
if condition:
    # run this code
```

If the condition is `True`, the indented block runs. If it's `False`, Python skips it entirely.

```py
hunger = 8

if hunger > 5:
    print("Time to eat! 🍔")

# Output: Time to eat! 🍔
```

> [!TIP]
> Python uses **indentation** (spaces or a tab) instead of curly braces `{}` to define code blocks. Get this wrong and your program crashes. Most editors auto-indent for you, but keep an eye on it!

---

# The `else` Clause

What if the condition is `False` and we still want something to happen? That's what `else` is for:

```py
if condition:
    # runs if True
else:
    # runs if False
```

```py
grade = 72

if grade >= 55:
    print("You passed.")
else:
    print("You failed.")

# Output: You passed.
```

---

# Relational Operators

To write conditions, we need relational operators — they compare values and return `True` or `False`:

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `7 > 3` | `True` |
| `<` | Less than | `2 < 9` | `True` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `4 <= 6` | `True` |

⚠️ The single most common beginner mistake: using `=` instead of `==` in a condition. One `=` is assignment. Two `==` is comparison.

```py
x = 5          # assignment — x is now 5
x == 5         # comparison — is x equal to 5? (True)
```

---

# The `elif` Clause

Sometimes there are more than two possible outcomes. `elif` (short for "else if") lets us chain as many conditions as we need:

```py
if condition1:
    # ...
elif condition2:
    # ...
elif condition3:
    # ...
else:
    # none of the above
```

Python checks each condition in order — the first one that's `True` wins, and the rest are skipped.

```py
ph = 9

if ph > 7:
    print('The pH is Basic')
elif ph < 7:
    print('The pH is Acidic')
else:
    print('The pH is Neutral')

# Output: The pH is Basic
```

---

## Instructions

Create a `grades.py` program that:

- Asks the user for a numerical grade
- Prints `"You passed."` if the grade is 55 or above
- Prints `"You failed."` if it's below 55

## Solved Exercise:

```py
# grades.py

grade = int(input('What is your grade? '))

if grade >= 55:
    print("You passed.")
else:
    print("You failed.")

# Example: 72
# Output: You passed.
```

---

## Instructions 2

Create a `ph_levels.py` program that:

- Asks the user for a pH value (whole number)
- Prints `'The pH is Basic'` if it's above 7
- Prints `'The pH is Acidic'` if it's below 7
- Prints `'The pH is Neutral'` if it's exactly 7

## Solved Exercise:

```py
# ph_levels.py

ph = int(input('What is the pH? '))

if ph > 7:
    print('The pH is Basic')
elif ph < 7:
    print('The pH is Acidic')
else:
    print('The pH is Neutral')

# Example: 4
# Output: The pH is Acidic
```

---

# Recap

- `if` runs a block of code only when a condition is `True`.
- `else` runs when the `if` condition is `False`.
- `elif` adds more conditions between `if` and `else`.
- Relational operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
- `=` is assignment. `==` is comparison. Never mix them up!
- Indentation matters — it defines which lines belong to which block.

Next up: Chapter 3.1 — the `random` module and how to make our programs unpredictable! 🎱
