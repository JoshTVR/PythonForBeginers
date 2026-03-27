# Functions

As our code gets longer and longer, you might find yourself copying and pasting a particular code block in different parts of the program. That's no good!

"Don't Repeat Yourself" (DRY) is a principle in software development aimed at reducing repetition. Functions are the main tool for this.

A **function** is a reusable block of code that performs a specific task. You write it once, give it a name, and call it wherever you need it. Five lines of code, twenty lines of code — throw it in a function and use it anywhere.

Plot twist: we've been using functions all along. 🧩

Built-in functions like `print()`, `input()`, and `len()` are 68 functions that come with Python — ready to use, no setup required. Like a car: you don't need to know what's under the hood to drive it.

---

# Defining Your Own Functions

The `def` keyword defines a function:

```py
def greet():
    print('Hola! 👋')
```

To **call** (run) the function, write its name followed by parentheses:

```py
greet()

# Output: Hola! 👋
```

The function only runs when you call it. Defining it doesn't execute anything.

```py
def greet():
    print('Hola! 👋')

# Nothing happens yet...

greet()     # Now it runs
greet()     # Run it again
greet()     # And again

# Output:
# Hola! 👋
# Hola! 👋
# Hola! 👋
```

That's the whole point — define once, use many times.

---

# Parameters and Arguments

Functions become way more powerful when they accept inputs. Those inputs are called **parameters**:

```py
def greet(name):
    print(f'Hola, {name}! 👋')

greet('Josh')
greet('María')
greet('Tomás')

# Output:
# Hola, Josh! 👋
# Hola, María! 👋
# Hola, Tomás! 👋
```

`name` is the **parameter** (the placeholder in the function definition). `'Josh'` is the **argument** (the actual value passed when calling). The distinction doesn't matter much now, but you'll hear both terms.

You can have multiple parameters — just separate them with commas:

```py
def convert_to_usd(cop_amount, rate=0.00023):
    usd = cop_amount * rate
    print(f'${cop_amount:,} COP = ${usd:.2f} USD')

convert_to_usd(50000)
convert_to_usd(200000)

# Output:
# $50,000 COP = $11.50 USD
# $200,000 COP = $46.00 USD
```

`rate=0.00023` is a **default parameter** — if you don't pass a value for it, it uses the default. But you can override it:

```py
convert_to_usd(50000, 0.00025)   # uses 0.00025 instead
```

---

# Return Values

Right now our functions just print things. But what if you want to use the result elsewhere in your program? That's what `return` is for:

```py
def add(a, b):
    return a + b

result = add(3, 5)
print(result)

# Output: 8
```

The `return` statement sends a value *back* to wherever the function was called from. After `return`, the function stops — no more lines execute.

Critical difference: `print()` shows something on screen. `return` sends a value back that you can store in a variable and use later.

```py
def square(n):
    return n * n

x = square(4)      # x is now 16
y = square(x)      # y is now 256

print(y)           # Output: 256
```

---

# Variable Scope

Variables created inside a function only exist inside that function — they're **local** variables:

```py
def my_function():
    local_var = 'I only exist in here'
    print(local_var)

my_function()
print(local_var)    # 💥 NameError: name 'local_var' is not defined
```

Think of it like what happens in Vegas — local variables stay inside the function. 🎲

Variables created outside any function are **global** — they can be read from anywhere:

```py
greeting = 'Hola'

def say_hi(name):
    print(f'{greeting}, {name}!')    # can read the global

say_hi('Josh')

# Output: Hola, Josh!
```

---

# Docstrings

Python functions can have a built-in description — a **docstring** — right after the `def` line:

```py
def calculate_tip(bill, percent=15):
    """
    Calculate the tip amount for a restaurant bill.
    bill: the total bill in dollars
    percent: tip percentage (default 15%)
    """
    return bill * (percent / 100)
```

Docstrings go between triple quotes `"""`. They show up when you call `help(function_name)`. This is how real developers document their functions.

---

## Instructions

Create a `dry.py` program that:

1. Picks 4 built-in functions you've used before in this course
2. Picks 1 built-in function you haven't seen yet (check the [Python docs](https://docs.python.org/3/library/functions.html) or Google it)
3. Uses each function at least once
4. Adds a comment explaining what each one does

## Solved Exercise:

```py
# dry.py

# len() — returns the number of items in a list or string
print(len([1, 2, 3, 4, 5]))        # Output: 5

# max() — returns the largest value
print(max([4, 8, 15, 16, 23, 42])) # Output: 42

# int() — converts a value to an integer
print(int('99'))                    # Output: 99

# round() — rounds a number to n decimal places
print(round(3.14159, 2))           # Output: 3.14

# abs() — returns the absolute value (new one!)
print(abs(-27))                    # Output: 27
```

---

## Instructions 2

Create a `tip_calculator.py` program with a function called `calculate_tip` that:

- Takes a `bill` amount and a `tip_percent` as parameters
- Has a default tip of 15% if no percentage is given
- Returns the tip amount
- Prints a clean summary using an f-string

Call the function a few times with different bills and tip percentages.

## Solved Exercise:

```py
# tip_calculator.py

def calculate_tip(bill, tip_percent=15):
    """Calculate tip amount for a restaurant bill."""
    tip = bill * (tip_percent / 100)
    return tip

tip1 = calculate_tip(50)           # uses default 15%
tip2 = calculate_tip(80, 20)       # 20% tip
tip3 = calculate_tip(120, 10)      # 10% tip

print(f'Bill: $50  | Tip (15%): ${tip1:.2f}')
print(f'Bill: $80  | Tip (20%): ${tip2:.2f}')
print(f'Bill: $120 | Tip (10%): ${tip3:.2f}')

# Output:
# Bill: $50  | Tip (15%): $7.50
# Bill: $80  | Tip (20%): $16.00
# Bill: $120 | Tip (10%): $12.00
```

> [!TIP]
> Functions are one of the biggest quality-of-life improvements in programming. If you find yourself copy-pasting a block of code more than twice, that's a strong signal to wrap it in a function.

---

# Recap

- `def function_name():` defines a function.
- Call a function with `function_name()`.
- **Parameters** are placeholders; **arguments** are the actual values passed.
- Default parameters: `def greet(name='stranger')` — used when no argument is given.
- `return` sends a value back from the function.
- Local variables only exist inside the function they're defined in.
- Docstrings (`"""..."""`) document what a function does.
- DRY — Don't Repeat Yourself. If you're copy-pasting code, write a function.

Chapter 7 — done! 🚀 Next up: **Chapter 8 — Dictionaries**. A whole new way to store and look up data.
