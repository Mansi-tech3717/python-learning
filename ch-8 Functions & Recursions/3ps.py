# write a program to find the sum of first n natural numbers using recursion
def sum_natural(n):
    if n <= 1:
        return n
    else:
        return n + sum_natural(n - 1)

n = int(input("Enter the value of n: "))
print("The sum of first n natural numbers is:", sum_natural(n))