class BankAccount:
    def __init__(self, interest_rate, initial_balance=500, over_draft = 25):
        self.interest_rate = interest_rate *.01
        self.balance = initial_balance
        self.over_draft = over_draft
        print(f"New account Created with {self.interest_rate} interest, Balance of ${self.balance}, and over draft fees will cost ${self.over_draft}")
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Depositing ${amount} to UserName's account. \nNew balance is ${self.balance}")
        return self
        
    def withraw(self, amount):
        if(self.balance > amount):
            self.balance -= amount
            print(f"Withdrawing ${amount} from UserName's account. \nNew balance is ${self.balance}")
        else:
            self.balance -= self.over_draft
            print(f"Insufficient funds for withdrawal.  \nOverdraft fee of ${self.over_draft} will be charged. \nNew balance is ${self.balance}")
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        print(f"You've got interest! Current rate is {self.interest_rate}")
        return self
    
    
    
newAccount = BankAccount(1, 1000, 30)
newAccount.deposit(200).withraw(10000).display_account_info().yield_interest().display_account_info().deposit(900).deposit(800).withraw(400).display_account_info().yield_interest().display_account_info()
secondAccount = BankAccount(2)
secondAccount.display_account_info().deposit(100).deposit(500).deposit(200).withraw(100).withraw(50).withraw(50).display_account_info().yield_interest().display_account_info()