# for Loops

The `while` loop is great when you don't know how many times you'll need to repeat. But when you *do* know — say, exactly 100 times — the `for` loop is cleaner. 🔄

---

# The `range()` Function

Before getting into `for` loops, meet `range()`. It generates a sequence of numbers:

```py
range(6)     # 0, 1, 2, 3, 4, 5
range(1, 6)  # 1, 2, 3, 4, 5
range(0, 10, 2)  # 0, 2, 4, 6, 8  (step of 2)
```

A few things to know:
- `range(n)` starts at 0 and goes up to (but **not including**) `n`
- `range(start, stop)` goes from `start` up to (but not including) `stop`
- `range(start, stop, step)` goes from `start` to `stop`, jumping by `step`

So `range(6)` gives you `0, 1, 2, 3, 4, 5` — six numbers total, but the last one is 5, not 6. This is the same non-inclusive right end as list slicing.

---

# The `for` Loop

```py
for i in range(n):
    # code to repeat
```

`i` is just a variable — it holds the current number from the range. You can name it anything, but `i` is the convention.

```py
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
```

---

## Instructions

A classic school detention punishment: write lines.

Create a `detention.py` program that uses a `for` loop to print `'I will not use Snapchat in class'` 100 times.

## Solved Exercise:

```py
# detention.py

for i in range(100):
    print('I will not use Snapchat in class')

# Output: (prints the line 100 times)
```

What takes a human an hour, Python does in milliseconds. 🤯

---

# String Interpolation (f-strings)

Back in 1949, the EDSAC computer in Cambridge printed its first output — the programmer had to hardcode every character. These days we have f-strings: you drop a variable directly into text with zero effort.

Put an `f` before the opening quote, then use `{variable}` wherever you want a value:

```py
name = 'Josh'
score = 97

print(f'{name} scored {score} points!')

# Output: Josh scored 97 points!
```

You can do math inside the braces too:

```py
price = 9.99
qty = 3

print(f'Total: ${price * qty:.2f}')

# Output: Total: $29.97
```

The `:.2f` part rounds the result to 2 decimal places. Useful for prices and percentages.

---

## Instructions

"99 Bottles of Beer" is a traditional song — the kind you'd sing on a very long road trip. The lyrics count down from 99 to 0:

```
99 bottles of beer on the wall
99 bottles of beer
Take one down, pass it around
98 bottles of beer on the wall
...
```

Create a `99_bottles.py` program that:

- Uses a `for` loop to count down from 99 to 0
- Uses an f-string to print the current count in each line

Hint: you'll need a variable that decrements with each iteration.

## Solved Exercise:

```py
# 99_bottles.py

beers = 99

for i in range(99):
    print(f'{beers} bottles of beer on the wall')
    print(f'{beers} bottles of beer')
    beers -= 1
    print('Take one down, pass it around')

# Output:
# 99 bottles of beer on the wall
# 99 bottles of beer
# Take one down, pass it around
# 98 bottles of beer on the wall
# ...
```

> [!TIP]
> `beers -= 1` is shorthand for `beers = beers - 1`. Python has these for all arithmetic operators: `+=`, `-=`, `*=`, `/=`. They save a lot of typing.

---

# Recap

- `for i in range(n)` repeats a block of code `n` times.
- `range(n)` goes from 0 to n-1 (non-inclusive on the right).
- `range(start, stop, step)` gives you full control over the sequence.
- f-strings: `f'text {variable} text'` — embed variables directly in strings.
- `beers -= 1` is shorthand for `beers = beers - 1`.

Next: Chapter 4.2 — combining `while` and `for` for classic challenges like FizzBuzz! 🔢
