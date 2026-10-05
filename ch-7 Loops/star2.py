""""
* * *
*   *
* * *
"""
for i in range(3):
    for j in range(3):
        if i == 0 or i == 2 or j == 0 or j == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ") 