marks1 = int(input("Enter your marks 1: "))
marks2 = int(input("Enter your marks 2: ")) 
marks3 = int(input("Enter your marks 3: "))

total_percentage = (marks1 + marks2 + marks3) / 3
if (total_percentage >= 40):
    print("You are pass. Congratulations!")
else:
    print("you are fail. better luck next year.")