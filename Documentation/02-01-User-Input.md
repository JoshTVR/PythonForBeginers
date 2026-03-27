# User Input

So far we've been talking *at* Python. We hard-code the values, Python runs, done. But real programs talk *with* the user — they ask questions and wait for answers. 🗣️

That's what `input()` is for.

```py
name = input('What is your name? ')
print(name)
```

When Python hits `input()`, it stops, prints the question, and waits. Whatever the user types gets stored in the variable. Try it — it feels different from anything we've written so far.

---

# The `input()` Function

The syntax is simple:

```py
variable = input('Your prompt here: ')
```

The string inside the parentheses is the prompt — the question or message shown to the user. It's optional, but you should always include it so the user knows what to type.

Here's the catch: **`input()` always returns a string**, even if the user types a number.

```py
age = input('How old are you? ')
print(type(age))

# Output: <class 'str'>
```

So if you ask for someone's age and try to do math with it, Python will complain:

```py
age = input('How old are you? ')
next_birthday = age + 1    # 💥 TypeError: can only concatenate str (not "int") to str
```

That error looks scary, but the fix is easy.

---

# Type Conversion: `int()` and `float()`

To turn a string into a number, wrap it in `int()` or `float()`:

```py
age = int(input('How old are you? '))
next_birthday = age + 1
print(f'Next year you will be {next_birthday}')

# Output: Next year you will be 21  (if user typed 20)
```

`int()` converts to a whole number. `float()` converts to a decimal:

```py
height = float(input('Your height in meters: '))
print(height)

# Output: 1.76
```

> [!TIP]
> Always wrap `input()` in `int()` or `float()` when you need numbers. Forget this once and you'll remember it forever after seeing the error 😅

---

# String Interpolation (f-strings)

When you want to mix variables into printed text, f-strings are the cleanest way:

```py
name = input('What is your name? ')
city = input('What city are you from? ')

print(f'Hey {name}, nice to meet you! I heard {city} is amazing.')

# Output: Hey Josh, nice to meet you! I heard Bogotá is amazing.
```

Put an `f` right before the opening quote, then use `{variable_name}` wherever you want a value to appear. We'll go deeper into f-strings in Chapter 4.

---

## Instructions

The Pythagorean theorem says that in a right triangle, the square of the hypotenuse equals the sum of the squares of the other two sides. Pythagoras figured this out around 570 BC — dude was ahead of his time. 📐

```
c = √(a² + b²)
```

Create a `hypotenus.py` program that:

- Asks the user for side `a` and side `b` (as integers)
- Calculates the hypotenuse `c`
- Prints the result

Hint: in Python, a square root is just raising something to the power of 0.5.

## Solved Exercise:

```py
# hypotenus.py

a = int(input('What is the first short side (a)? '))
b = int(input('What is the second short side (b)? '))

c = ((a**2 + b**2)**0.5)
print(c)

# Example: a=3, b=4
# Output: 5.0
```

---

## Instructions 2

Just got back from a trip through South America 🇨🇴🇵🇪🇧🇷 and I've still got some local currency left over. Let's figure out how much that is in USD.

Create a `currency.py` program that:

- Asks the user how much they have in Colombian pesos (COP)
- Asks how much they have in Peruvian soles (PEN)
- Asks how much they have in Brazilian reais (BRL)
- Converts each amount to USD using the approximate rates below
- Adds everything up and prints the total in USD

Approximate exchange rates:
- 1 COP ≈ 0.0002319 USD
- 1 PEN ≈ 0.2685 USD
- 1 BRL ≈ 0.1722 USD

## Solved Exercise:

```py
# currency.py

co = int(input('How much do you have in Colombian pesos? '))
pe = int(input('How much do you have in Peruvian soles? '))
br = int(input('How much do you have in Brazilian reais? '))

cousd = co * 0.0002319
peusd = pe * 0.2685
brusd = br * 0.1722

leftovers = cousd + peusd + brusd

print(leftovers)

# Example: 50000 COP, 100 PEN, 50 BRL
# Output: 43.255  (approx USD)
```

> [!TIP]
> Exchange rates change daily — google the current rates and update the numbers if you want accurate results!

---

# Recap

- `input()` stops the program and waits for the user to type something.
- `input()` always returns a string, even if the user types a number.
- Use `int()` or `float()` to convert strings to numbers before doing math.
- f-strings let you embed variables directly inside printed text: `f'Hello {name}'`.
- Always include a prompt inside `input()` so the user knows what to type.

Next: Chapter 2.2 — Variables Summary and final exercise! 🎯
