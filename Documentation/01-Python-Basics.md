# Process Number One

### Learning How Python Interacts with the User via the Console

I'd like to discuss this briefly, as it's often one of the initial \"canon events\" every developer experiences when learning a new programming language.

Here's a simple example of interacting with Python through the console:

```python
# Python Language :D
print('Hello World!')
```

This is essentially the first step you'll take in Python. To see this in action, simply click the \"Run\" button. After waiting just 1-2 seconds, you should see your first Python message appear. Congratulations, you've just completed your first canon event!

The expected output in the Terminal window:

```
Hello World
```

---

### First Step to Learn Python

My first Python script contains a simple print statement. This script prints \"Hello World\" to the console.

```python

print('Hello World!')

# The output of this example program would be:

# Hello World!

"""
The print() function is used to output text to the console.
The text to be printed is enclosed in single or double quotes.
The print() function can also be used to print numbers, variables, and other data types.
"""
```

Python is run one line at a time, from top to bottom. You can output multiple messages using multiple print() functions.

Example:

```python
print('🌻 Morning Dharma!')
print('🙋🏽 Evening Sonny!')

# Output:
# 🌻 Morning Dharma!
# 🙋🏽 Evening Sonny!
```

You can also format output exactly as you desire:

```python
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

### How Do I Comment in Python?

- Comments are preceded by a hash (#) symbol.
- Comments are ignored by the Python interpreter.
- Comments are useful for explaining code and making it more readable.
- Single-line comments start with #.
- Multi-line comments can be created using triple quotes (`'''` or `"""`).

Example:

```python
# print('Hi')   # I'm a comment, too!

# Example of multi-line comment:
"""
This is a
multi-line comment
"""
```

---

### Data Types

#### Variables

Variables store data values. Variable names consist of letters, numbers, and underscores.

Examples:

```python
name = 'Erlich Bachman'
user_id = 16180339887
progress = 0.75
exp = 60
verified = True
```

You can also change or print variable values:

```python
xp = 70
xp = 80
print(xp)  # Output: 80
```

#### Integer

Whole numbers without decimal points:

```python
year = 2023
age = 32
```

#### Float

Decimal numbers:

```python
pi = 3.14159
meal_cost = 12.99
```

#### String

Text values enclosed in quotes:

```python
message = "good nite"
username = '@snoopdogg'
```

#### Boolean

True or False values:

```python
late_to_class = False
cranky = True
```

---

### Operators

Python supports various arithmetic operators:

- Addition (+)

- Subtraction (-)

- Multiplication (\*)

- Division (/)

- Modulo (%) - returns the remainder

```python
score = 4 + 3  # 7
score = 4 - 3  # 1
score = 4 * 3  # 12
score = 4 / 3  # 1.3333
score = 4 % 3  # 1
```

Example calculating a tip:

```python
pizza = 2.99
coke = 0.99
tip = (pizza + coke) * 0.2
print(tip)  # Output: 0.796
```

---

### Temperature Conversion

Convert Fahrenheit to Celsius:

```python
F = -459.67
C = (F - 32) * 5/9
print(C)  # Output: -273.15 °C
```

---

### Exponents

Exponentiation using \*\*:

```python
score = 2 ** 5
print(score)  # Output: 32
```

---

### Body Mass Index (BMI)

Calculate BMI:

```python
bmi = 67.600 / (1.76 ** 2)
print(bmi)  # Output: 22.86
```

---

### User Input

Thus far, we've only been outputting things to the user, making our programs one-sided and not that fun. Almost every popular website, mobile app, or video game nowadays has both input and output.

Python uses the `input()` function to get user input:

```python
username = input('Enter your name: ')
print('Your name is: ' + username)
```

The output will say "Enter your name: " and the user can type in something, hit enter, and whatever the user typed gets stored into the `username` variable.

By default, the user input is stored as a text string, which is okay for now. If a numeric input is required, use `int()`:

```python
age = int(input('What is your age? '))
print(age)
```

### Pythagorean Theorem

The Pythagorean theorem describes the relationship between the sides of a right triangle:

```python
a = int(input('What would be the first short a side? '))
b = int(input('What would be the second short b side? '))

c = ((a**2 + b**2)**0.5)
print(c)
```

### Currency Conversion

Let's create a program to convert leftover currency to USD:

```python
co = int(input('What do you have left in Colombian pesos?? '))
pe = int(input('What do you have left in Peruvian soles?? '))
br = int(input('What do you have left in Brazilian reais?? '))

cousd = co * 0.0002319
peusd = pe * 0.2685
brusd = br * 0.1722

leftovers = cousd + peusd + brusd
print(leftovers)
```

### Decision Making with If/Else Statements

Let's simulate a coin flip:

```python
import random

num = random.randint(0, 1)

if num > 0.5:
  print('Heads')
else:
  print('Tails')
```

---

### Recap of Python Basics

- **Data types**: `int`, `float`, `str`, `bool`
- **Arithmetic operators**: `+`, `-`, `*`, `/`
- The `%` modulo finds the remainder
- The `**` exponentiation finds the exponent
- The `input()` function gets user input
- The `int()` function converts values into integers

Happy coding!

---

### String Manipulation

Python provides various methods to manipulate strings, including concatenation, slicing, and formatting:

```python
first_name = "Richard"
last_name = "Hendricks"
full_name = first_name + " " + last_name
print(full_name)  # Output: Richard Hendricks

# Slicing strings
print(full_name[:7])  # Output: Richard
print(full_name[-9:])  # Output: Hendricks
```

String formatting example:

```python
age = 25
intro = f"My name is {full_name} and I am {age} years old."
print(intro)
# Output: My name is Richard Hendricks and I am 25 years old.
```

---

### Lists

Lists are collections of items that can store different data types:

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
```

Lists can be modified:

```python
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
```

---

### Conditional Statements

Python uses conditional statements (`if`, `elif`, `else`) to make decisions:

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# Output: Grade: B
```

---

### Loops

Loops help to execute code repeatedly.

#### For Loop

```python
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
# orange
```

#### While Loop

```python
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# Output:
# Count is: 0
# Count is: 1
# Count is: 2
```

---

### Functions

Functions encapsulate reusable code blocks:

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Dinesh")
print(message)  # Output: Hello, Dinesh!
```

---

### Importing Modules

Python allows importing external libraries:

```python
import math

print(math.sqrt(16))  # Output: 4.0
```

---

### Handling Errors (Try/Except)

Python handles exceptions gracefully using `try` and `except`:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Output: Cannot divide by zero!
```

---

### Final Thoughts

With these fundamentals, you're equipped to write and understand basic Python scripts. Keep exploring, coding, and having fun!
