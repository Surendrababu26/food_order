class Account:
    def __init__(self,n,b):
        self.name=n
        self.balance=b
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"deposited amount is {amount}")
        print(f"balance is{self.balance}")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print(f"withdrawl amount{amount}")
            print(f"balance amount {self.balance}")
        else:
            print("insufficient balance")
    def show_balance(self):
        print(f"balance {self.balance}")
class SavingsAccount(Account):
    def __init__(self,n,b,ir=0.05):
        super().__init__(n,b)
        self.interest_rate=ir
    def add_interest(self):
        interest=self.balance*self.interest_rate
        self.balance=self.balance+interest
        print(f"interest amount{interest}")
        print(f"balance {self.balance}")
class CheckingAccount(Account):
    def __init__(self,n,b,ol=1000):
        super().__init__(n,b)
        self.overdraft_limit=ol
    def withdraw(self,amount):
        if self.balance+self.overdraft_limit>=amount:
            self.balance=self.balance-amount
            print(f"withdrawl amount{amount}")
        else:
            print("exceed overdraft limit")

print("========savings Account========")
s = SavingsAccount("Surya", 1000)
s.deposit(500)
s.add_interest()
s.withdraw(200)
s.show_balance()
print("========checking Account========")
c = CheckingAccount("Axis", 1000)
c.withdraw(1200)
c.deposit(300)
c.withdraw(700)
c.show_balance()
        
    
