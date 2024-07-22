c=1
while(c==1):
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    print("Welcome To the Treasure Island.Your Mission is to find the Treasure\n")
    print("After a Long path you have reached a crossroad There are two paths before you one that leads to your death and other to the Treasure\nWhat do you choose Left or Right\n")
    us = input()

    if(us == "Left"):
        print("You continue your journey Towards the Treasure\n")
        print("After some time you reached the end of the path facing a river \n,Now you have two choices you either swim or wait\n")
        us = input()
        if(us=="wait"):
            print("After crossing a river you finally reached the cave In which the treasure is hidden\nThe treasure is within your reach at last\nThere are Three Doors infront of you\n1)Red\n2)Yellow\n3)Blue\nBehind one of these doors lies the hidden treasure\nWhat will you choose\n")
            us=input()
            if(us=="Red"):
                print("You are Burned by the fire\nGAME OVER")
                c=0
                c=int(input("If You want to continue press 1\n"))
            elif(us=="Yellow"):
                print("Congratulation After the long and Adventurous journey you have atlast reached the Treasure\nYou win")
            elif(us=="Blue"):
                print("You are Eaten by the beasts\nGAME OVER")
                c=0
                c=int(input("If You want to continue press 1\n"))
            else:
                print("Game Over")
        elif(us=="swim"):
            print("You were attacked by the trout\nGAME OVER")
            c=0
            c=int(input("If You want to continue press 1\n"))
    else:
        print("Sadly your choice was wrong.You fell into a hole\nGAME OVER")
        c=0
        c=int(input("If You want to continue press 1\n"))
