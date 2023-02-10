class BankAccount:
    bank_name = "Intergalatic Bank of the Republic"
    accounts = []
    def __init__(self, int_rate: float, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        self.int_yeild = int_rate * balance
        BankAccount.accounts.append(self)
        
        

    def deposit(self, amount):
        self.balance += amount
        print(f"Depoist:{amount}\nBalance:{self.balance}")
        return self
    
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds.Charging a $5 fee")
            self.balance - 5
            return self
        else :
            self.balance -= amount
            print(f"Withdraw:{amount}\nBalance:{self.balance}")
            return self
    
    
    def display_account_info(self):
        print(f"\nIntrest Rate:{self.int_rate}\nBalance:{self.balance}")
        return self
        
    
    def yield_interest(self):
        if self.balance > 0:
            self.int_yeild = self.balance * self.int_rate
            self.balance += self.int_yeild
            print(f"Intrest yeild:{self.int_yeild}")
        else:
            print("Account not eligible for yield")
        return self
    
    @classmethod
    def accounts_info(cls):
        for account in cls.accounts:
            account.display_account_info()
        

accountOne = BankAccount(.05)

accountTwo = BankAccount(.075)

accountOne.deposit(200).deposit(1200).deposit(3000).withdraw(500).yield_interest().display_account_info()

accountTwo.deposit(760). deposit(5239).withdraw(75).withdraw(100).withdraw(120).withdraw(570).yield_interest().display_account_info()

BankAccount.accounts_info()

