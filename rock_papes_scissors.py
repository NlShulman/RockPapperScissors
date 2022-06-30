
#  Rock Paper Scissors game

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
import random 
users_choice = int(input("choose, 0 for rock, 1 for paper, or 2 for scissors "))

options = [rock, paper, scissors]
computer_choice = random.randint(0,2)
computer_image = options[computer_choice]

if users_choice > 2 : 
    print("Try again")
else:
    print(f"You chose : \n {options[int(users_choice)]}")
    print(f"Computer chose : \n {computer_image}")


    if computer_choice == users_choice:
        print("It's a tie")

    elif ((computer_choice == 0) and (users_choice == 2)) or ((computer_choice == 2) and (users_choice == 1)) or ((computer_choice == 1) and (users_choice == 0)):
        print("You LOST ")


    else:
        print("You WON")

