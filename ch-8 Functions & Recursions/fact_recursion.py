def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)
factorial = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {factorial} is: {fact(factorial)}")