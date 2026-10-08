# import random 

# def game():
#     print("You are playing the game...")
#     score = random.randint(1, 62)
#     # Fetch the high score from the file
#     with open("hiscore.txt", "r") as f:
#         hiscore = f.read()
#         if hiscore != "":
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0
#     print(f"Your score:{score}")
#     if(score>hiscore ):
#         with open("hiscore.txt", "w") as f:
#             f.write(str(score))
#         print("You have made a new high score")
#     return score

# game()


import random

score = random.randint(1, 62)

# Read old high score
with open("hiscore.txt", "r") as f:
    high_score = f.read()

if high_score == "":
    high_score = 0
else:
    high_score = int(high_score)

print("Your score:", score)
print("Old high score:", high_score)

if score > high_score:
    print("New high score!")

    with open("hiscore.txt", "w") as f:
        f.write(str(score))