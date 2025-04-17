
"""
First step to learn Python
my first Python script contains a simple print statement
This script prints "Hello World" to the console
"""

# print('Hello World!')
# The output of this example program would be:
# Hello World!
# The print() function is used to output text to the console.
# The text to be printed is enclosed in single or double quotes.
# The print() function can also be used to print numbers, variables, and other data types.

# Python is run one line at a time, from top to bottom.
# We can output multiple messages by using multiple print() functions. 
# For example, if we want to print out two simple greetings:
"""
print('🌻 Morning Dharma!')
print('🙋🏽 Evening Sonny!')

# This will output:

🌻 Morning Dharma!
🙋🏽 Evening Sonny!
"""
# Suppose we want the output to look exactly like this pattern below:
"""
       1
     2 3
   4 5 6
7 8 9 10
"""

# We can achieve this by using the print() function with the appropriate formatting.
# The following code will print the desired pattern:
"""
print('       1')
print('     2 3')
print('   4 5 6')
print('7 8 9 10')
"""

# The output of this example program would be:
"""
       1
     2 3
   4 5 6
7 8 9 10
"""

"""
how do i comment in Python?
comments are preceded by a hash (#) symbol
comments are ignored by the Python interpreter
comments are useful for explaining code and making it more readable
comments can be single-line or multi-line
single-line comments start with a # symbol
"""
# multi-line comments can be created using triple quotes (''' or """)
"""
multi-line comments can span multiple lines
multi-line comments are useful for documenting code and providing detailed explanations about the code
multi-line comments are ignored by the Python interpreter
"""
"""
Comments are very important in programming because they are used to document what our code does. 
They are also used to disable parts of the program.

When the program is run, the comments are ignored.

In Python, we can create a comment using the # hashtag symbol:
"""
# to declare a # in Python, you can use the escape character (\) before the # symbol
# for example, to declare a # in a string, you can use the following syntax: 
# my_string = 'This is a # symbol'
# or you can use double quotes:
# my_string = "This is a # symbol"
# or you can use triple quotes:
# my_string = '''This is a # symbol'''

# print('Hi')   # I'm a comment, too!

# Data Types
"""
Variables
In programming, variables are used for storing data values. 
Each variable has a name and holds a value. 📦
The variable name can consist of letters, numbers, and the _ underscore.

These are all valid variable names and values:

name = 'Erlich Bachman'
user_id = 16180339887
progress = 0.75
exp = 60
verified = True

The = equal sign means assignment:
We're assigning the string value 'Erlich Bachman' to the variable name.
We're assigning the number value 16180339887 to the variable user_id.
We're assigning the number value 0.75 to the variable progress.
We're assigning the number value 60 to the variable exp.
We're assigning the truth value True to the variable verified.

We can also change the value of a variable, or print it out:

xp = 70
xp = 80

print(xp)    # Output: 80

Data Types

Integer
An integer, or int, is a whole number. It has no decimal point and contains the number 0, positive and negative counting numbers. 
If we were counting the number of people on the bus or the number of jellybeans in a jar, we would use an integer.

year = 2023
age = 32

Float
A floating-point number, or a float, is a decimal number. It can be used to represent fractions or precise measurements. 
If you were measuring the length and width of the couch, calculating the test score percentage, 
or storing a baseball player’s batting average, we would use a float instead of an int.

pi = 3.14159
meal_cost = 12.99

String
A string, or str, is used for storing text. 
Strings are wrapped in double quotes " " or single quotes ' '.

message = "good nite"
username = '@snoopdogg'

Boolean
A Boolean data type, or bool, stores a value that can only be either true or false. In Python, it's capitalized True or False. 
It's named after the British mathematician George Boole (1815-1864).

late_to_class = False
cranky = True
"""

"""
Operators

Computers are incredible at doing math calculations. 
Now that we have learned about variables, let's use them with arithmetic operators to calculate things! 🔢

Python has the following arithmetic operators:

+ Addition
- Subtraction
* Multiplication
/ Division
% Modulo (returns the remainder)

score = 0           # score is 0
score = 4 + 3       # score is now 7
score = 4 - 3       # score is now 1
score = 4 * 3       # score is now 12
score = 4 / 3       # score is now 1.3333
score = 4 % 3       # score is now 1

print(score)        # Output: 1

And take a look at this code that calculates a 20% tip by calculating
the total and then multiplying by a float (decimal number):

pizza = 2.99
coke = 0.99

total = pizza + coke

tip = total * 0.2

print(tip) # Output: 0.796

Another way to write this is using parentheses to calculate the total and the tip in one line of code:

tip = (pizza + coke) * 0.2
"""

"""
Instructions
Create a temperature.py program that converts
a number from Fahrenheit (°F) to Celsius (°C).
Use the following formula and write it out in Python:

C = (F - 32) * 5/9

Print out the converted temperature.
"""

# temperature.py
# This program converts Celsius to Fahrenheit:
"""
F = -459.67  # Fahrenheit temperature
C = (F - 32) * 5/9
print(C)
# Output: -273.15 °C
"""

"""
Exponents
Python can also perform exponentiation such as 2³ or 10².

In written math, we might see an exponent as a superscript number (like above), but typing superscripts isn't always easy on modern keyboards. Since exponentiation is super similar to multiplication, Python uses the notation **.

So 2 ** 3 is 2³ and 10 ** 2 is 10².

Here are more examples:

score = 2 ** 2      # score is 4
score = 2 ** 3      # score is now 8
score = 2 ** 4      # score is now 16
score = 2 ** 5      # score is now 32

print(score)        # Output: 32
"""

"""
Instructions
The body mass index (BMI) was created by a Belgian mathematician in the 1850s and it's used 
by health and nutrition professionals to estimate human body fat in certain populations.

It is computed by taking an individual's weight (mass) in kilograms and 
dividing it by the square of their height in meters.
The formula is:

bmi = weight / height²
"""
"""
bmi = 67.600 / (1.76 ** 2)  # weight in kg, height in m
print(bmi)  # Output: 22.86
"""

""""
User Input
Thus far, we've only been outputting things to the user, making our programs one-sided and not that fun. Almost every popular website, mobile app, or video game nowadays have both input and output.

So how do we get input from the user?

Python uses the input() function to get user input:

username = input('Enter your name: ')

print('Your name is: '+ 
      username)

The output will say "Enter your name: " and the user can type in something, 
hit enter, and whatever the user typed gets stored into the username variable.

So here, suppose the user typed in their name and pressed enter, 
it will output their name.


int()
By default, the user input is stored as a text string, which is okay for now.

But what about when we want to get a number from a user?

In that case, we would need to wrap an int() around the input() 
to convert the text string into a number:


age = int(input('What is your age? '))

print(age)

Now that the user types 24 and presses enter, the age variable 
will be an integer 24, not a text string "24".
"""

"""
If you slept through your geometry class, a Pythagorean theorem is the relationship between the three sides 
of a right triangle. It was named after the Greek philosopher Pythagoras, born around 570 BC.

Pythagorean equation looks like:

c = ((a**2 + b**2)**0.5)

The a is the length of a short side.
The b is the length of another short side.
The c is the length of the hypotenuse.
"""

"""
a = int(input('What would be the first short a side? '))
b = int(input('What would be the second short b side? '))

c = ((a**2 + b**2)**0.5)
print(c)
"""
"""
You learned variables in Python!

Here's a recap of everything we learned in this chapter:

Data types: int, float, str, bool.
Arithmetic operators: +, -, *, /.
The % modulo finds the remainder.
The ** exponentiation finds the exponent.
The input() function is used to get user input.
The int() function converts a value into an integer number.
Let's put it all together now!

We just got home from a fun trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

🇨🇴 Colombian pesos
🇵🇪 Peruvian soles
🇧🇷 Brazilian reais
Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

Make sure to Google the current exchange rates!
"""
"""
co = int(input('What do you have left in Colombian pesos?? '))
pe = int(input('What do you have left in Peruvian soles?? '))
br = int(input('What do you have left in Brazilian reais?? '))

cousd = co * 0.0002319
peusd = pe * 0.2685
brusd = br * 0.1722

leftovers = cousd + peusd + brusd

print(leftovers)
"""

"""
So far, every Python program we've encountered has only had one path of execution
they all execute one line at a time, from top to bottom. Every time you run them, it gives you the same result.

Sometimes, we want our program to do different things based on different conditions.

we will explore how programs "make decisions" by evaluating different conditions. 
And start introducing logic into our code!

Before we dive deep into something called an if statement, let's do a fun demo using a coin flip simulation!

We will learn more about random and .randint() later in the chapter.

All you need to know is that this program simulates a coin toss:

≈ 50% of the time, it's "Heads".
≈ 50% of the time, it's "Tails".

Run the program 5 times to get a taste of the if/else statement!

How many times did it go Heads?
"""


"""
import random

num = random.randint(0, 1)   # Generates a random number that's either 0 or 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')
"""

















""""
User Input
Thus far, we've only been outputting things to the user, making our programs one-sided and not that fun. Almost every popular website, mobile app, or video game nowadays have both input and output.

So how do we get input from the user?

Python uses the input() function to get user input:

username = input('Enter your name: ')

print('Your name is: '+ 
      username)

The output will say "Enter your name: " and the user can type in something, 
hit enter, and whatever the user typed gets stored into the username variable.

So here, suppose the user typed in their name and pressed enter, 
it will output their name.


int()
By default, the user input is stored as a text string, which is okay for now.

But what about when we want to get a number from a user?

In that case, we would need to wrap an int() around the input() 
to convert the text string into a number:


age = int(input('What is your age? '))

print(age)

Now that the user types 24 and presses enter, the age variable 
will be an integer 24, not a text string "24".
"""

"""
If you slept through your geometry class, a Pythagorean theorem is the relationship between the three sides 
of a right triangle. It was named after the Greek philosopher Pythagoras, born around 570 BC.

Pythagorean equation looks like:

c = ((a**2 + b**2)**0.5)

The a is the length of a short side.
The b is the length of another short side.
The c is the length of the hypotenuse.
"""

"""
a = int(input('What would be the first short a side? '))
b = int(input('What would be the second short b side? '))

c = ((a**2 + b**2)**0.5)
print(c)
"""
"""
You learned variables in Python!

Here's a recap of everything we learned in this chapter:

Data types: int, float, str, bool.
Arithmetic operators: +, -, *, /.
The % modulo finds the remainder.
The ** exponentiation finds the exponent.
The input() function is used to get user input.
The int() function converts a value into an integer number.
Let's put it all together now!

We just got home from a fun trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

🇨🇴 Colombian pesos
🇵🇪 Peruvian soles
🇧🇷 Brazilian reais
Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

Make sure to Google the current exchange rates!
"""
"""
co = int(input('What do you have left in Colombian pesos?? '))
pe = int(input('What do you have left in Peruvian soles?? '))
br = int(input('What do you have left in Brazilian reais?? '))

cousd = co * 0.0002319
peusd = pe * 0.2685
brusd = br * 0.1722

leftovers = cousd + peusd + brusd

print(leftovers)
"""

"""
So far, every Python program we've encountered has only had one path of execution
they all execute one line at a time, from top to bottom. Every time you run them, it gives you the same result.

Sometimes, we want our program to do different things based on different conditions.

we will explore how programs "make decisions" by evaluating different conditions. 
And start introducing logic into our code!

Before we dive deep into something called an if statement, let's do a fun demo using a coin flip simulation!

We will learn more about random and .randint() later in the chapter.

All you need to know is that this program simulates a coin toss:

≈ 50% of the time, it's "Heads".
≈ 50% of the time, it's "Tails".

Run the program 5 times to get a taste of the if/else statement!

How many times did it go Heads?
"""


"""
import random

num = random.randint(0, 1)   # Generates a random number that's either 0 or 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')
"""

