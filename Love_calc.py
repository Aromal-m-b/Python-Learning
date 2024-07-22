print("Welcome to My True Love Calculator\n")

first = input("Enter your name\n")
second = input("Enter your crush's name\n")

first=first.lower()
second=second.lower()
first = first+second

print(first)

one = str(first.count("t")+first.count("r")+first.count("u")+first.count("e"))
ten = str(first.count("l")+first.count("o")+first.count("v")+first.count("e"))

print("T occurs "+str(first.count("t"))+" times\nR occurs "+str(first.count("r"))+"times\nU occurs "+str(first.count("u"))+" times\nE occurs "+str(first.count("e"))+" times")
print("\n\nL occurs "+str(first.count("l"))+" times\nO occurs "+str(first.count("o"))+" times\nV occurs "+str(first.count("v"))+" times\nE occurs "+str(first.count("e"))+" times")

print("Your score is "+one+ten+"\n")

score =int(one + ten)

if score<10 & score>90:
    print("You go together like coke and mentos")
elif score>=40 & score<=50:
    print("You are alright Together")
