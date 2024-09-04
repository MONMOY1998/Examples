print("My name is: ", __name__)
# create an account
def account():
    return {'balance': 0} # dictionary 

# Deposit and withdrawal
def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']

# get balance
def balance(account):
    return account['balance']
