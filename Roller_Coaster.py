print("Welcome to Roller Coaster Ticket Generator\n")

age=int(input("Enter your age\n"))
height=int(input("Enter your Height(cm)\n"))
if(age>18 & height>122):
    print("You are an Adult \nyour Ticker Fee is $12")
elif(height<122):
    print("Sorry you have to grow taller before you can ride\n")
else:
    print("You are a Child \nYour ticket fee would be $8")
