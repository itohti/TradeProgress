# This class holds data from the get requests /v3/accounts/{accountID}.
class Account:
    # This will store the ID.
    accountID = ""

    # This will store the balance of the account.
    accountBalance = 0

    # Historical balance.
    historic_pl = []

    # Unrealized PL
    unrealized_pl = 0
    
    # Is the total profit of the account. Unrealized pl + realized pl.
    total_pl = 0

    # Is the historic_balance. Follows the pl of the account and does not account funding as it is added at the beginning.
    historic_balance = []

    # A flag to see if the account has any open positions.
    has_openPositions = False

    def __init__(self, accountID, accountBalance, historic_pl):
        self.accountID = accountID
        self.accountBalance = accountBalance
        self.historic_pl = historic_pl

    
    def set_balance(self, balance):
        self.accountBalance = balance
    
    # adds up the historic pl of the account there is a better way to get this data tho. It is fetched through v3/accounts/{accountID}
    # The reason why I get historic pl is to plot the graph of how balance moved over time.
    def get_total_historic_pl(self):
        profit = 0
        for i in self.historic_pl:
            profit += i[1]
        return profit
    
    # gets the running balance and adds all points to an array.
    def get_historic_balance(self):
        running_balance = self.accountBalance - self.total_pl
        for i in self.historic_pl:
            running_balance += i[1]
            self.historic_balance.append((i[0], running_balance))

    # Unrealized pl + realized pl = total pl
    def calculate_total_pl(self, unrealized_pl):
        self.total_pl = unrealized_pl + self.get_total_historic_pl()
    
    # prints notable variables of this class.
    def account_summary(self):
        print(f"Account: {self.accountID} Balance: {self.accountBalance}")
        print(f"Unrealized pl: {self.unrealized_pl}")
        print(f"Total profit: {self.total_pl}")
        print(f"Initial balance: {self.accountBalance-self.total_pl}") # initial balance will not equal to funding if there has been transactions because of spread cost.
