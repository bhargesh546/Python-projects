# Encapsulation is used to bundle attributes, method and restricting direct access by making them protected 

class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        else:
            self._balance += amount

    def withdrawl(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawl amount must be positive.")
        elif amount > self._balance:
            raise ValueError("Insufficient funds.")
        else:
            self._balance -= amount

account = BankAccount()
print(account.balance)
account.withdrawl(20)