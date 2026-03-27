# Loops

Imagine having to write `print('I will not use Snapchat in class')` 100 times by hand. Yeah, no. That's exactly what loops are for. 🔁

A loop is a way to repeat a block of code multiple times without copy-pasting it. What takes a human an hour, Python does in microseconds.

There are two main types: the `while` loop and the `for` loop. This chapter covers `while`. Think of them like this:
- `while` = keep going *as long as* something is true
- `for` = repeat a *specific number* of times

---

# The `while` Loop

The `while` loop checks a condition before each repetition. As long as the condition is `True`, it keeps running:

```py
while condition:
    # run this code
    # update something so the condition eventually becomes False
```

```py
count = 0

while count < 5:
    print(count)
    count += 1

# Output:
# 0
# 1
# 2
# 3
# 4
```

Step by step:
1. Check: is `count < 5`? → Yes (0 < 5) → run the body
2. Print `0`, increment `count` to 1
3. Check again: is `1 < 5`? → Yes → run again
4. ...keeps going until `count` reaches 5
5. Check: is `5 < 5`? → No → stop

> [!TIP]
> If you forget to update the variable inside the loop (`count += 1`), the condition never becomes `False` and you get an **infinite loop** — your program runs forever. Press `Ctrl+C` in the terminal to force-quit it.

---

# ATM Demo

A great real-world example of a `while` loop: an ATM PIN check. Keep asking for the PIN until the user gets it right.

```py
print('BANK OF PYTHON')

pin = int(input('Enter your PIN: '))

while pin != 1234:
    pin = int(input('Incorrect PIN. Enter your PIN again: '))

print('PIN accepted! 💳')

# Keeps looping until user enters 1234
```

The loop runs while the PIN is *wrong*. The moment the user types the correct PIN (`1234`), the condition `pin != 1234` becomes `False` and the loop stops.

---

## Instructions

Create an `enter_pin.py` program that:

- Prints a bank name banner
- Asks the user to enter a PIN
- Keeps asking if the PIN is wrong
- Prints `'PIN accepted!'` when they get it right (use `1234` as the correct PIN)

## Solved Exercise:

```py
# enter_pin.py

print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
    pin = int(input('Incorrect PIN. Enter your PIN again: '))

print('PIN accepted!')
```

---

# Compound `while` Conditions

You can combine conditions in a `while` loop just like in `if` statements:

```py
guess = 0
tries = 0

while guess != 6 and tries < 3:
    guess = int(input('Guess the number (1-6): '))
    tries += 1
```

This loop stops when *either* the user guesses correctly OR they've used all 3 attempts — whichever happens first.

---

## Instructions 2

Create a `guess.py` program that:

- Generates a random number between 1 and 6
- Gives the user 3 tries to guess it
- Prints `"You got it!"` if they guess correctly
- Prints `"You ran out of tries :("` if they use all 3 without getting it

## Solved Exercise:

```py
# guess.py

import random

num = random.randint(1, 6)
guess = 0
tries = 0

while guess != num and tries < 3:
    guess = int(input('Guess the number (1-6): '))
    tries += 1

    if guess == num:
        print('You got it!')
        print(f'The number was {num}')
    elif tries == 3:
        print('You ran out of tries :(')
        print(f'The number was {num}')
    else:
        print('Try again!')
```

---

# Recap

- A `while` loop repeats code as long as a condition stays `True`.
- Always update the condition variable inside the loop to avoid infinite loops.
- You can combine conditions with `and` and `or`.
- `while` is great when you don't know in advance how many times to loop.

Next: Chapter 4.1 — `for` loops. When you *do* know how many times to repeat. 🔄
