#imports

import random,os


#Assets
Logo  = """
 __          __  _                            _          _    _                                           _ 
 \ \        / / | |                          | |        | |  | |                                         | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __   | |
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | |
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |  | | (_| | | | | (_| | | | | | | (_| | | | | |_|
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| (_)
                                                                             __/ |                          
                                                                            |___/                                             
"""



#initializations 

key = "Immortal"
size = len(key)
size = size-1
mark = list()

for i in range(0,size):
    mark.append('_')

#methods


def graphic(desired):
    Image = ['''
         |
         |
         |
        ===''','''
    +---+
         |
         |
         |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
    print(Image[desired])


def check_word(user,icon,life):
    count = 0
    for k in range(0,size):
        if user == key[k] and mark[k] == "_":
            mark[k] = key[k]
            count = 1
            print(key[k]+" ",end = '')
        else :
            print(mark[k]+" ",end = '')

    print("\n")

    if count == 0:
        stat,icon,life = check_life(life,icon)
        return stat,icon,life
    else :
        stat = 1
        graphic(icon)
        print("\n\n")
        return stat,icon,life

def check_life(life,icon):
     if life == 2:
        graphic(icon)
        print("\n\n")
        print("You lose\nThe hidden word is\n")
        graphic(icon+1)
        for i in range (0,size+1):
            print(key[i]+" ",end = "")
        return 0,icon,life
     else:
        icon = icon + 1
        graphic(icon)
        print("\n\n")
        life =life - 1
        return 1,icon,life

# main()

life = 8
end = 1
print(Logo+"\n")

print("Guess the word \nEach wrong guess result in the Death of your Avatar\n")

print("_ _ _ _ _ _ _ _\n\n")

icon = 0
while(end):
    print("Enter a letter :")
    user =  input()
    print("\n")
    end,icon,life = check_word(user,icon,life)
    
