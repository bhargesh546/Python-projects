# Static Methods - It belongs to the class itself rather than any instance of the class and
#       We use '@staticmethod' decorator to define the static method and is used when we don’t need class or instance data.
#       whereas we use '@classmethod' decorator when we need to know which class is calling the method (important for inheritance).

class BankAccount:
    MIN_BALANCE = 100
    MIN = 10
    MAX = 20

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            # print(f"{self.owner}'s new balance is ${self._balance}")
            self.__log_transaction("deposit", amount)
        else:
            print("Deposit amount must be greater than 0")
    
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
    
    # protected method
    def _is_valid_amount(self, amount):
        return amount > 0
    
    # private method
    def __log_transaction(self, transaction_type, amount):
        print(f"Logging \n{transaction_type.capitalize()} of ${amount}. New balance is ${self._balance} ")

    @classmethod
    def adding_things(cls):
        sum = cls.MIN + cls.MAX
        return cls("Teddy", sum)
    
    @staticmethod
    def adding_numbers(num1, num2):
        return num1 + num2
    
account = BankAccount("Alice", 500)
account.deposit(200)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))
print(BankAccount.adding_numbers(3, 5))

account2 = BankAccount.adding_things()
print(account2.owner)