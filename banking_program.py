def show_balance():
    print(f"your balance is ${balance:.2f}")
def deposite():
    amount=float(input("enter the amount to be deposited:"))
    if amount<0:
        print("amount should not be negative")
        return 0
    else:
        return amount

def withdraw():
    amount=float(input("entr the amount to be withdrawn:"))
    if amount>balance:
        print("insufficiant balance")
        return 0
    elif amount<0:
        print("amount should not be negative")
        return 0
    else:
        return amount

balance=0
is_running=True
while is_running:
    print("1.check balence")
    print("2.deposite")
    print("3.withdrwan")
    print("4.exit")
    choise=input("enter the number from(1-4):")
    if choise=="1":
        show_balance()
    elif choise=="2":
        balance+=deposite()
    elif choise=="3":
        balance-=withdraw()
    elif choise=="4":
        is_running=False
    else:
        print("enter a valid choise")
print("thank you have a good day")    

