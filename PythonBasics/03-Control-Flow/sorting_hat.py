  
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


if G >= R and G >= H and G >= S:
  print('🦁 Gryffindor!')
elif R >= H and R >= S:
  print('🦅 Ravenclaw!')
elif H >= S:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')
  
  
  
  
  # Version 2:
  
  """
  # Sorting Hat 🧙‍♂️
# Codédex

gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('===============')
print('The Sorting Hat')
print('===============')

# ~~~~~~~~~~~~~~~ Question 1 ~~~~~~~~~~~~~~~

print('Q1) Do you like Dawn or Dusk?')

print('  1) Dawn')
print('  2) Dusk')

answer = int(input('Enter answer (1-2): '))

if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin +=1
else:
  print('Wrong input.')

# ~~~~~~~~~~~~~~~ Question 2 ~~~~~~~~~~~~~~~

print("\nQ2) When I'm dead, I want people to remember me as:")

print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
  hufflepuff += 2
elif answer == 2:
  slytherin += 2
elif answer == 3:
  ravenclaw += 2
elif answer == 4:
  gryffindor += 2
else:
  print('Wrong input.')

# ~~~~~~~~~~~~~~~ Question 3 ~~~~~~~~~~~~~~~

print('\nQ3) Which kind of instrument most pleases your ear?')

print('  1) The violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
  slytherin += 4
elif answer == 2:
  hufflepuff += 4
elif answer == 3:
  ravenclaw +=4
elif answer == 4:
  gryffindor += 4
else:
  print('Wrong input.')
  
print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)

# Bonus Part

most_points = max(gryffindor, ravenclaw, hufflepuff, slytherin)   # We'll learn about the max() function in Chapter 6

if gryffindor == most_points:
  print('🦁 Gryffindor!')
elif ravenclaw == most_points:
  print('🦅 Ravenclaw!')
elif hufflepuff == most_points:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')
  """