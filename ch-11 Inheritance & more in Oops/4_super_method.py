class Employee:
    def __init__(self):
        print("Employee Constructor")
    a = 1
class Programmer(Employee):
    def __init__(self):
        super().__init__() #calls constructor of base class Employee
        print("Programmer Constructor")
    b = 2
class Manager(Programmer):
    def __init__(self):
        super().__init__() #calls constructor of base class Programmer
        print("Manager Constructor")
    c = 3
# o = Employee()
# print(o.a)
 
# o = Programmer()
# print(o.a , o.b) 
o = Manager() # This will call the constructor of Manager class which in turn calls the constructor of Programmer class and then the constructor of Employee class
print(o.a , o.b , o.c) 