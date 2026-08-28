menu={"Pizza": 250,
    "Burger": 150,
    "Biryani": 180,
    "Dosa": 80,
    "Idli": 50,
    "Fried Rice": 120,
    "Noodles": 130,
    "Sandwich": 100,
    "Paneer": 200,
    "Ice Cream": 70
    }
cart=[]
total=0
print("------------MENU------------")
for key,value in menu.items():
    print(f"{key:10}:{value:.2f}")
print("----------------------------")  
while True:
    food=input("enter the food you like (q to quite):")
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food) 

print("------------------YOUR ORDER-----------------")  
for x in cart:
    total+=menu.get(x)
    print(x, end=" ")     
print()
print(f"your total is:${total:.2f}")        