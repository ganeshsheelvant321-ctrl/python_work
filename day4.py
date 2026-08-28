#string indexing
# credit_number="1233-465-4746-348574"
# print(credit_number[2])
# print(credit_number[0:4])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-3])
# print(credit_number[::2])
# print(credit_number[::3])
# last_digit=credit_number[-6:]
# print(last_digit)
# print(credit_number[::-1])
#python format specifier
# price1=3.141599
# price2=-956.7879
# price3=160000000000
# print(f"price1 is ${price1:.2f}")
# print(f"price2 is ${price2:.2f}")
# print(f"price3 is ${price3:.2f}")
# print(f"price1 is ${price1:10}")
# print(f"price2 is ${price2:10}")
# print(f"price3 is ${price3:10}")
# print(f"price1 is ${price1:010}")
# print(f"price2 is ${price2:010}")
# print(f"price3 is ${price3:010}")
# print(f"price1 is ${price1:<}")
# print(f"price1 is ${price2:<}")
# print(f"price1 is ${price3:<}")
# print(f"price1 is ${price1:>}")
# print(f"price1 is ${price2:>}")
# print(f"price1 is ${price3:>}")
# print(f"price1 is ${price1:+}")
# print(f"price2 is ${price2:+}")
# print(f"price3 is ${price3:+}")
# print(f"price1 is ${price1:=}")
# print(f"price3 is ${price3: }")
# print(f"price3 is ${price3:,}")
#while loop in python
#1
# name=input("enter your name:")
# while name=="":
#     print("you did not enter your name")
#     name=input("enter your name:")

# print(f"hello {name}")
#2
# age=int(input("enter your age:"))
# while age<=0:
#     print("age cant be negative")
#     age=int(input("enter your age:"))

# print(f"you are {age} years old")
#3
# food=input("enter a food you like(q to quite):")
# while not food=="q":
#     print(f"you like {food}")
#     food=input("enter another food you like(q to quite):")

# print("bye")
#4
# num=int(input("enter a number between 1 and 10:"))
# while num<1 or num>10:
#     print(f"{num} is not valid")
#     num=int(input("enter a number between 1 and 10:"))

# print(f"youur number is:{num}")  
# 5
# i=1
# while i<=100:
#     print(i)
#     i=i+1
#6
# i=100
# while i>1:
#     print(i)
#     i-=1
#7
# n=int(input("enter the number:"))
# i=1
# while i<=100:
#     print(i*n)
#     i+=1
#8
# sum=0
# i=1
# n=100
# while i<=100:
#     sum=sum+i
#     i+=1
# print(sum)
#9
# fact=1
# i=1
# n=7
# while i<=5:
#     fact=fact*i
#     i+=1
# print(fact)
#for loop in python
# for x in range(1,11):
#     print(x)

# for x in reversed(range(1,11)):
#     print(x)

# credit_card="123-456604-3332-2323-4556"
# for x in credit_card:
#     print(x)    

#break and continue statements in python
# for x in range(1,23):
#     if x==13:
#         continue
#     else:
#         print(x)

# for x in range(3,20):
#     if x==13:
#         break
#     else:
#         print(x)
#nested loops in python
# for x in range(5):
#     for y in range(1,10):
#         print(y,end=" ")
#     print()  
# row=int(input("enter the no of rows:"))
# columns=int(input("enter the no of columns:"))
# symbol=input("enter the symbol to be used:")
# for x in range(row):
#     for y in range(columns):
#         print(symbol,end=" ")

#     print()
#timer function in python
# import time
# time.sleep(3)
# print("TIME'S UP!")
# my_time=int(input("enter your time:"))
# for i in range(my_time):
#     print(i)
#     time.sleep(1)

# print("times up!")
#lists in python
# fruits=["apple","banana","mango","coconut"]
# print(fruits)
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])
# # print(fruits[4])#error
# for fruit in fruits:
#     print(fruit)

# print(fruits[::-1])  
# #list functions
# print(dir(fruits))  
# print(len(fruits))
# print("pinaeapple" in fruits)
# fruits[0]="ganesh"
# print(fruits)
# fruits.append("icecream")
# fruits.remove("icecream")
# fruits.insert(0,"orange")
# fruits.sort()
# fruits.reverse()
# # fruits.clear()
# fruits.index("coconut")
# print(fruits.count("banana"))
# print(fruits)
#sets in python
# cars={"ferrari","lamberginni","mercedis","toyata"}
# print(cars)
# # print(cars[0])#sets are unorderd
# print(len(cars))
# print("audi" in cars)
# cars.add("audi")
# cars.remove("audi")
# cars.pop()
# cars.clear()
# print(cars)
#tuples in python
laptops=("lenavo","asus","acer","thinkpad","macbook")
print(laptops)
print(len(laptops))
print(laptops[0])
print("dell" in laptops)
# print(help(tuple))
print(laptops.index("lenavo"))
print(laptops.count("lenavo"))
for x in laptops:
    print(x)

idx=0
for idx in range(len(laptops)):
    print(laptops[idx])
idx+=1