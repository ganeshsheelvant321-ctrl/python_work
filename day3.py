#arithmatic operators
# friends=0
# # friends=friends+1
# friends+=1
# friends=friends-2
# friends-=2
# friends=friends*3
# friends*=3
# friends=friends/3
# friends/=3
# friends=friends**2
# friends**=2
# friends=friends%2
# friends%=2
# print(friends)
#some math functions
# x=3.14
# y=4
# z=5
# print(round(x))
# print(abs(y))
# print(pow(x,y))
# print(max(x,y,z))
# print(min(x,y,z))
#math module
# import math
# print(math.pi)
# print(math.e)
# print(math.sqrt(3))
# print(math.ceil(7.999))
# print(math.floor(9.999))
#if statements in python
#1
# age=int(input("enter the age:"))
# if age>=100:
#     print("you are too old to signup")
# elif age>=18:
#     print("you are now signup")
# elif age<=0:
#     print("you havent born yet")
# else:
#     print("you must be 18+ to signup")
#2
# response=input("would you like food?(Y/N):")
# if response=="Y":
#     print("have some food")
# else:
#     print("no food for you")
#3
# online=True
# if online:
#     print("user is online")
# else:
#     print("user is offline")
 
# for_sale=True
# if for_sale:
#     print("this item is for sale")
# else:
#     print("this item is not for sale")

# name=input("enter your name:")
# if name=="":
#     print("you didnt type your name")
# else:
#     print(f"hello{name}")
#logical operators
#and
# temp=20
# if temp>=30 and temp>0:
#     print("temperature is good")
# else:
#     print("temperature is bad")

# #or
# speed=150
# if speed>=100 and speed<=150:
#     print("please slow down your speed")
# else:
#     print("yoou are in over limit speed and you are in denger")

    
# #not
# sunny=False
# if not sunny:
#     print("it's sunny outside")
# else:
#     print("it's clody outside")

# #conditional expression(ternary operator in python)
# num=45
# result="positive" if num>=0 else "negetive"
# print(result)
# x=47
# eoro="EVEN" if x%2==0 else "ODD"
# print(eoro)
# a=3
# b=5
# max_num=a if a>b else b
# print(max_num)
# min_num=a if a<b else b
# print(min_num)
# temp=34
# weather="hot" if temp>20 else "cold"
# print(weather)
# user_role="Ganesh"
# acess_level="full acess" if user_role=="admin" else "limited acess"
# print(acess_level)
#string methods
name="ganesh"
phone_num=1-234-456-678
print(len(name))
print(name.find("a"))
print(name.rfind("h"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.replace("ganesh","mantesh"))
phone_num = "98765-43210"

print(phone_num.count("-"))
