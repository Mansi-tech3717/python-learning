# write a program to make pattern using recursion
def pattern(n):
    if n > 0:
        print("*" * n)
        pattern(n - 1)
pattern(3)