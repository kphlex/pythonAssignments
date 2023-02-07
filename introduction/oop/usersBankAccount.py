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
        return self
    
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds.Charging a $5 fee")
            self.balance - 5
            return self
        else :
            self.balance -= amount
            print(f"\nWithdraw:{amount}\nBalance:{self.balance}")
            return self
    
    
    def display_account_info(self):
        print(f"Intrest Rate:{self.int_rate}\nBalance:${self.balance}")
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
        



class User:
    all_users = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = .05, balance = 0)
        
        
    def make_deposit(self, amount, accountType=""):
        self.account.deposit (amount)
        print(f"\nAccount:{accountType}")
        return self
        
    def make_withdraw(self, amount, accountType=""):
        self.account.withdraw(amount)
        print(f"Account:{accountType}")
        return self
    
    def display_User_account(self):
        print(f"Name:{self.name}\nEmail:{self.email}")
        self.account.display_account_info()
        
    # Transfers money from user 1 to user 2. If user 1 does not have enough, it doesnt send. 
    def transfer_money(self, amount, other_user):
        if  self.account.balance > amount:
            self.account.balance - amount
            print(f"{user1.name} sent you ${amount}!")
            return self
        else :
            print("Try transfer later....")
        return self
        
        
user1 = User("Darth Vader","empireStrikesBack@deathstar.com")
user2 = User("Jabba DaHut","tatooineCutie@HuttClanCrimeSyndicate.com")

user1.make_deposit(2000, "savings").display_User_account()
user2.make_deposit(200, "checking").display_User_account()

user1.transfer_money(.99, user2)