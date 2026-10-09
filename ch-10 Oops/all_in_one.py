class User:
    def __init__(self, name, number, balance):      # dunder
        self.name = name                             # self
        self.number = number
        self.balance = balance

    def recharge(self, amount):                      # self
        self.balance += amount

    def show_balance(self):                          # self
        print(self.name, "ka balance:", self.balance)

    def __str__(self):                               # dunder
        return f"{self.name} ({self.number}) - Rs.{self.balance}"

    def __add__(self, other):                        # dunder
        return self.balance + other.balance

    @staticmethod
    def is_valid_number(number):                     # staticmethod
        return len(number) == 10 and number.isdigit()


num = "9876543210"

if User.is_valid_number(num):          # staticmethod (object ke bina)
    u1 = User("Rahul", num, 100)       # __init__ chala
    u1.recharge(50)                    # self wala method
    print(u1)                          # __str__ chala