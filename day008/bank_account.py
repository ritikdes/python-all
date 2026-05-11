class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount < 0:
            print("Amount must be positive")
            return
        else:
            self.balance += amount
            self.transactions.append(amount)
            return self.balance
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient amount!")
        else:
            self.balance -= amount
            self.transactions.append(-amount)
        return self.balance
    
    def get_statement(self):
        print(f"{self.owner}'s Statement")
        for t in self.transactions:
            if t < 0:
                print(f" - {abs(t)}")
            else:
                print(f" + {t}")
        print(f"Balance: {self.balance}")
    
    def __str__(self):
        return f"{self.owner}'s account | Balance: {self.balance}"
    
account1 = BankAccount("Ram", 10000)
print(account1)
account1.deposit(10000)
print(account1)
account1.withdraw(20000)
print(account1.get_statement())
print(account1)