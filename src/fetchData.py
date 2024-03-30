import requests
from Account import Account

base_api_url = "https://api-fxtrade.oanda.com/v3/accounts"
account_api_url = "https://api-fxtrade.oanda.com/v3/accounts/{accountID}"
headers = {"Authorization" : "Bearer 43f492ed5656703c3dd4a844361acade-3949401692b5a2cb95da7e1aef875381"}
accounts = []
# Creates account objects and stores it in accounts with the basic information needed.
def fetch_accounts():
    response = requests.get(base_api_url, headers=headers)
    # response was sucessful
    if (response.status_code == 200):
        # gets details of every account.
        for i in response.json()["accounts"]:
            # gets the id of the account
            id = i['id']
            balance = 0
            # requests for more details for the account. See https://developer.oanda.com/rest-live-v20/account-ep/ for more details.
            response = requests.get(account_api_url.format(accountID = id), headers=headers)
            if (response.status_code == 200):
                balance = float(response.json()['account']['balance']) # type cast into a float
                response = requests.get(account_api_url.format(accountID = id)+"/changes", headers=headers, params={"sinceTransactionID": "1"})

                # gets the historic pl of the account.
                historic_balance = fetch_historic_pl(response.json()['changes'])

                account = Account(id, balance, historic_balance)
                accounts.append(account)
                fetch_unrealized_pl(account)
                account.calculate_total_pl()
                account.get_historic_balance()
            else:
                print("Could not get a response.")
    # response unsucessful
    else:
        print("Could not get a response.")


# Fetches the history pl while also getting the initial funding of the account. And gets the spread cost.
def fetch_historic_pl(data):
    historic_pl = []
    for i in data['transactions']:
        if (i['type'] == 'ORDER_FILL'):
            historic_pl.append((i['time'], float(i['pl'])))
    return historic_pl


# Unrealized pl is profits on a position that is currently working.
def fetch_unrealized_pl(account):            
    response = requests.get(account_api_url.format(accountID = account.accountID)+"/openPositions", headers=headers)
    ### TODO: A way to dynamically update the PL is by looping requesting the open positions over and over. Unrealized PL + PL = Total PL
    ### This will be useful for making the graph later.
    total_unrealized_pl = 0
    has_openPositions = False
    for position in response.json()['positions']:
        total_unrealized_pl += float(position['unrealizedPL'])
        has_openPositions = True
    
    account.unrealized_pl = total_unrealized_pl
    account.has_openPositions = has_openPositions

def main():
    fetch_accounts()

    return accounts