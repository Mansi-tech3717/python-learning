from random import randint

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}.")
        print(f"The seats available in the train are {self.seats}.")

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