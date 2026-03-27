# Variables

In programming, variables are used for storing data values. Think of them as labeled boxes 📦 — you put something inside, give it a name, and whenever you need it, you just call the name.

Each variable has a name and holds a value. The variable name can consist of letters, numbers, and the `_` underscore.

Here's what that looks like in Python:

```py
name = 'Erlich Bachman'
user_id = 16180339887
progress = 0.75
exp = 60
verified = True
```

The `=` sign means **assignment** — we're telling Python "hey, store this value in this box." It's not the same as the math equal sign. Python is basically saying: *"right side goes into left side."*

We can also change the value of a variable after creating it, or print it out:

```py
xp = 70
xp = 80

print(xp)    # Output: 80
```

---

# Data Types

Not all variables hold the same kind of data. Python has four basic data types that every beginner should know:

## int — Integer

An integer is a whole number. No decimal point, no fractions — just a clean, round number. Positive, negative, or zero.

```py
year = 2023
age = 20
temperature = -5
```

If you're counting things (people on a bus, levels in a game, days until the weekend), you're using an `int`.

## float — Floating-point number

A float is a number with a decimal point. When you need precision — measurements, prices, percentages — use a float.

```py
pi = 3.14159
meal_cost = 12.99
batting_average = 0.342
```

## str — String

A string is text. Any characters wrapped in single `' '` or double `" "` quotes.

```py
message = "good nite"
username = '@snoopdogg'
city = 'Bogotá'
```

Strings can hold anything — letters, numbers, symbols, spaces. As long as it's in quotes, Python treats it as text.

## bool — Boolean

A boolean can only be one of two values: `True` or `False`. Named after the British mathematician George Boole (1815–1864) — yes, a person invented the concept of true/false logic. 🧠

```py
late_to_class = False
cranky = True
is_logged_in = True
```

Booleans are tiny but super powerful — they're the heart of every `if` statement we'll write in Chapter 3.

---

# Arithmetic Operators

Python is incredible at math. Now that we have variables, let's do something with them! 🔢

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `4 + 3` | `7` |
| `-` | Subtraction | `4 - 3` | `1` |
| `*` | Multiplication | `4 * 3` | `12` |
| `/` | Division | `4 / 3` | `1.3333` |
| `%` | Modulo | `4 % 3` | `1` |
| `**` | Exponent | `2 ** 3` | `8` |

```py
score = 0           # score is 0
score = 4 + 3       # score is now 7
score = 4 - 3       # score is now 1
score = 4 * 3       # score is now 12
score = 4 / 3       # score is now 1.3333
score = 4 % 3       # score is now 1

print(score)        # Output: 1
```

The `%` modulo operator returns the *remainder* after division. So `4 % 3` is `1` because 3 goes into 4 once with 1 left over. We'll use this a LOT in Chapter 4 with loops.

Here's a real-world example — calculating a 20% tip at a restaurant:

```py
pizza = 2.99
coke = 0.99

total = pizza + coke
tip = total * 0.2

print(tip)          # Output: 0.796
```

Or more compact, using parentheses:

```py
tip = (pizza + coke) * 0.2
```

---

# Exponents

The `**` operator handles exponentiation — things like 2³ or 10². In written math we'd write them as superscripts, but keyboards don't have superscripts, so Python uses `**` instead.

```py
score = 2 ** 2      # score is 4
score = 2 ** 3      # score is now 8
score = 2 ** 4      # score is now 16
score = 2 ** 5      # score is now 32

print(score)        # Output: 32
```

---

## Instructions

The body mass index (BMI) was created by a Belgian mathematician in the 1850s and it's used by health and nutrition professionals to estimate human body fat.

It's calculated by dividing a person's weight in kilograms by the square of their height in meters:

```
bmi = weight / height²
```

Create a `bmi.py` program that:

- Stores a weight value (in kg) in a variable
- Stores a height value (in meters) in a variable
- Calculates the BMI using the formula above
- Prints out the result

## Solved Exercise:

```py
# bmi.py

bmi = 67.600 / (1.76 ** 2)
print(bmi)

# Output: 21.81...
```

> [!TIP]
> Notice how we use `**` to square the height: `1.76 ** 2`. This is the same as 1.76 × 1.76.

---

## Instructions 2

Create a `temperature.py` program that converts a temperature from Fahrenheit to Celsius.

Use the formula:

```
C = (F - 32) × 5/9
```

Start with `F = 60` and print the result.

## Solved Exercise:

```py
# temperature.py

F = 60
C = (F - 32) * 5/9
print(C)

# Output: 15.555555555555555
```

---

# Recap

- Variables are named containers that store data values.
- The `=` operator *assigns* a value — it's not checking for equality.
- Python has four basic data types: `int`, `float`, `str`, `bool`.
- Arithmetic operators: `+`, `-`, `*`, `/`, `%`, `**`.
- The `%` modulo returns the remainder of a division.
- The `**` operator handles exponents.
- Variable names are case-sensitive: `Score` and `score` are different variables.

Next up: Chapter 2.1 — User Input! Time to make Python listen to us. 👂
