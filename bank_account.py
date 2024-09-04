# create an account
print('Module:', __name__)
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

if __name__ == '__main__':
    a = account()
    b = account()
    deposit(a, 1000)
    deposit(b, 500)
    withdraw(b, 100)
    withdraw(a, 100)
    print('Balance -> A/C a:', balance(a), 'A/C b:', balance(b))
