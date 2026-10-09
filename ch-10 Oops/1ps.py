class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

p = Programmer("Mansi", 800000, "Python")
print(f"Name: {p.name}, Salary: {p.salary}, Language: {p.language}, Company: {Programmer.company}")
p = Programmer("kanu", 900000, "Java")
print(f"Name: {p.name}, Salary: {p.salary}, Language: {p.language}, Company: {Programmer.company}")