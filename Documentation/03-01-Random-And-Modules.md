# The `random` Module

Time to add some chaos to our programs. 🎱

Everything we've written so far is 100% predictable — run it once, run it a thousand times, same result. But real programs aren't like that. Games, simulations, quizzes — they all need randomness. That's where the `random` module comes in.

---

# What's a Module?

Python's standard library ships with 200+ modules — collections of pre-written code you can plug into your programs. Think of them as DLC packs for Python 🎮. You don't write everything from scratch; you import what you need.

To use a module, you need to `import` it at the top of your file:

```py
import random
```

That one line unlocks everything in the `random` module. Then you call its functions using the `module_name.function()` syntax.

---

# `random.randint()`

The most useful function in the module for beginners: `random.randint(a, b)`. It gives back a random integer between `a` and `b`, **inclusive on both ends**.

```py
import random

num = random.randint(1, 6)
print(num)

# Output: 4  (could be 1, 2, 3, 4, 5, or 6 — different every time!)
```

Every time you run it, you'll get a different number. That's the whole point. ✨

Here's a coin flip — 50/50 heads or tails:

```py
import random

num = random.randint(0, 1)

if num > 0:
    print('Heads')
else:
    print('Tails')
```

---

# `random.choice()`

If you have a list and want to pick one item at random, `random.choice()` handles it:

```py
import random

options = ['rock', 'paper', 'scissors']
pick = random.choice(options)
print(pick)

# Output: paper  (random each time)
```

We'll use this a lot in Chapter 5 with the Rock Paper Scissors project.

---

## Instructions

The Magic 8 Ball is a toy invented in the 1940s. You ask it a yes/no question, shake it, and a random answer floats up through a dark liquid window. 🎱

The original has 20 answers — 10 positive, 5 neutral, 5 negative. We'll build a simplified version with 9.

Create a `magic8.py` program that:

- Asks the user to type a yes/no question
- Generates a random number between 1 and 9
- Prints a different Magic 8 Ball response for each number

The 9 responses:
1. Yes — definitely.
2. It is decidedly so.
3. Without a doubt.
4. Reply hazy, try again.
5. Ask again later.
6. Better not tell you now.
7. My sources say no.
8. Outlook not so good.
9. Very doubtful.

## Solved Exercise:

```py
# magic8.py

import random

input('Make a question for the MAGIC 8 BALL!!!! ')

num = random.randint(1, 9)

if num == 1:
    print('Yes — definitely.')
elif num == 2:
    print('It is decidedly so.')
elif num == 3:
    print('Without a doubt.')
elif num == 4:
    print('Reply hazy, try again.')
elif num == 5:
    print('Ask again later.')
elif num == 6:
    print('Better not tell you now.')
elif num == 7:
    print('My sources say no.')
elif num == 8:
    print('Outlook not so good.')
else:
    print('Very doubtful.')

# Output: (random answer each time)
```

> [!TIP]
> Notice we put `import random` at the very top of the file — that's the convention in Python. Imports always go first.

---

# Recap

- A **module** is a collection of pre-written Python code you can import and use.
- `import module_name` at the top of your file.
- `random.randint(a, b)` returns a random integer from `a` to `b` (inclusive).
- `random.choice(list)` picks a random item from a list.
- Modules save you from writing everything yourself — use them!

Next: Chapter 3.2 — Logical Operators. What happens when one condition isn't enough? 🧠
