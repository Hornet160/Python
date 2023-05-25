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

# code is below this line 👇


games_image = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))
if user_choice>=3 or user_choice<0:
    print("You Entered invalid number")
else:
    print(games_image[user_choice])
    print("Computer Chose:")
    print(computer_choice)
    print(games_image[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You Win")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose")
    elif user_choice > computer_choice:
        print("You Win")
    elif user_choice < computer_choice:
        print("You lose")
    elif user_choice == computer_choice:
        print("It is a draw")
