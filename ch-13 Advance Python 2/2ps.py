from functools import reduce
l = [3,4,5,678,98,56,656,455,4345,67645,45445]

def greater(a,b):
    if(a>b):
        return a 
    return b 

print(reduce(greater,l))
