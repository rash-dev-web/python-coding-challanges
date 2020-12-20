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

game_images = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if user_input >= 3 or user_input < 0:
    print("Your have entered a invalid number. You lose!")
else:
    print(game_images[user_input])
    print("Computer chose:")
    computer_pick = random.randint(0, 2)
    print(game_images[computer_pick])

    if user_input == 0 and computer_pick == 2:
        print("You win!")
    elif computer_pick == 0 and user_input == 2:
        print("You Lose!")
    elif computer_pick > user_input:
        print("Your Lose!")
    elif user_input > computer_pick:
        print("You Win!")
    elif user_input == computer_pick:
        print("It's a draw")
