class Employee:
    a = 1
    @classmethod # This decorator is used to define a class method.
    def show(cls):
        print(f"the  class attribute of a is {cls.a}")

e = Employee()
e.a = 2
e.show()