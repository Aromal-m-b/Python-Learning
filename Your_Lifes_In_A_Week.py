year = int(input("Enter is the year you were born?"))
current = int(input("Enter the current year"))
age = current-year
print("Assuming you will live until 90 years old\nyou have "+str(age-90)+" years remaining\nyou have "+str((age-90)*52)+" weeks \nyou have "+str((age-90)*365)+" Days")
