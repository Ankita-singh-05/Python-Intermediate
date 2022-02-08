from abc import ABCMeta, abstractmethod

class Vehicle(metaclass=ABCMeta):
    @abstractmethod
    def payment_mode(self):
        pass #Line1

class Car(Vehicle):
    def payment_mode(self):
        print("Payment mode")

class BMW(Vehicle):
    pass #Line2

BMW() #Line3