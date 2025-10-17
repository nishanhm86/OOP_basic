# Define a class named OOPEncapsulation to demonstrate the concept of encapsulation
class OOPEncapsulation:

    # Constructor method to initialize object attributes
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute (can be accessed directly)
        self.__balance = balance    # Private attribute (encapsulated / hidden from outside)

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount                                    # Check if the deposit amount is positive
            print(f"Deposited {amount}.New balance: {self.__balance}")  # Add the amount to the private balance

    # Method to withdraw money from the account
    def withdraw(self, amount):
        # Check if the withdrawal amount is valid and within available balance
        if 0 < amount <= self.__balance:
            self.__balance -= amount                                    # Deduct the amount from the balance
            print(f"Withdrawal {amount}.Remaining Balance: {self.__balance}")

        else:
            # Triggered if balance is insufficient or invalid withdrawal amount
            print("Insufficient Balance")

    # Getter method to safely access the private balance value
    def get_balance(self):
        return self.__balance   # Returns the private variable value

acc = OOPEncapsulation("Nishan", 1000000)
acc.deposit(100000)
acc.withdraw(50000)

# Access the current balance using the getter method
print("Final Balance:", acc.get_balance())