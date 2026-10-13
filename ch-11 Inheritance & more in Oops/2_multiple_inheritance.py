class Employee:
    company = "Microsoft"
    name = "default"
    def show(self):
        print(f"the name of the employee is {self.name} and the company  is {self.company}")

class coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the languages, the best language is {self.language}")
class Programmer(Employee,coder):
    company = "Google"
    def showLanguage(self):
        print(f"the company of the employee is {self.company}  and the language is {self.language}")  
a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()