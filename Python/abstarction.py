

from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print("your purchase amount: ",amount)

    @abstractmethod
    def payment(self, amount):
        pass

class CardPayment(car):

    def payment(self, amount):
        print('your purchase amount of {} exceeded your $100 limit '.format(amount))


obj = CardPayment()
obj.paySlip("$444")
obj.payment("$90")
