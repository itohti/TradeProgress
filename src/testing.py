import requests
from Account import Account
api_url = "https://api-fxtrade.oanda.com/v3/accounts"
headers = {"Authorization": "Bearer 43f492ed5656703c3dd4a844361acade-3949401692b5a2cb95da7e1aef875381"} # This is my token perhaps later into development I will find a way to fetch different tokens based on username and password submitted.
response = requests.get(api_url, headers=headers)

# Creating account class
accounts = [] # should be type Account.

# Testing extracting data from requests
print(response.json()) # So this returns the json. Perhaps we should create a class to represent this json.

for i in response.json()['accounts']:
    account = Account()
    id = i['id']
    response = requests.get(api_url+"/"+id+"/summary", headers=headers)
    balance = response.json()['account']['balance']
    account.set_balance(balance)
    account.set_id(id)
    accounts.append(account)

# so we sucessfully stored the values of my account into a class by fetching it from the API. nice 👍
for i in accounts:
    i.account_summary()
