import random

print("Welcome to my Rock Paper Scissors Game\nInstructions:-\n* 0 represents Rock\n* 1 represents Paper\n* 2 represents Scissors")


GAME_IMAGES = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

print("Enter the Score needed to win\n")
t = int(input())
win =0
cwin = 0
uwin = 0
print("\n Game Starts now")
while win<=t:
    comp = random.randint(0,2)
    print("what is your choice? 1 = rock, 2 = paper, 3 = scissors")
    user = input()
    valid=0
    while valid == 0:
        if user.isdigit() :
            user = int(user)
            if user>=0 and user<=2:
                valid = 1
        else:
            print("Sorry Wrong Choice \n")
    if comp == user:
        print("User\n"+GAME_IMAGES[user]+"Computer\n"+GAME_IMAGES[comp])
        print("\n Draw\nComputer\t\tUser\n   "+str(cwin)+"\t                 "+str(uwin))
    else :
        if user == 0:
            if comp == 1:
                cwin = cwin + 1
                print("User\n"+GAME_IMAGES[user]+"Computer\n"+GAME_IMAGES[comp])
                print("Paper beats Rock\nComputer\t\tUser\n   "+str(cwin)+"\t                 "+str(uwin))
            elif comp == 2:
                uwin = uwin + 1
                print("User\n"+GAME_IMAGES[user]+"Computer\n"+GAME_IMAGES[comp])
                print("Rock beats Scissors\nComputer\t\tUser\n   "+str(cwin)+"\t                 "+str(uwin))
        elif user == 1:
            if comp == 0:
                uwin = uwin + 1
                print("User\n"+GAME_IMAGES[user]+"Computer\n"+GAME_IMAGES[comp])
                print("Paper beats Rock\nComputer\t\tUser\n   "+str(cwin)+"\t                 "+str(uwin))
            elif comp == 2:
                cwin = cwin + 1
                print("User\n"+GAME_IMAGES[user]+"Computer\n"+GAME_IMAGES[comp])
                print("Scissor beats Paper\nComputer\t\tUser\n   "+str(cwin)+"\t                 "+str(uwin))          
        elif user == 2:
            if comp == 0:
                cwin = cwin + 1
                print("User\n"+GAME_IMAGES[user]+"Computer\n"+GAME_IMAGES[comp])
                print("Rock beats Scissors\nComputer\t\tUser\n   "+str(cwin)+"\t                 "+str(uwin))
            elif comp == 1:
                uwin = uwin + 1
                print("User\n"+GAME_IMAGES[user]+"Computer\n"+GAME_IMAGES[comp])
                print("Scissors beat Paper\nComputer\t\tUser\n   "+str(cwin)+"\t                 "+str(uwin))
    
    if uwin > cwin:
        win = uwin
    else :
        win = cwin

if win == uwin:
    print("User Won")
else:
    print("Computer Won")
