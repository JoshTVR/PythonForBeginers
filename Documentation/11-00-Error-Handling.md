# Error Handling

Real talk: your programs will crash. That's not failure — it's normal. Every developer deals with it. The question is: do you let the crash explode in the user's face with a scary traceback, or do you handle it gracefully? 💥 vs 🤝

---

# Common Error Types

You've already seen some of these without realizing it:

| Error | When it happens | Example |
|-------|----------------|---------|
| `SyntaxError` | Invalid Python syntax | `if x = 5:` (should be `==`) |
| `NameError` | Variable doesn't exist | `print(x)` before defining `x` |
| `TypeError` | Wrong data type | `'age' + 5` (can't add str and int) |
| `ValueError` | Right type, wrong value | `int('hello')` |
| `IndexError` | List index out of range | `my_list[99]` on a 3-item list |
| `KeyError` | Dict key doesn't exist | `my_dict['missing_key']` |
| `ZeroDivisionError` | Dividing by zero | `10 / 0` |
| `FileNotFoundError` | File doesn't exist | `open('ghost.txt')` |

---

# Reading Tracebacks

When Python crashes, it gives you a **traceback** — a stack trace that tells you exactly what went wrong and where. It looks scary but it's actually very helpful once you know how to read it:

```
Traceback (most recent call last):
  File "my_script.py", line 5, in <module>
    result = 10 / number
ZeroDivisionError: division by zero
```

Read it **bottom to top**:
1. Last line: the error type and message — this is the main thing
2. Middle lines: the call stack — which file, which line
3. First line: just says "here comes a traceback"

---

# `try` / `except`

Wrap risky code in a `try` block. If an error occurs, Python jumps to `except` instead of crashing:

```py
try:
    number = int(input('Enter a number: '))
    print(10 / number)
except:
    print('Something went wrong!')
```

But bare `except` catches *everything* — even keyboard interrupts and system exits. That makes programs hard to stop and hides bugs. Always catch specific errors:

```py
try:
    number = int(input('Enter a number: '))
    print(10 / number)
except ValueError:
    print('That was not a number!')
except ZeroDivisionError:
    print('Cannot divide by zero!')
```

---

# Multiple `except` Blocks

You can handle different errors differently:

```py
try:
    data = [1, 2, 3]
    index = int(input('Which index? '))
    print(data[index])
except ValueError:
    print('Please enter a whole number.')
except IndexError:
    print(f'Index out of range. List has {len(data)} items.')
```

---

# `else` and `finally`

Two optional clauses that are often forgotten:

**`else`** — runs only if *no exception* occurred:

```py
try:
    result = int(input('Enter a number: '))
except ValueError:
    print('Not a number!')
else:
    print(f'You entered: {result}')   # only runs if no error
```

**`finally`** — runs *always*, whether there was an error or not. Great for cleanup:

```py
try:
    file = open('data.txt')
    content = file.read()
except FileNotFoundError:
    print('File not found!')
finally:
    print('Done.')    # always prints, error or not
```

---

# Raising Exceptions

You can raise errors yourself to enforce rules:

```py
def set_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative!')
    return age

set_age(-5)    # 💥 ValueError: Age cannot be negative!
```

This is how you validate data at the edges of your program — user input, API responses, file data.

> [!TIP]
> Never use bare `except:` without specifying the exception type. It catches *everything* — including `KeyboardInterrupt` (Ctrl+C) and `SystemExit` — which makes your program impossible to stop cleanly and hides real bugs.

---

## Instructions

Create a `safe_division.py` program that:

1. Asks the user for two numbers (numerator and denominator)
2. Divides them and prints the result
3. Handles `ValueError` if the user types something that isn't a number
4. Handles `ZeroDivisionError` if the denominator is zero
5. Prints a success message in the `else` block

## Solved Exercise:

```py
# safe_division.py

try:
    numerator = float(input('Enter numerator: '))
    denominator = float(input('Enter denominator: '))
    result = numerator / denominator
except ValueError:
    print('Please enter valid numbers only.')
except ZeroDivisionError:
    print('Cannot divide by zero!')
else:
    print(f'{numerator} / {denominator} = {result:.4f}')
finally:
    print('Calculator done.')

# Example (valid input): 10 / 4
# Output:
# 10.0 / 4.0 = 2.5000
# Calculator done.

# Example (zero denominator):
# Output:
# Cannot divide by zero!
# Calculator done.
```

---

## Instructions 2

Create a `safe_input.py` function called `get_integer` that:

- Keeps asking for input until the user enters a valid integer
- Uses a `while True` loop with `try/except`
- Returns the integer once it's valid

## Solved Exercise:

```py
# safe_input.py

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('That\'s not a whole number. Try again!')

age = get_integer('Enter your age: ')
print(f'In 10 years you\'ll be {age + 10}')
```

---

# Recap

- Errors are normal — handle them instead of letting them crash everything.
- `try` wraps risky code. `except ErrorType` catches specific errors.
- `else` runs if no error occurred. `finally` always runs.
- `raise` lets you throw errors yourself.
- Always catch specific exceptions, not bare `except`.
- Read tracebacks bottom to top — the last line is the most important.

Next: **Chapter 12 — File Handling**. Time to save data that survives after your program ends. 💾
