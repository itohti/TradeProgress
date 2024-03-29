import fetchData
import matplotlib.pyplot as plt
import datetime
import pandas as pd

# This will update the data for any open positions.
def update_data(account, dataframe):
    if (account.has_openPositions):
       pass # Working on here rn ##########################

# Main entry for the program.
def main():
    accounts = []
    accounts = fetchData.main()
    while(True):
        fetchData.fetch_unrealized_pl()
        for account in accounts:
            dataframe = pd.DataFrame(account.historic_balance, columns=['Time', 'Balance'])
            account.account_summary()


main()