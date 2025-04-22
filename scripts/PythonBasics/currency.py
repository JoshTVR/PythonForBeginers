"""
You've learned variables in Python!

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

co = int(input('What do you have left in Colombian pesos?? '))
pe = int(input('What do you have left in Peruvian soles?? '))
br = int(input('What do you have left in Brazilian reais?? '))

cousd = co * 0.0002319
peusd = pe * 0.2685
brusd = br * 0.1722

leftovers = cousd + peusd + brusd

print(leftovers)