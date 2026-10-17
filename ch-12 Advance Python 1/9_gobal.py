a = 56
def fun():
    global a
    a = 5
    print(a)
    
fun()
print(a)