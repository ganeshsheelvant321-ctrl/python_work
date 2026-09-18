sum_odd_digits=0
sum_even_digit=0
total=0
#step1
card_number=input("enter the credit card number")
card_number=card_number.replace("-","")
card_number=card_number.replace(" ","")
card_number=card_number[::-1]
#step2
for x in card_number[::2]:
    sum_odd_digits+=int(x)
#step3
for y in card_number[1::2]:
    x=int(x)*2
    if x>=10:
        sum_even_digit+=(1+(x%10))
    else:
        sum_even_digit+=x
#step4
total=sum_even_digit+sum_odd_digits
#step5
if total%10==0:
    print("VALID")  
else:
    print("INVALID")      
    
