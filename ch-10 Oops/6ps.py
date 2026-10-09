from random import randint

class Train:
    def __init__(slf, name, fare, seats):
        slf.name = name  #If i write slf instead of self it will not give any error but it is a convention to use self as the first parameter of the method in python classes. It is used to refer to the instance of the class.
        slf.fare = fare
        slf.seats = seats

    def getStatus(mansi): # if i write mansi instead of self it will not give any error but it is a convention to use self as the first parameter of the method in python classes. It is used to refer to the instance of the class.
        print(f"The name of the train is {mansi.name}.")
        print(f"The seats available in the train are {mansi.seats}.")

    def fareInfo(self):
        print(f"The price of the ticket is Rs. {self.fare}.")

    def bookTicket(self):
        if self.seats > 0:
            print(f"Your ticket has been booked! Your seat number is {randint(1, 100)}.")
            self.seats -= 1 # this is used to update the number of seats available after booking a ticket
        else:
            print("Sorry, no seats available!")
t = Train("Rajdhani Express", 1500, 5)
t.getStatus()
t.fareInfo()
t.bookTicket()