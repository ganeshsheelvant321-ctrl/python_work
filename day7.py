#functions in python
#functions are the block of codes that are use to reuse code multiple times
#fun() after the function to invoke it
def happy_birthday(name,age):
    print(f"happy birthaday to {name}")
    print(f"you are {age} years old")
    print(f"happy birthday to you!")

happy_birthday("ganesh",18)
happy_birthday("mega",19)

def add(x,y):
    z=x+y
    return z
def subsratct(x,y):
    z=x-y
    return z
def multiply(x,y):
    z=x*y
    return z
def divide(x,y):
    z=x/y
    return z

print(add(1,2))
print(subsratct(1,2))
print(multiply(1,2))
print(divide(1,2))

def invoice(username,amount,duedate):
    print(f"hello{username}")
    print(f"your bill of${amount:.2f} is due is {duedate}")
invoice("ganesh",67,"1/1/2021")


def username(first,last):
    first=first.capitalize()
    lat=last.capitalize()
    return first+" "+last
fullname=username("ganesh","sheelvant")
print(fullname)

def sum_of_n(n):
    sum=0
    for i in range(0,n):
        sum=sum+i
    return sum
summation=sum_of_n(34)
print(summation)
#default aruguments in python
def net_price(list_price,discount=0,tax=0.06):
    return list_price*(1-discount)*(1+tax)
print(net_price(30))
import time
def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")    

count(10)
#keyword arguments
def hello(greeting,title,first,last):
    return f"{greeting} {title} {first} {last}"
print(hello(title="mr",first="ganesh",last="sheelvant",greeting="hello"))
def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"


print(get_phone(91,23,2346,3466))
    