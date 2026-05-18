balance=8000
print("1.withdraw:")
print("2.deposit:")
print("3.check balance:")
choice=int(input("Enter the choice:"))
if choice=="1":
    amount=int(input("Enter the amount:"))
    balance=balance-amount
    print(balance)
elif choice=="2":
    amount=int(input("Enter the amount:"))
    balance=balance+amount
    print(balance)
else:
    print("Invalid balance")
