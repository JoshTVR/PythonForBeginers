# Python

Welcome to the first chapter of The Legend of Python! 🐍

The programming language we're learning is called Python, created by a developer named Guido van Rossum in 1991. The name? Not from the snake — from the British comedy group Monty Python. Guido wanted something fun.

Python is designed to be easy to read, which makes it the perfect first language. Seriously, compare it to Java or C++ and you'll see what I mean — Python almost reads like English.

It's also incredibly versatile. Here's what people build with it:

- 🤖 AI & Machine Learning
- 📊 Data analysis & visualization
- 🌐 Web development (Instagram, Spotify, and YouTube all use Python backends)
- 🔬 Scientific computing
- 🎮 Game scripting

All the code we write will go in `.py` files — Python files. We write and run them inside a code editor. If you haven't set up VS Code yet, download it from [code.visualstudio.com](https://code.visualstudio.com) and install the Python extension.

---

# Hello World

The first program every developer writes. It's basically a rite of passage. 🙌

Create a file called `hello_world.py` and add this:

```py
print('Hello World!')
```

Run it in the terminal:

```
python hello_world.py
```

You should see:

```
Hello World!
```

![Hello World running in VS Code](../PythonBasics/imgs/HelloWorld.png)

The `print()` function outputs text to the console. The text goes inside parentheses, wrapped in single `' '` or double `" "` quotes. Both work — pick one and be consistent.

---

# Printing Multiple Lines

Python runs top-to-bottom, one line at a time. So multiple `print()` calls print multiple lines:

```py
print('🌻 Morning!')
print('🙋 Evening!')

# Output:
# 🌻 Morning!
# 🙋 Evening!
```

You can also print patterns by carefully spacing your output:

```py
print('       1')
print('     2 3')
print('   4 5 6')
print('7 8 9 10')

# Output:
#        1
#      2 3
#    4 5 6
# 7 8 9 10
```

Each `print()` starts on a new line automatically.

---

# Comments

Comments are notes you leave in your code — for yourself, for teammates, for future-you who completely forgot what this script does. Python ignores them when running the program.

A single-line comment starts with `#`:

```py
# This is a comment
print('Hello')   # This is also a comment
```

A multi-line comment uses triple quotes `"""`:

```py
"""
This is a multi-line comment.
It can span as many lines as you want.
Python ignores all of this.
"""
print('Still prints!')
```

Honestly, comments are like leaving sticky notes for future-you. Your code might make perfect sense *now*. Three months from now? Not so much. Comment as you go.

---

## Instructions

Create a `hello_world.py` program that:

1. Prints `"Hello World!"` to the console
2. Adds at least one comment explaining what the program does

## Solved Exercise:

```py
# hello_world.py
# This script prints a greeting to the console

print('Hello World!')

# Output: Hello World!
```

---

## Instructions 2

Print your initials using multiple `print()` statements to form a letter pattern.

For example, the letter `J`:

```
JJJJJJJJJJJ
     J
     J
     J
JJJJJJ
```

## Solved Exercise:

```py
# initials.py

print('JJJJJJJJJJJ')
print('     J     ')
print('     J     ')
print('     J     ')
print('JJJJJJ     ')

# Output:
# JJJJJJJJJJJ
#      J
#      J
#      J
# JJJJJJ
```

![First Python program running](../PythonBasics/imgs/FirstPythonProgram.png)

---

# Recap

- Python was created by Guido van Rossum in 1991.
- Python files use the `.py` extension.
- `print()` outputs text to the console.
- Quotes: single `' '` and double `" "` both work.
- Comments: `#` for single-line, `"""..."""` for multi-line.
- Python runs top-to-bottom, one line at a time.

You just completed your first canon event! 🎉 Next: **Chapter 2 — Variables**. Time to actually store some data.
