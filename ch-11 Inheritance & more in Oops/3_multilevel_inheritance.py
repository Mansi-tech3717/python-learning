class Employee:
    a = 1
class Programmer(Employee):
    b = 2
class Manager(Programmer):
    c = 3
o = Employee()
print(o.a) # Prints the attribute a of class Employee
print(o.b) # This will give an error because class Employee does not have attribute b
o = Programmer()
print(o.a , o.b) # Prints the attributes a and b of class Programmer
o = Manager()
print(o.a , o.b , o.c) # Prints the attributes a, b, and c of class Manager