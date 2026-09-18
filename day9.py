# #iterables inn python
# numbers=[1,2,3,4,5,67]
# for number in reversed(numbers):
#     print(number)
# fruits=("apple","banana","mango","orange")    
# for fruit in reversed(fruits):
#     print(fruit,end="")
# phone_number={9,1,4,8,3,3,0,8,2,3}   
# for phone in phone_number:
#     print(phone) #not ordered
# name="ganesh sheelvant"
# for username in name:
#     print(username)
# my_dictionary={"A":1,
#                "B":2,
#                "C":3,
#                "D":4}  
# for key,value in my_dictionary.items():
#     print(f"{key}={value}")      

# #membership operators in python
# word="apple"
# fruits=input("enter the name of the fruit:")
# if word in fruits:
#     print(f"{word} is there")
# else:
#     print(f"{word} is not there")

# cars={"lamborginni","swift","mercediss","santro"}
# car=input("enter a car")
# if car in cars:
#     print(f"{car} is there")
# else:
#     print(f"{car} is not there")
# #list comprehensions in python
# double=[ x*2 for x in range(1,11)]  
# print(double) 
# triple=[y*3 for y in range(1,11)] 
# print(triple)
# squares=[z*z for z in range(1,11)]
# print(squares)
# names=["ganesh","appu","mantesh","akash","shivu"]
# hello=[name.upper() for name in names]
# print(hello)
# numbers=[1,2,3,-3.-2,-1,4,5,-6,60,50,5886677]
# positive_nums=[ num for num in numbers if num>=0]
# print(positive_nums)
# negative_nums=[num for num in numbers if num<=0]
# print(negative_nums)
# even_nums=[num  for num in numbers if num%2==0]
# print(even_nums)
# odd_nums=[ num for num in numbers if num%2==1]
# print(odd_nums)
# grades=[80,45,67,89,45,56]
# passing_grade=[ grade for grade in grades if grade>=60]
# print(passing_grade)
#match case statements in python
def calculator(num1,num2,operator):
    match operator:
        case "+":
            return num1+num2
        case "-":
            return num1-num2
        case "*":
            return num1*num2
        case "/":
            return num1/num2
        case "_":
            return "not a valid operator"
print(calculator(2,3,"%"))
#module in python
import math
print(math.pi)
print(math.e)
help("module")
print(help("module"))
import example
result=example.cube(2)
print(result)





