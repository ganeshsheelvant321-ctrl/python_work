#shopping cart
item=input("what item would you like to buy :")
price=float(input("what is the price?:"))
quantity=int(input("how many would you want buy?:"))
total=quantity*price
print(f"you have bought{quantity} X {item}\s")
print(f"your total is:${total}")
