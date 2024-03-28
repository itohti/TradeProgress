class Account:
    # This will store the ID
    accountID = ""

    # This will store the balance of the account.
    accountBalance = 0


    def __init__(self):
        self.accountID = ""
        self.accountBalance = 0
    
    def set_balance(self, balance):
        self.accountBalance = balance
    
    def set_id(self, id):
        self.accountID = id

    def account_summary(self):
        print(f"Account: {self.accountID} Balance: {self.accountBalance}")
