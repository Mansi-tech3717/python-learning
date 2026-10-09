class Employee:
    language = "Python"  # This is a class attribute
    salary = 500000
    def getInfo(self):
        return f"Language: {Employee.language}, Salary: {Employee.salary}"

    @staticmethod
    def greet():
        return "Hello, welcome to the company!"
Mansi = Employee()
Mansi.language = "Java"  # This is an instance attribute
print(Employee.greet())
print(Mansi.getInfo())