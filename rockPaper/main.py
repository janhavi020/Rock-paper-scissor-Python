import random
from art import logo
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

print(logo)
emoji = [rock,paper,scissors]
print("")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(emoji[user_choice])
computer_choice = random.randint(0,2)
print("computer choose: ")
print(emoji[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == computer_choice:
    print("it's a draw!!")
elif user_choice == 2 and computer_choice == 0:
    print("you lose")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice > user_choice:
    print("you lose")
elif user_choice > computer_choice:
    print("you win")

