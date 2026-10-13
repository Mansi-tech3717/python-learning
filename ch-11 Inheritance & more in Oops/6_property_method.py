class Employee:
    a = 1
    @classmethod # This decorator is used to define a class method.
    def show(cls):
        print(f"the  class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 2
e.name = "Mansi Prajapat"
print(e.name)
e.show()