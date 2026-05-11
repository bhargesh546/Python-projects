# Encapsulation - Encapsulation is about bundling data and methods together and controlling access to that data.

class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Amount must be positive")
        
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive and greater than 0")
        elif amount > self._balance:
            raise ValueError("insufficient funds")
        else:
            self._balance -= amount

account = BankAccount()
account.deposit(1.99)
print(account.balance)
account.withdraw(1)
print(account.balance)