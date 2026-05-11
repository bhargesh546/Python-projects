# A static method is a method that belongs to the class itself rather than any instance of the class. 
# Also cannot take self as a parameter.

class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self.balance += amount
            self.__log_transaction("deposit", amount)
        else:
            print("Deposit amount must be positive")

    def _is_valid_amount(self, amount):
        return amount > 0

    def __log_transaction(self, transaction_type, amount):
        print(f"Logging {transaction_type} of ${amount}. New Balance: ${self.balance}")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
    
account = BankAccount("Alice", 500)
account.deposit(200)

print(BankAccount.is_valid_interest_rate(6))