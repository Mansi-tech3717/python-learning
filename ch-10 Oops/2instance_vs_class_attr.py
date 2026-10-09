class Employee:
    language = "Python"  # This is a class attribute
    salary = 500000
    
Mansi = Employee()
Mansi.language = "Java"  # This is an instance attribute
print(Mansi.language)
print(Mansi.salary)
