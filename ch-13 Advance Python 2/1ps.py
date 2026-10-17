def divisible5(n):
    if(n%5 == 0 ):
        return True
    return False

a = [3,4,5,678,98,56,656,455,4345,67645,45445]
f = list(filter(divisible5,a))
print(f)