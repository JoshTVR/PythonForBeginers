
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


a = int(input('What would be the first short a side? '))
b = int(input('What would be the second short b side? '))

c = ((a**2 + b**2)**0.5)
print(c)

