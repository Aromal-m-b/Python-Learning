print("Welcome to tip calculator")
bill = float(input("What is the bill amount? \n$"))
n = int(input("How many People to split the bill?\n"))
tip = ((input("What percentage tip would you like to give? 10, 12, 15,or custom")))
if(tip=="custom"):
    tip=float(input("What percentage would you like to give"))
elif((tip.isdigit())=="Flase"):
    print("Invalid Input")
    exit()
tip=float(tip)
amount = ((bill/100)*tip)+bill
print("Each of your friends can pay $"+str((amount/float(n))))
