```python
## Guess a number
import random

logo = """
  ___  _  _  ____  ____  ____     __     __ _  _  _  _  _  ____  ____  ____ 
 / __)/ )( \(  __)/ ___)/ ___)   / _\   (  ( \/ )( \( \/ )(  _ \(  __)(  _ \
( (_ \) \/ ( ) _) \___ \\___ \  /    \  /    /) \/ (/ \/ \ ) _ ( ) _)  )   /
 \___/\____/(____)(____/(____/  \_/\_/  \_)__)\____/\_)(_/(____/(____)(__\_)

"""

print(logo)

level = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard':")

# define difficulty level
if level == "easy":
  guess_times = 10
  print(f"You have {guess_times} attempts remaining to guess the number.")
elif level == "hard":
  guess_times = 5
  print(f"You have {guess_times} attempts remaining to guess the number.")
else:
  print("Please check your input.")

# generate a correct answer
answer = random.randint(1,101)

def compare():
  continue_to_play = True
  while continue_to_play:
    for i in range(1, guess_times+1):
      guess_number = int(input("Make a guess:"))
      remaining_times = guess_times - i
      if guess_number == answer:
        print(f"You got it! The answer was {guess_number}!")
      elif guess_number < answer:
        print(f"Too low.\nGuess again.\nYou have {remaining_times} attempts remaining to guess the number.\n")
      else:
        print(f"Too high.\nGuess again.\nYou have {remaining_times} attempts remaining to guess the number.\n")

    if remaining_times > 0 and guess_number != answer:
      continue_to_play = True
    elif remaining_times > 0 and guess_number == answer:
      continue_to_play = False
      print("This game ends.")
    else:
      continue_to_play = False
      print("Sorry, there is no attempt anymore. This game ends.")
  

compare()
```
