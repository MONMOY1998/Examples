from bankaccount import account, deposit, withdraw, balance
a = account()
b = account()
deposit(a, 1000)
deposit(b, 500)
withdraw(b, 100)
withdraw(a, 100)
print('Balance -> A/C a:', balance(a), 'A/C b:', balance(b))
