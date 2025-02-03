class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account({self.account_number}, {self.account_holder}, Balance: {self.balance})"

    def credit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def debit(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def transfer(self, amount, target_account):
        if self.debit(amount):
            target_account.credit(amount)
            return True
        return False