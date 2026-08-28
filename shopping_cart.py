foods=[]
prices=[]
total=0
while True:
    food=input("enter food you like (q to quite):")
    if food.lower()=="q":
        break
    else:
        price=float(input("enter the price of a food:$"))
        foods.append(food)
        prices.append(price)

print("-------YOYR CART-------") 
for x in foods:
    print(x,end=" ") 


for y in prices:
    total=total+y

print()
print(f"your total is:${total}")

    