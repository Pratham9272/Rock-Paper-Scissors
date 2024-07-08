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
choosen=int(input("What do you want to choose type 0 for rock,1 for paper and 2 for scissors"))
game=[rock,paper,scissors]
print("You choose:")
i_choose=game[choosen]
print(i_choose)
print("Computer chooses:")
result=random.randint(0,2)
final=game[result]
print(final)
if i_choose==rock and final==scissors:
   print("You won")
elif i_choose==scissors and final==paper:
     print("You won")
elif i_choose==paper and final==rock:
     print("You won")
elif i_choose==final:
  print("It's a draw1")
else:
     print("AI won")