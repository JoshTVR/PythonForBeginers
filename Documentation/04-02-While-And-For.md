# FizzBuzz and Vowel Counting

You've got both `while` and `for` in your toolkit now. Let's put them to work on some classics. 💪

---

# The Modulo Operator in Loops

Before FizzBuzz, we need to talk about `%` again — the modulo operator. In loops it's everywhere.

The modulo returns the **remainder** after division:

```py
10 % 3   # → 1   (3 goes into 10 three times, remainder 1)
9 % 3    # → 0   (3 goes into 9 exactly three times, no remainder)
7 % 2    # → 1   (2 goes into 7 three times, remainder 1)
8 % 2    # → 0   (2 goes into 8 exactly, no remainder)
```

The key insight: **if `n % x == 0`, then `n` is divisible by `x`** — it's a multiple of `x`.

So to check if a number is even: `n % 2 == 0`. To check if it's a multiple of 3: `n % 3 == 0`. This is how FizzBuzz works.

---

# FizzBuzz

FizzBuzz is the most famous coding interview question. It famously filters out a huge chunk of candidates who can't figure it out under pressure. The rules:

- Count from 1 to 100
- For multiples of 3, print `"Fizz"` instead of the number
- For multiples of 5, print `"Buzz"` instead of the number
- For multiples of **both** 3 and 5, print `"FizzBuzz"`
- For everything else, just print the number

The critical trap: you must check the `FizzBuzz` condition **first**. If you check `% 3` first, `15` prints `"Fizz"` and never reaches `"FizzBuzz"`.

```py
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# Output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...
```

> [!TIP]
> `range(1, 101)` goes from 1 to 100 inclusive. We use `1` as the start because FizzBuzz counts from 1, not 0. And `101` as the stop because `range()` is non-inclusive on the right.

---

## Instructions

Create a `fizz_buzz.py` program that:

- Counts from 1 to 100
- Prints `"Fizz"` for multiples of 3
- Prints `"Buzz"` for multiples of 5
- Prints `"FizzBuzz"` for multiples of both 3 and 5
- Prints the number for everything else

## Solved Exercise:

```py
# fizz_buzz.py

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
```

---

# Iterating Over a String

Here's something cool — strings are sequences, just like lists. You can loop over them character by character:

```py
word = 'Python'

for character in word:
    print(character)

# Output:
# P
# y
# t
# h
# o
# n
```

The `in` operator also works to check membership:

```py
vowels = ['a', 'e', 'i', 'o', 'u']

if 'a' in vowels:
    print('Found a vowel!')

# Output: Found a vowel!
```

Combine both ideas and you can count vowels in any word.

---

## Instructions

Create a `vowels.py` program that:

- Asks the user to enter a word
- Counts how many vowels are in the word
- Prints the count

## Solved Exercise:

```py
# vowels.py

vowels = ['a', 'e', 'i', 'o', 'u']
word = input('What word would you like to search? ')
count = 0

for character in word:
    if character in vowels:
        count += 1

print(count)

# Example: 'python'
# Output: 1  (only 'o' is a vowel)
```

---

# Chapter 4 — Recap

- `for i in range(1, 101)` goes from 1 to 100 (non-inclusive stop).
- `n % x == 0` checks if `n` is divisible by `x`.
- When checking multiple modulo conditions, check the most specific one first.
- Strings are sequences — you can iterate over characters with `for c in word`.
- The `in` operator checks membership: `'a' in vowels` returns `True` or `False`.

Python also has `break` (exit the loop immediately) and `continue` (skip to the next iteration) — we'll use those more in later chapters!

Next up: **Chapter 4.3 — Turtle Graphics**. Time to make Python draw something. 🐢
