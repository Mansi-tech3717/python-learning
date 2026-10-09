class Employee:
    language = "Python"  # This is a class attribute
    salary = 500000
    def getInfo(self):
        return f"Language: {Employee.language}, Salary: {Employee.salary}"
    
    @staticmethod
    def greet():
        return "Hello, welcome to the company!"

    def __init__(self, language, salary): # Dunder method, also known as a constructor method which is automatically called when an object is created.
        self.language = language
        self.salary = salary
        print("This is a constructor method. It is called when an object is created.")
Mansi = Employee("Java", 600000)
print(Employee.greet())
# print(Mansi.getInfo())  
print(f"Language: {Mansi.language}, Salary: {Mansi.salary}")