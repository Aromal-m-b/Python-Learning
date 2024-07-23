
map = [['◻️','◻️','◻️','◻️','◻️','◻️','◻️','◻️','◻️'],['◻️','◻️','◻️','◻️','◻️','◻️','◻️','◻️','◻️'],['◻️','◻️','◻️','◻️','◻️','◻️','◻️','◻️','◻️'],['◻️','◻️','◻️','◻️','◻️','◻️','◻️','◻️','◻️'],['◻️','◻️','◻️','◻️','◻️','◻️','◻️','◻️','◻️'],['◻️','◻️','◻️','◻️','◻️','◻️','◻️','◻️','◻️']]

for x in range (0,6):
    for y in range (0,9):
        print(map[x][y]+" ",end ="")
    print()

print("Welcome to the Tresure map creator 1.0\nyou can mark the location of the treasure on the above map \nwhere do you want to hide the map?\nwhich column? which row?")
c = int(input())
r = int(input())

map[r][c] = "X"

for x in range (0,6):
    for y in range (0,9):
        if y == c and x == r:
            print(" "+map[x][y]+"",end = "")
        else :
            print(map[x][y]+" ",end ="")
    print()

print("Treasure has been sucesfully marked")
