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

Happy coding!
