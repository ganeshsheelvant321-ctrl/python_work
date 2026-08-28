unit=input("is your temp in celsius or farenheit(C OR F):")
temp=float(input("enter the temperature:"))
if unit=="C":
    temp=round((9*temp)/5+32,1)
    print(f"the temperature is in fahrenheit is:{temp}F")
elif unit=="F":
    temp=round((temp-32)*5/9,1)
    print(f"the temperature is in celsius is:{temp}C")
else:
    print(f"{unit} is an invalid unit of measurement")