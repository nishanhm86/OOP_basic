from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay (self, currency, payment_amount):
        pass

class CreditCards(Payment):
    def pay (self, currency, payment_amount):
        print(f"\nPaid {currency} {payment_amount} using credit card payment method")

class PayPal(Payment):
    def pay (self, currency, payment_amount):
        print(f"\nPaid {currency} {payment_amount} using PayPal payment method")

class CryptoCurrency(Payment):
    def pay (self, currency, payment_amount):
        print(f"\nPaid {currency} {payment_amount} using Crypto currency")

pay1 = PayPal()
pay2 = CreditCards()
pay3 = CryptoCurrency()

pay1.pay ("USD", 1000)
pay2.pay ("LKR", 2500)
pay3.pay ("SHIB", 2500)