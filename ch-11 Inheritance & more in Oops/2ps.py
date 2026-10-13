class Animals:
    pass
class Pets(Animals):
    pass
class Dog(Pets):
    @staticmethod # when don't want to write self so we need to write this method
    def bark():
        print("bow bow!!!")

d = Dog()
d.bark()