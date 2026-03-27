# Logical Operators

One condition is sometimes enough. But what if you need TWO things to be true at the same time? Or at least one of them? That's where logical operators come in. 🧠

Python has three: `and`, `or`, `not`.

---

# `and`

Both conditions must be `True` for the whole thing to be `True`.

```py
hunger = 7
anger = 3

if hunger > 4 and anger > 1:
    print("I'm hangry 😤")

# Output: I'm hangry 😤
```

Truth table for `and`:

| A | B | A and B |
|---|---|---------|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

Only one combination gives `True`: both sides must be `True`.

---

# `or`

At least one condition needs to be `True`.

```py
has_coffee = False
has_bubble_tea = True

if has_coffee or has_bubble_tea:
    print("Ready to code ☕🧋")

# Output: Ready to code ☕🧋
```

Truth table for `or`:

| A | B | A or B |
|---|---|--------|
| True | True | **True** |
| True | False | **True** |
| False | True | **True** |
| False | False | False |

Only fails when *both* are `False`.

---

# `not`

Flips a boolean. `True` becomes `False`, `False` becomes `True`.

```py
tired = False

if not tired:
    print("Time to build something 💻")

# Output: Time to build something 💻
```

---

# Combining Conditions

You can stack multiple conditions together. Use parentheses to make the logic clear:

```py
height = 145
credits = 12

if height >= 137 and credits >= 10:
    print("Enjoy the ride! 🎢")
elif height < 137 and credits < 10:
    print("Your height and credits are insufficient.")
elif height < 137:
    print("You are not tall enough to ride.")
else:
    print("You don't have enough credits.")
```

---

## Instructions

The Cyclone is a ride at Coney Island with some requirements:

- You must be at least 137 cm tall
- You must have at least 10 credits

Create a `the_cyclone.py` program that:

- Asks the user for their height in cm
- Asks the user for how many credits they have
- Prints the appropriate message based on whether they meet the requirements

There are 4 outcomes:
1. Both requirements met → `"Enjoy the ride! 🎢"`
2. Too short AND not enough credits → `"Your height and credits are insufficient."`
3. Too short only → `"You are not tall enough to ride."`
4. Not enough credits only → `"You don't have enough credits."`

## Solved Exercise:

```py
# the_cyclone.py

height = int(input('What is your height in cm? '))
credits = int(input('How many credits do you have? '))

if height >= 137 and credits >= 10:
    print("Enjoy the ride! 🎢")
elif height < 137 and credits < 10:
    print("Your height and credits are insufficient.")
elif height < 137:
    print("You are not tall enough to ride.")
else:
    print("You don't have enough credits.")

# Example: height=150, credits=5
# Output: You don't have enough credits.
```

---

## Instructions 2

The Hogwarts Sorting Hat quiz! 🧙 Based on a series of questions, the hat assigns you to one of four houses: Gryffindor, Ravenclaw, Hufflepuff, or Slytherin.

Create a `sorting_hat.py` program that asks 3 questions and accumulates points for each house. At the end, whichever house has the most points wins.

**Q1 — Do you prefer Dawn or Dusk?**
- 1) Dawn → +1 Gryffindor, +1 Ravenclaw
- 2) Dusk → +1 Hufflepuff, +1 Slytherin

**Q2 — When I'm dead, I want people to remember me as:**
- 1) The Good → +2 Hufflepuff
- 2) The Great → +2 Slytherin
- 3) The Wise → +2 Ravenclaw
- 4) The Bold → +2 Gryffindor

**Q3 — Which kind of instrument most pleases your ear?**
- 1) The violin → +4 Slytherin
- 2) The trumpet → +4 Hufflepuff
- 3) The piano → +4 Ravenclaw
- 4) The drum → +4 Gryffindor

At the end, print whichever house has the highest score.

## Solved Exercise:

```py
# sorting_hat.py

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

Q1 = int(input('Q1) Do you prefer Dawn or Dusk?\n1) Dawn\n2) Dusk\n'))

if Q1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif Q1 == 2:
    hufflepuff += 1
    slytherin += 1

Q2 = int(input('Q2) When I\'m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n'))

if Q2 == 1:
    hufflepuff += 2
elif Q2 == 2:
    slytherin += 2
elif Q2 == 3:
    ravenclaw += 2
elif Q2 == 4:
    gryffindor += 2

Q3 = int(input('Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n'))

if Q3 == 1:
    slytherin += 4
elif Q3 == 2:
    hufflepuff += 4
elif Q3 == 3:
    ravenclaw += 4
elif Q3 == 4:
    gryffindor += 4

if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
    print('🦁 Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
    print('🦅 Ravenclaw!')
elif hufflepuff >= slytherin:
    print('🦡 Hufflepuff!')
else:
    print('🐍 Slytherin!')
```

> [!TIP]
> The `+=` shortcut: `gryffindor += 1` is the same as `gryffindor = gryffindor + 1`. Python has these for all arithmetic operators: `+=`, `-=`, `*=`, `/=`.

---

# Chapter 3 — Recap

- `and` → both conditions must be True
- `or` → at least one condition must be True
- `not` → flips True to False and vice versa
- You can chain as many conditions as needed with `elif`
- Use parentheses to group complex conditions and keep things readable

You can now make Python think! 🧠 Next up: **Chapter 4 — Loops**. Time to make Python repeat itself (intentionally). 🔁
