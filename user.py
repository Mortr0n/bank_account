import bank_account
class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.bank_account = bank_account.BankAccount(2, 500, 20)
        
    def make_deposit(self, amount):
        self.bank_account.display_account_info()
        self.bank_account.deposit(amount)
        # print(f"Depositing ${amount} in to account. \n{self.name}'s New balance total is ${self.bank_account}")
        return self
        
    def make_withdrawal(self, amount):
        self.bank_account.withraw(amount)
        return self
    
    def transfer_money(self, other_user, amount):
        if(self.bank_account.balance > amount):
            print(f"Transferring ${amount} from {self.name} to {other_user.name}")
            self.bank_account.withraw(amount)
            other_user.bank_account.deposit(amount)
        return self
            

    def display_user_balance(self):
        print(f"{self.name}'s ")
        self.bank_account.display_account_info()
        # print(f"{self.name}'s current account balance is", self.bank_account.display_account_info())
        return self
    



chris = User("Chris", "cmsl4y3r@gmail.com")
misty = User("Misty", "email@email.com")
chris.make_deposit(100).make_withdrawal(50).make_deposit(1000).make_deposit(500).make_withdrawal(100).display_user_balance()
misty.make_deposit(1000).make_deposit(500).make_withdrawal(50).make_withdrawal(100).make_deposit(200).make_withdrawal(100).display_user_balance().transfer_money(chris, 100).display_user_balance()
chris.display_user_balance().bank_account.yield_interest().display_account_info()
