# Variables — Summary

Chapter 2 is a wrap! 🎉 You now know how to store data, work with different types, do math, and get input from the user. That's a huge foundation.

Here's a recap of everything:

- Variables are named containers that store values: `name = 'Josh'`
- The `=` sign is assignment, not equality.
- Python has four basic types: `int`, `float`, `str`, `bool`.
- Arithmetic operators: `+` `-` `*` `/` `%` `**`
- The `%` modulo returns the remainder: `7 % 3` → `1`
- The `**` exponent raises a number to a power: `2 ** 8` → `256`
- `input()` always returns a `str` — use `int()` or `float()` to convert.
- f-strings: `f'Hello {name}'` — the cleanest way to mix variables into text.

---

# Quick Reference

| Concept | Example | Notes |
|---------|---------|-------|
| Declare a variable | `score = 0` | Any type |
| Integer | `age = 20` | Whole number |
| Float | `price = 4.99` | Decimal number |
| String | `city = 'Medellín'` | Text in quotes |
| Boolean | `logged_in = True` | Only `True` or `False` |
| Addition | `total = a + b` | |
| Modulo | `remainder = 10 % 3` | Returns `1` |
| Exponent | `squared = 4 ** 2` | Returns `16` |
| User input (string) | `name = input('...')` | Always returns str |
| User input (number) | `n = int(input('...'))` | Convert with int() |
| f-string | `f'Hi {name}!'` | Embed variables in text |

---

## Instructions

The quadratic formula finds the roots of any equation in the form `ax² + bx + c = 0`.

```
x = (-b ± √(b² - 4ac)) / 2a
```

Create a `quadratic.py` program that:

- Asks the user for values `a`, `b`, and `c`
- Calculates both roots (`x1` and `x2`) using the formula
- Prints both results

Hint: `±` means you calculate twice — once with `+` and once with `-`.

## Solved Exercise:

```py
# quadratic.py

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

root1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
root2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)

print(root1)
print(root2)

# Example: a=1, b=-5, c=6
# Output:
# 3.0
# 2.0
```

> [!TIP]
> If `b*b - 4*a*c` is negative, you'll get a complex number error — that's expected! Real roots only exist when the discriminant is zero or positive. We'll handle errors like this in Chapter 11. 🛡️

---

You finished Chapter 2! 🏅 Variables are officially in your toolkit. Next stop: **Chapter 3 — Control Flow**, where Python starts making decisions. 🚦
