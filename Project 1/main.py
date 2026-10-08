# write a program to play a game snake,water,gun
import random

computer=random.choice(['snake', 'water', 'gun'])
user= input("Enter your choice (snake, water, gun): ")
print(f"Computer chose: {computer}")
print(f"You chose: {user}")
if user == computer:
    print("It's a tie!")
elif (user == "snake" and computer == "water") or (user == "water" and computer == "gun") or (user == "gun" and computer == "snake"):
    print("You win!")
else:
    print("Computer wins!")