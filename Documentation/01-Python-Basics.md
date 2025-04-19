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

Claro, aquí tienes el contenido adicional incorporado directamente al documento en Markdown respetando el mismo formato original:

---

### Currency Conversion (South America Trip Example)

We just got home from a fun trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

- 🇨🇴 Colombian pesos
- 🇵🇪 Peruvian soles
- 🇧🇷 Brazilian reais

Create a `currency.py` program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

Make sure to Google the current exchange rates!

```python
co = int(input('What do you have left in Colombian pesos?? '))
pe = int(input('What do you have left in Peruvian soles?? '))
br = int(input('What do you have left in Brazilian reais?? '))

# Exchange rates as of the time the program was written
cousd = co * 0.0002319
peusd = pe * 0.2685
brusd = br * 0.1722

leftovers = cousd + peusd + brusd

print(leftovers)
```

---

### Recap of Python Basics

- **Data types**: `int`, `float`, `str`, `bool`
- **Arithmetic operators**: `+`, `-`, `*`, `/`
- The `%` modulo finds the remainder
- The `**` exponentiation finds the exponent
- The `input()` function gets user input
- The `int()` function converts values into integers

---

### Decision Making (Introduction)

So far, every Python program we've encountered has only had one path of execution:  
they all execute one line at a time, from top to bottom. Every time you run them, it gives you the same result.

Sometimes, we want our program to do different things based on different conditions.

We will explore how programs "make decisions" by evaluating different conditions and start introducing logic into our code!

Before we dive deep into something called an **if statement**, let's do a fun demo using a coin flip simulation!

We will learn more about `random` and `.randint()` later in the chapter.

All you need to know is that this program simulates a coin toss:

- 50% of the time, it's "Heads".
- 50% of the time, it's "Tails".

Run the program 5 times to get a taste of the `if/else` statement!

How many times did it go Heads?

```python
import random

num = random.randint(0, 1)   # Generates either 0 or 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')
```

---

### Grades Example (`grades.py`)

Create a `grades.py` program that checks whether a grade is above or below 55.

Start by creating a variable called `grade` and give it a value between 0-100.

Write an `if/else` statement:

- If grade ≥ 55, print "You passed."
- Else, print "You failed."

After you run the code, change `grade`'s value and rerun it.

```python
grade = int(input('What is the grade temperature?? '))

if grade >= 55:
  print("You passed.")
else:
  print("You failed.")
```

---

### pH Levels (`ph_levels.py`)

Create a program `ph_levels.py` to check whether a pH level is basic, acidic, or neutral.

Ask the user for a value between 0 and 14:

- If ph > 7, output "Basic".
- If ph < 7, output "Acidic".
- Else, output "Neutral".

```python
ph = int(input('What is the ph?? '))

if ph > 7:
  print('The ph is Basic')
elif ph < 7:
  print("The ph is Acidic")
else:
  print('The ph is Neutral')
```

---

### Random Numbers (`random` module)

We can use the `.randint()` function from the Python `random` module to generate a random number from a range.

```python
import random

num = random.randint(1, 9)
print(num)
```

This generates a random number between 1 and 9 (inclusive).

---

### Magic 8 Ball (`magic8.py`)

The Magic 8 Ball is a popular toy used for fortune-telling and advice-seeking.

Create a `magic8.py` program that responds to Yes or No questions with a random answer each time:

```python
import random

input('Make a question for the MAGIC 8 BALL!!!! ')
num = random.randint(1, 9)
if num == 1:
  print('Yes - definitely.')
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
```

---

### Logical Operators

Logical operators (`and`, `or`, `not`) combine conditions:

- `and`: Both conditions must be True.
- `or`: At least one condition must be True.
- `not`: Inverts the truth value.

Example:

```python
if hunger > 4 and anger > 1:
  print('Hangry')

if coffee > 0 or bubble_tea > 0:
  print('😊')

if not tired:
  print('Time to code!')
```

---

### The Cyclone Roller Coaster (`the_cyclone.py`)

Visitors must be at least 137 cm and pay 10 credits to ride.

Create `the_cyclone.py` program:

```python
height = int(input('What is your height in cm??'))
credits = int(input('How many credits do you have??'))

if height < 137 and credits < 10:
  print('Your height and credits are insufficient')
elif height >= 137 and credits < 10:
  print("You don't have enough credits.")
elif height < 137 and credits >= 10:
  print('You are not tall enough to ride.')
else:
  print('Enjoy the ride!')
```

---

### Sorting Hat (`sorting_hat.py`)

Write a program to determine Hogwarts house assignments:

```python
G = 0
R = 0
H = 0
S = 0

Q1 = int(input('Q1) Do you like Dawn or Dusk? \n1) Dawn\n2) Dusk\n'))

if Q1 == 1:
  G += 1
  R += 1
  print('Gryffindor:', G, '\nRavenclaw:', R)
elif Q1 == 2:
  H += 1
  S += 1
  print('Hufflepuff:', H, '\nSlytherin:', S)
else:
  print('Wrong input')

Q2 = int(input('Q2) When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n'))

if Q2 == 1:
  H += 2
  print('Hufflepuff:', H)
elif Q2 == 2:
  S += 2
  print('Slytherin:', S)
elif Q2 == 3:
  R += 2
  print('Ravenclaw:', R)
elif Q2 == 4:
  G += 2
  print('Gryffindor:', G)
else:
  print('Wrong input')

Q3 = int(input('Q3) Which kind of instrument most pleases your ear?\n1) Violin\n2) Trumpet\n3) Piano\n4) Drum\n'))

if Q3 == 1:
  S += 4
  print('Slytherin:', S)
elif Q3 == 2:
  H += 4
  print('Hufflepuff:', H)
elif Q3 == 3:
  R += 4
  print('Ravenclaw:', R)
elif Q3 == 4:
  G += 4
  print('Gryffindor:', G)
else:
  print('Wrong input')
```

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
