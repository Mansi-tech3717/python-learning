class Demo:
    a = 4
o= Demo()# Prints class attribute because instance attribute is not present
print(o.a)
o.a = 0 #Instance attribute is created and assigned a value of 0
print(o.a) # Prints instance attribute because instance attribute is present