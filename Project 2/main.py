import random 
n = random.randint(1,100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the number : "))
    if(a >n ):
        print("Lower number please")
    else:
        print("higher number please")
    guesses +=1

print(f"Your have guess the number {n} correctly in {guesses} attempts")