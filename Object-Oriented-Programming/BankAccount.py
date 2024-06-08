class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False

    def get_balance(self):
        return self.balance

account = BankAccount("123456789", "John Doe", 1000.0)
print("Initial Balance:", account.get_balance())  # Output: 1000.0

account.deposit(500.0)
print("Balance after deposit:", account.get_balance())  # Output: 1500.0

withdrawal_status = account.withdraw(200.0)
print("Withdrawal Status:", withdrawal_status)  # Output: True
print("Balance after withdrawal:", account.get_balance())  # Output: 1300.0

withdrawal_status = account.withdraw(2000.0)
print("Withdrawal Status:", withdrawal_status)  # Output: False
print("Balance after withdrawal:", account.get_balance())  # Output: 1300.0