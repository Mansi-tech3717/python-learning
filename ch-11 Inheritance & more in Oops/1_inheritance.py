class Employee:
    company = "Microsoft"
    def show(self):
        print(f"the name of the employee is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "Google"
#     def __init__(self, name, salary, language):
#         super().__init__(name, salary)
#         self.language = language

#     def show(self):
#         print(f"the name of the employee is {self.name} and the salary is {self.salary} ")

#     def showLanguage(self):
#         print(f"the name of the employee is {self.name}  and the language is {self.language}") 
class Programmer(Employee):
    company = "Google"
    def showLanguage(self):
        print(f"the name of the employee is {self.name}  and the language is {self.language}")  
a = Employee()
b = Programmer()
print(a.company , b.company)