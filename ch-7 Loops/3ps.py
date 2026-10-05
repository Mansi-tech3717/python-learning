n = int(input("Enter your number : "))
for i in range(2,n):
    if(n%2)== 0:
        print("this is not a prime number.")
        break
else:
    print("This is a prime number.")