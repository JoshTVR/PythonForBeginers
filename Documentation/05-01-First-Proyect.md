# Chapter 5 — First Project: Rock Paper Scissors 🎮

Congratulations on completing the first four chapters of The Legend of Python! Variables, control flow, loops — you've got all the building blocks. Now let's combine everything and build a real program.

This is your first checkpoint project. No hand-holding — just a project brief, the concepts you've learned, and your own problem-solving. 🧠

---

# Rock Paper Scissors

Rock, Paper, Scissors is a classic game played worldwide. Two players simultaneously reveal one of three shapes — the rules determine the winner.

The rules:
- Rock beats Scissors ✊ > ✌️
- Scissors beat Paper ✌️ > ✋
- Paper beats Rock ✋ > ✊

---

# Planning Before Coding

Before writing a single line, let's think about the logic. This is how real developers work — plan first, code second.

The program needs to:
1. Show the player the 3 options
2. Get the player's choice (1, 2, or 3)
3. Generate a random choice for the computer
4. Compare the two choices
5. Print who won

The tricky part is step 4. There are 9 possible combinations (3 × 3). Let's map them all out:

| User | CPU | Result |
|------|-----|--------|
| 1 Rock | 1 Rock | Tie |
| 1 Rock | 2 Paper | CPU wins |
| 1 Rock | 3 Scissors | User wins |
| 2 Paper | 1 Rock | User wins |
| 2 Paper | 2 Paper | Tie |
| 2 Paper | 3 Scissors | CPU wins |
| 3 Scissors | 1 Rock | CPU wins |
| 3 Scissors | 2 Paper | User wins |
| 3 Scissors | 3 Scissors | Tie |

From this table we can extract the conditions:

**User wins when:**
- `user == 1 and cpu == 3` (Rock beats Scissors)
- `user == 2 and cpu == 1` (Paper beats Rock)
- `user == 3 and cpu == 2` (Scissors beats Paper)

**CPU wins:** all other non-tie combinations.

**Tie:** `user == cpu`

Map the logic out *before* typing code. It saves so much debugging time.

---

## Instructions

Create a `Rock-Paper-Scissors.py` program where:

1. The player picks a number (1 = Rock, 2 = Paper, 3 = Scissors)
2. The computer picks a random number (1–3) using `random.randint()`
3. The program determines the winner using `if/elif/else`
4. Prints the result

Expected output:

```
1) ✊
2) ✋
3) ✌️
Pick a number: 2

You chose: ✋
CPU chose: ✊
You win!
```

## Solved Exercise:

```py
# Rock-Paper-Scissors.py

import random

user_choice = int(input('1) ✊\n2) ✋\n3) ✌️\nPick a number: '))
cpu = random.randint(1, 3)

if user_choice < 1 or user_choice > 3:
    print('Invalid choice!')
elif user_choice == cpu:
    print('Tie! Try again.')
elif (user_choice == 1 and cpu == 3) or \
     (user_choice == 2 and cpu == 1) or \
     (user_choice == 3 and cpu == 2):
    print('You win! 🎉')
else:
    print('CPU wins! 🤖')

print(f'Your choice: {user_choice} | CPU: {cpu}')
```

---

# Bonus: Rock Paper Scissors Lizard Spock

You've played Rock Paper Scissors, but have you heard of Rock Paper Scissors Lizard Spock? 🖖🦎

It's a variation made popular by the TV show *The Big Bang Theory*. The inventor, Sam Kass, created it because:

> "When you know someone well enough, 75-80% of Rock Paper Scissors games end in a tie. This version reduces that probability."

The rules add 4 more outcomes to the original:

- Rock crushes Lizard 🪨 > 🦎
- Lizard poisons Spock 🦎 > 🖖
- Spock smashes Scissors 🖖 > ✌️
- Scissors decapitate Lizard ✌️ > 🦎
- Lizard eats Paper 🦎 > ✋
- Paper disproves Spock ✋ > 🖖
- Spock vaporizes Rock 🖖 > ✊
- (plus the original 6 rules)

Now there are 25 possible combinations (5 × 5). Writing 25 `elif` conditions gets messy fast.

The clean approach: use the logic tables to list exactly which combinations make each player win, same as above.

The full outcome table:

| Symbol | Beats |
|--------|-------|
| 1 ✊ Rock | 3 ✌️ Scissors, 4 🦎 Lizard |
| 2 ✋ Paper | 1 ✊ Rock, 5 🖖 Spock |
| 3 ✌️ Scissors | 2 ✋ Paper, 4 🦎 Lizard |
| 4 🦎 Lizard | 2 ✋ Paper, 5 🖖 Spock |
| 5 🖖 Spock | 1 ✊ Rock, 3 ✌️ Scissors |

## Solved Exercise:

```py
# Rock-Paper-Scissors-Lizard-Spock.py

import random

user = int(input('1) ✊  2) ✋  3) ✌️  4) 🦎  5) 🖖\nPick: '))
cpu = random.randint(1, 5)

# Winning combinations (user_choice, cpu_choice)
user_wins = [
    (1, 3), (1, 4),    # Rock beats Scissors, Lizard
    (2, 1), (2, 5),    # Paper beats Rock, Spock
    (3, 2), (3, 4),    # Scissors beats Paper, Lizard
    (4, 2), (4, 5),    # Lizard beats Paper, Spock
    (5, 1), (5, 3)     # Spock beats Rock, Scissors
]

if user < 1 or user > 5:
    print('Invalid choice!')
elif user == cpu:
    print("It's a tie!")
elif (user, cpu) in user_wins:
    print('You win! 🎉')
else:
    print('CPU wins! 🤖')

print(f'You: {user} | CPU: {cpu}')
```

> [!TIP]
> When you have this many combinations, storing them in a list of tuples is much cleaner than a long `if/elif` chain. When you learn dictionaries in Chapter 8, there's an even neater way to handle this. 👀

---

Chapter 5 done! 🎮 Next: **Chapter 6 — Lists**. One of Python's most powerful data structures.
