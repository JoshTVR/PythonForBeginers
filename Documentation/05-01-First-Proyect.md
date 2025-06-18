Checkpoint Project ⛳️
Congratulations on completing the first four chapters of The Legend of Python! Now let's use the skills you've learned (variables, control flow statements, and loops) to build a Python project on your own.

Use the Python Code Editor, Visual Studio Code, or your code editor of choice for this project.

Terminal and our three characters

# Rock Paper Scissors

Rock, Paper, Scissors is a classic game that resonates with folks from around the world.

Create a rock_paper_scissors.py program where the user plays a round of Rock, Paper, Scissors against the computer.

The rules are as follows:

Rock beats Scissors.
Scissors beat Paper.
Paper beats Rock.
First, create a player and a computer variable.

Prompt the player to select number between 1 and 3 with input() and store it in player:

1 is for '✊' (Rock).
2 is for '✋' (Paper).
3 is for '✌️' (Scissors).
Then, use the random.randint() method to assign a number to the computer variable (1 to 3).

Lastly, use control flow to compare the user's choice and the computer's choice, determine the winner, and print out who won.

The output should look something like this:

===================
Rock Paper Scissors
===================

1. ✊
2. ✋
3. ✌️
   Pick a number: 2

You chose: ✋
CPU chose: ✊
The player won!

# Bonus: Rock Paper Scissors Lizard Spock

Okay, you have played Rock, Paper, Scissors, but have you heard of Rock, Paper, Scissors, Lizard, Spock? It's a fun variation of the classic game brought to popularity with a TV show called The Big Bang Theory.

The rules follow the classic “Rock Paper Scissors” game, but with two new choices – “Lizard” and “Spock”:

Scissors cut Paper.
Paper covers Rock.
Rock crushes Lizard.
Lizard poisons Spock.
Spock smashes Scissors.
Scissors beat Lizard.
Lizard eats Paper.
Paper disproves Spock.
Spock vaporizes Rock.
Rock breaks Scissors.
Watch this video to understand it better.

Here's a note from the creator, Sam Kass:

“I invented this game because it seems like when you know someone well enough, 75-80% of any Rock Paper Scissors games you play with that person end up in a tie. Well, here is a slight variation that reduces that probability. This version is also nice because it satisfies the Law of Fives.”

Go back to your Rock Paper Scissors program and turn it into Rock Paper Scissors Lizard Spock!

Use '🖖' for "Spock" and '🦎' for "Lizard".

The output should look something like this:

================================
Rock Paper Scissors Lizard Spock
================================

1. ✊
2. ✋
3. ✌️
4. 🦎
5. 🖖
   Pick a number: 3

You chose: ✌️
CPU chose: ✌️
It's a tie!

```py
print("Welcome to my first project\n \n")


print("██████╗  ██████╗  ██████╗ ██╗  ██╗    ██████╗  █████╗ ██████╗ ███████╗██████╗     ███████╗ ██████╗██╗███████╗███████╗ ██████╗ ██████╗ ███████╗"
    "\n██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██╔════╝██╔════╝██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝"
    "\n██████╔╝██║   ██║██║   ██║█████╔╝     ██████╔╝███████║██████╔╝█████╗  ██████╔╝    ███████╗██║     ██║███████╗███████╗██║   ██║██████╔╝███████╗"
    "\n██╔══██╗██║   ██║██║   ██║██╔═██╗     ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗    ╚════██║██║     ██║╚════██║╚════██║██║   ██║██╔══██╗╚════██║"
    "\n██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ██║     ██║  ██║██║     ███████╗██║  ██║    ███████║╚██████╗██║███████║███████║╚██████╔╝██║  ██║███████║"
    "\n╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝\n \n")

user_choice = int(input("1) ✊"
                    "\n2) ✋"
                    "\n3) ✌️"
                    "\nPick a number to fight against the IA: "))

import random

num = random.randint(1, 3)


if user_choice > 3 or user_choice < 1:
    print("Thats not a correct answer")
    print(f'CPU choice: {num} \nUser Choice: {user_choice}')
elif num == user_choice:
    print("Its a tie, try it again")
    print(f'CPU choice: {num} \nUser Choice: {user_choice}')
elif user_choice == 3 and num !=1:
    print("You have defeted the IA by choosing scissors!! Cogratz!!")
    print(f'CPU choice: {num} \nUser Choice: {user_choice}')
elif user_choice == 2 and num !=3:
    print("You have defeted the IA by choosing paper!! Cogratz!!")
    print(f'CPU choice: {num} \nUser Choice: {user_choice}')
elif user_choice == 1 and num !=2:
    print("You have defeted the IA by choosing rock!! Cogratz!!")
    print(f'CPU choice: {num} \nUser Choice: {user_choice}')
elif num == user_choice:
    print("Its a tie, try it again")
    print(f'CPU choice: {num} \nUser Choice: {user_choice}')
elif num == 3 and user_choice !=1:
    print("Sorry, IA has destroyed you by choosing scissors...")
    print(f'CPU choice: {num} \nUser Choice: {user_choice}')
elif num == 2 and user_choice !=3:
    print("Sorry, IA has destroyed you by choosing paper...")
    print(f'CPU choice: {num} \nUser Choice: {user_choice}')
elif num == 1 and user_choice !=2:
    print("Sorry, IA has destroyed you by choosing rock...")
    print(f'CPU choice: {num} \nUser Choice: {user_choice}')
else:
    print("No winner for this round")
    print(f'CPU choice: {num} \nUser Choice: {user_choice}')
```

| User     | CPU      | Winner |
| -------- | -------- | ------ |
| Rock     | Rock     | Tie    |
| Rock     | Paper    | CPU    |
| Rock     | Scissors | User   |
| Paper    | Rock     | User   |
| Paper    | Paper    | Tie    |
| Paper    | Scissors | CPU    |
| Scissors | Rock     | CPU    |
| Scissors | Paper    | User   |
| Scissors | Scissors | Tie    |

With numbers (like your code):

| user_choice | cpu_choice | Result |
| ----------- | ---------- | ------ |
| 1           | 1          | Tie    |
| 1           | 2          | CPU    |
| 1           | 3          | User   |
| 2           | 1          | User   |
| 2           | 2          | Tie    |
| 2           | 3          | CPU    |
| 3           | 1          | CPU    |
| 3           | 2          | User   |
| 3           | 3          | Tie    |

---

### How to use it:

- **Tie:** `user_choice == cpu_choice`
- **User wins:**

  - `(user_choice == 1 and cpu_choice == 3)`
  - `(user_choice == 2 and cpu_choice == 1)`
  - `(user_choice == 3 and cpu_choice == 2)`

- **CPU wins:**

  - `(cpu_choice == 1 and user_choice == 3)`
  - `(cpu_choice == 2 and user_choice == 1)`
  - `(cpu_choice == 3 and user_choice == 2)`

- **Any other value:** Invalid option

---

> [!TIP]
> This helps your logic always give the correct result, regardless of the order.
