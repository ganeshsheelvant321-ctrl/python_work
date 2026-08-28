#weight converter
weight=float(input("enter your weight:"))
unit=input("enter the unit kilogramss or pounds?(K or L):")
if unit=="K":
    weight=weight*2.205
    unit="lbs."
    print(f"your weight is:{round(weight,2)}{unit}")
elif unit=="L":
    weight=weight/2.205
    unit="kgs."
    print(f"your weight is:{round(weight,2)}{unit}")
else:
    print("enter the valid unit")
