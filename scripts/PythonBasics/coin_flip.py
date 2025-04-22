
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

import random

num = random.randint(0, 1)   # Generates a random number that's either 0 or 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')

