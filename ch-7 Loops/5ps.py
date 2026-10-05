n = int(input("Enter your number : "))
i = 1
fact = 1
for i in range(1,n+1):
    fact = fact*i
print(f"the factorial of {n} is {fact}")