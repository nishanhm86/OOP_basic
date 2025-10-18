class BankingSystem:
    def __init__(self, name, currency, pin):
        self.name = name            #public attribute
        self.currency = currency    #public attribute
        self.__balance = 500        #private attribute (Encapsulation) Also introduce security
        self.__pin = pin            #private attribute (Encapsulation) Also introduce security

    def get_client_info(self):
        print(f"Customer Name is {self.name} and account is maintained in {self.currency}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit {amount} current balance is {self.currency} {self.__balance}")
        else:
            print("Enter the correct amount")

    def withdrawal(self, amount, pin):
        if pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdraw {amount} Remaining balance: {self.currency} {self.__balance}")
            else: print("Insufficient funds!")
        else:
            print(f"incorrect pin. Contact bank for more information")
    def get_balance(self):
        print(f"Statement balance is {self.currency} {self.__balance}")
        return self.__balance

d2 = BankingSystem("Janethri", "USD", 1234)
d2.get_client_info()
d2.deposit(600)
d2.withdrawal(100, 1234)
d2.get_balance()
