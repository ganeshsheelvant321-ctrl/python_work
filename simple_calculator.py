#simple calculator
operator=input("enter the operator(+,-,*,/):")
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
if operator=="+":
    sum=num1+num2
    print(sum)
elif operator=="-":
    diff=num1-num2
    print(diff)
elif operator=="*":
    product=num1*num2
    print(product)
elif operator=="/":
    division=num1/num2
    print(division)
else:
    print(f"{operator} is not a valid operator")

