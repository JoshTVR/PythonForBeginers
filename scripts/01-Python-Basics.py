
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


"""
Create a grades.py program that checks whether a grade is above or below 55.

Start by creating a variable called grade and give it a value between 0-100.

Write a if/else statement for the following:

If grade is greater than or equal to 55, then print "You passed."
Else, print "You failed."
After you run the code, change grade's value and rerun it. 
Do this a few times to make sure it's working as intended.
"""

"""
grade = int(input('What is the grade temperature?? '))

if grade >= 55:
  print("You passed.")
else:
  print("You failed.")
"""



"""
pH Levels

Relational Operators
A lot of the times inside conditions, we are comparing two values. To do so, we need to use a different type of operators called relational operators that compares values:

== equal to
!= not equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal to
"""

"""
Elif
One or more elif statements (short for "else if") can be optionally added in between the if and else to provide additional condition(s) to check. Sometimes two is simply not enough.

if grade > 90:
  print('A')
elif grade > 80:
  print('B')
elif grade > 70:
  print('C')
elif grade > 60:
  print('D')
else:
  print('F')

Note: Only one of these options will execute.
"""


"""
Instructions
In chemistry, pH is a scale used to specify the acidity or basicity of a liquid. 🧪

Create a ph_levels.py program that checks whether a pH level is basic, acidic, or neutral.

First, create a ph variable and ask the user for a value between 0 and 14.

Write an if, elif, else statement that:

If ph is greater than 7, output "Basic".
If ph is less than 7, output "Acidic".
Else, output "Neutral".
"""

"""
ph = int(input('What is the ph?? '))

if ph > 7:
  print('The ph is Basic')
elif ph < 7:
  print("The ph is Acidic")  
else:
  print('The ph is Neutral')
"""

"""
Random

In Python, modules are .py files containing Python code that can be imported inside another Python program.
The Python standard library contains well over 200 modules that we can use.

We can use the .randint() function from a module called random to generate a random number from a range.

But first, let's import this module so we can use its functions.


import random

Next, we'll create a variable to store the randomly generated value. Declare a variable called num, 
and assign it to the function call:

num = random.randint(1, 9)

This will generate a random number between 1 and 9 (inclusive of both).

Together, the code will look like:

import random

num = random.randint(1, 9)

print(num)

Try running this code! ☝️

The output should be different each time it runs: 2, 8, 5, 9, 2, 1, 3...
"""

"""
Instructions
The Magic 8 Ball is a popular office toy and children's toy invented in the 1940s for fortune-telling and advice seeking. 🎱

It's an oversized 8 ball with some of the following answers:

Yes - definitely.
It is decidedly so.
Without a doubt.
Reply hazy, try again.
Ask again later.
Better not tell you now.
My sources say no.
Outlook not so good.
Very doubtful.

Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.

The output should have the following format:
"""
"""
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
  
"""





"""
Logical Operators
One more thing that we should learn is logical operators.

Logical operators, also known as Boolean operators, combine and evaluate two conditions. 
They are and, or, and not operators:

and returns True if both conditions are True, and returns False otherwise.
or returns True if at least one of the conditions is True, and False otherwise.
not returns True if the condition is False, and vice versa.

Here are some examples:

if hunger > 4 and anger > 1:
  print('Hangry')
  
If the hunger variable is greater than 4 and the anger variable is greater than 1, 
then the program prints "Hangry".

if coffee > 0 or bubble_tea > 0:
  print('😊')
  
If the coffee variable is greater than 0 or the bubble_tea variable is greater than 0, 
then the program prints a smiley face.

if not tired:
  print('Time to code!')
  
If the tired variable is not True, then the program prints "Time to code!"

So you might be wondering: and and or are awfully similar, 
how do I remember the differences between the two?

 Let's break this down in a table form:

A	B	A and B	A or B
False	False	False	False
False	True	False	True
True	False	False	True
True	True	True	True
"""


"""
Instructions

Since 1927, "The Cyclone" roller coaster has delighted visitors at Coney Island (Brooklyn, NY). 🎢

They're now installing a new entry system (the height requirement is 137 cm and the cost is 10 credits) and need your help writing the program for it!

Create a new file called the_cyclone.py.

Ask the user what their height is and how many credits they have, and store the values in a height variable and a credits variable.

Use a combination of relational and logical operators to create the rules:

If they are tall enough and have enough credits, print "Enjoy the ride!"
Else if they have enough credits, but they aren't tall enough, print "You are not tall enough to ride."
Else if they are tall enough, but they don't have enough credits, print "You don't have enough credits."
Else, print a message saying they have not met either requirement.
"""
"""
height = int(input('What is your height in cm??'))
credits = int(input('How many credits do you have??'))

if height < 137 and credits < 10:
  print('Your height and credits are insufficient')
elif height > 137  and credits < 10:
  print('You don\'t have enough credits.')
elif height < 137 and credits > 10:
  print('You are not tall enough to ride.')
else:
  print('Enjoy the ride!')
"""
  
"""
Here's a recap of everything we learned so far:

Control flow is the order in which the program's code executes.
if statement tests a condition for truth and executes the code if it's True.
elif clause can be added between if and else.
else executes the code if none of the above is True.
Relational operators are used to compare two values: ==, !=, >, >=, <, <=.
Logical operators are used to combine two or more conditions: and, or, not.
Here's an if/elif/else statement in action just in case:

if review >= 4.5:
  print('Extraordinary')
elif review >= 4:
  print('Excellent')
elif review >= 3:
  print('Good')
else:
  print('Eh')
"""  

"""
Instructions

The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

🦁 Gryffindor
🦅 Ravenclaw
🦡 Hufflepuff
🐍 Slytherin


Write a program that asks the user some questions with the int() and input() functions:

Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk

If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
Else, output the message "Wrong input."
Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold

If the answer is 1, Hufflepuff +2.
Else if answer is 2, Slytherin +2.
Else if answer is 3, Ravenclaw +2.
Else if answer is 4, Gryffindor +2.
Else, output the message "Wrong input."
Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum

If the answer is 1, Slytherin +4.
Else if the answer is 2, Hufflepuff +4.
Else if the answer is 3, Ravenclaw +4.
Else if the answer is 4, Gryffindor +4.
Else, output "Wrong input."
Lastly, print out the score for each house.

Bonus: If you want to go further, see if you can figure out how to print out the house with the most points!s
"""

G = 0
R = 0
H = 0
S = 0


Q1 = int(input('Q1) Do you like Dawn or Dusk? \n'
    '1) Dawn \n'
    '2) Dusk \n'))

if Q1 == 1:
  G = G + 1
  R = R + 1
  print('Griffindor = ',G,'\n Ravenclaw = ',R)
elif Q1 == 2:
  H = H + 1
  S = S + 1
  print('Hufflepuff = ',H,'\n Slytherin = ',S)
else:
  print('Wrong input')

Q2 = int(input('Q2) When I’m dead, I want people to remember me as: \n'
    '1) The Good \n'
    '2) The Great \n'
    '3) The Wise \n'
    '4) The Bold \n'))

if Q2 == 1:
  H = H + 2
  print('Hufflepuff = ',H)
elif Q2 == 2:
  S = S + 2
  print('Slytherin = ',S)
elif Q2 == 3:
  R = R + 2
  print('Ravenclaw = ',R)
elif Q2 == 4:
  G = G + 2
  print('Griffindor = ',G)
else:
  print('Wrong input')

Q3 = int(input('Q3) Which kind of instrument most pleases your ear? \n'
    '1) The violin \n'
    '2) The trumpet \n'
    '3) The piano \n'
    '4) The drum \n'))
  
if Q3 == 1:
  S = S + 4
  print('Slytherin = ',S)
elif Q3 == 2:
  H = H + 4
  print('Hufflepuff = ',H)
elif Q3 == 3:
  R = R + 4
  print('Ravenclaw = ',R)
elif Q3 == 4:
  G = G + 4
  print(G)
else:
  print('Wrong input')
  