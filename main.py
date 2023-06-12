#importing random module
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("welcome to the game!")
choice_user = int(input("Rock, Paper Or Scissors (0/1/2) --> "))
choice_comp = random.randint(0, 2)

displaying_choice_user = ''
displaying_choice_comp = ''
winner = ''
gameOption = [rock,paper,scissors]

displaying_choice_comp = gameOption[choice_comp]
print("\n")
if not choice_user > 2:
  displaying_choice_user = gameOption[choice_user]
  print('User:'+displaying_choice_user)
  print('Comp:'+displaying_choice_comp)
  # User: Rock
  if choice_user == 0 :
    if choice_comp == 0:
      winner = 'Tie'
    elif choice_comp == 1:
      winner = 'Comp'
    elif choice_comp == 2:
      winner = 'User'
  # User: Paper
  elif choice_user == 1 :
    if choice_comp == 0:
      winner = 'User'
    elif choice_comp == 1:
      winner = 'Tie'
    elif choice_comp == 2:
      winner = 'Comp'
  # User: Scissors
  elif choice_user == 2 :
    if choice_comp == 0:
      winner = 'Comp'
    elif choice_comp == 1:
      winner = 'User'
    elif choice_comp == 2:
      winner = 'Tie'

  if not winner == 'Tie':
    print(f"-----------> {winner}: wins the game <-----------")
  else:
    print(f"-----------> {winner}: nobody wins the game <-----------")
else:
  print("\n---> Select only 0 or 1 or 2 <---")