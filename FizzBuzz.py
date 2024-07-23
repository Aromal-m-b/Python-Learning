print("Welcome to my FizzBuzz Game\nin this game we count numbers from 0  to 100 \nFor each multiple of 3 occurs we will say Fizz\nFor each Multiple of 5 we will say Buzz\nFor each mutliple of 3 and 5 we will say FizzBuzz")
for i in range (0,101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else :
        print(str(i))
