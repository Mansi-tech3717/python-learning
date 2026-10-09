class Employee:
    language = "Python"  # This is a class attribute
    salary = 500000
    def getInfo(self):
        return f"Language: {self.language}, Salary: {self.salary}"
Mansi = Employee()
Mansi.language = "Java"  # This is an instance attribute
print(Mansi.getInfo())
