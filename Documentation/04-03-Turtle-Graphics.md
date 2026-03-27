# Turtle Graphics

We've been printing text this whole chapter. What if we could *draw* instead? 🐢

Meet Python Turtle — a drawing module that's been part of Python's standard library forever. It's built-in, no installation needed.

---

# A Little History

The "turtle" idea comes from MIT in the 1960s. Logo, an educational programming language, used a small triangular robot called a "turtle" that moved around the floor drawing lines as it went. Python's `turtle` module recreates that concept on screen — a cursor (the "turtle") moves around a canvas and draws as it goes.

---

# Two Modules at Once

Our script uses two modules:

```py
import turtle, colorsys
```

You can import multiple modules in one line by separating them with commas.

- `turtle` — the drawing library
- `colorsys` — converts between color formats. We'll use it to cycle through the full rainbow 🌈

---

# Walking Through the Code

Here's the full script:

```py
import turtle, colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("Black")
h = 0

for _ in range(100):
    t.color(colorsys.hsv_to_rgb(h, 1, 1))
    t.circle(100)
    t.left(36)
    h += 0.1

t.hideturtle()
turtle.done()
```

Let's break it down line by line:

**`t = turtle.Turtle()`**
Creates a turtle object — the drawing cursor. We name it `t` for short.

**`t.speed(0)`**
Sets drawing speed to maximum. Without this, watching it draw would take forever.

**`turtle.bgcolor("Black")`**
Sets the canvas background to black. The colorful spirals pop much better against dark backgrounds.

**`h = 0`**
This is our hue variable. Hue is the "color" part of the HSV color model — it goes from 0.0 (red) to 1.0 (back to red, having cycled through the whole rainbow).

**`for _ in range(100)`**
The `_` is a Python convention for "I don't actually need this loop variable." We're just saying "repeat 100 times." Using `_` instead of `i` signals to anyone reading the code: the counter value doesn't matter here.

**`t.color(colorsys.hsv_to_rgb(h, 1, 1))`**
`colorsys.hsv_to_rgb(h, s, v)` converts a color from HSV (Hue, Saturation, Value) to RGB format. `h` changes each iteration, cycling through colors. Saturation `1` and Value `1` keep colors bright and vivid.

**`t.circle(100)`**
Draws a circle with radius 100. The turtle moves forward while curving, tracing out the circle.

**`t.left(36)`**
Rotates the turtle 36 degrees to the left. After 10 circles (10 × 36° = 360°), the turtle has done a full rotation — creating the spiral overlap effect.

**`h += 0.1`**
Advances the hue by 0.1 each loop. 10 iterations × 0.1 = 1.0, which cycles through the entire color spectrum.

**`t.hideturtle()`**
Hides the arrow cursor at the end so the final image looks clean.

**`turtle.done()`**
Tells Python the drawing is finished. Keeps the window open until you close it.

<!-- TODO: add screenshot of the final spiral output -->

---

## Instructions

Create a `python_turtle_graphics.py` program and run it. When it's done drawing, you should see 100 overlapping colorful circles arranged in a spiral pattern on a black background.

Then try tweaking these values and see what happens:
- Change `range(100)` to `range(50)` or `range(200)`
- Change `t.circle(100)` to `t.circle(50)` or `t.circle(150)`
- Change `t.left(36)` to `t.left(45)` or `t.left(60)`
- Change `"Black"` to `"White"`

Each change produces a completely different pattern. That's the fun part. 🎨

## Solved Exercise:

```py
# python_turtle_graphics.py

import turtle, colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("Black")
h = 0

for _ in range(100):
    t.color(colorsys.hsv_to_rgb(h, 1, 1))
    t.circle(100)
    t.left(36)
    h += 0.1

t.hideturtle()
turtle.done()
```

> [!TIP]
> Turtle graphics runs in its own window. If the window doesn't appear, check that nothing is blocking it behind VS Code. On some systems you may need to click the taskbar icon to bring it to the front.

---

# Chapter 4 — Complete! 🎉

You covered a lot:
- `while` loops for repeating while a condition is true
- `for` loops with `range()` for fixed repetitions
- f-strings for embedding variables in text
- `%` modulo for divisibility checks
- Iterating over strings character by character
- Importing multiple modules
- Building visual output with `turtle`

Next: **Chapter 5 — First Project: Rock Paper Scissors** 🎮 Time to build something real.
