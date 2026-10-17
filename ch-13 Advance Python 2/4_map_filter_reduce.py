from functools import reduce

# Map example ... map tb use hota h jb hume sare elements ke liye function chalana hota h toh 
l = [1,2,3,4,5,6,7,8,9]
square = lambda x: x*x
sqlist = map(square,l)
print(list(sqlist))


# Filter example
def even(n):
    if(n%2 == 0):
        return True
    return False
onlyEven = filter(even,l)
print(list(onlyEven))

# Reduce example
def  sum (a,b):
    return a+b
print(reduce(sum,l))