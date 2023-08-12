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
def printChoice(Choice):
    if Choice == 0:
        print(rock)
    elif Choice == 1:
        print(paper)
    else:
        print(scissors)

userChoice=(int)(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
comChoice=random.randint(0,2)
printChoice(userChoice)
print("Computer Chose:\n")
printChoice(comChoice)
if comChoice-userChoice==0:
    print("You Tied")
elif comChoice-userChoice==1 or comChoice-userChoice==-2:
    print("You Lose")
else:
    print("You Win!")