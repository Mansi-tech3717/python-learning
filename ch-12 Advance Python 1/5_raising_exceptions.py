a = int(input("Enter a number : "))
b = int(input("Enter b number : "))
if(b == 0 ):
    raise ZeroDivisionError("Hey our program is not meant for divide numbers by zero.")
else:
    print(f"The divison a/b is {a/b}")