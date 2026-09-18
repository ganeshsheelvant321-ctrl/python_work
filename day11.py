list=[1,1,1,0,0,1,1,1,1]
count=0
max=0
for num in list:
    if num==1:
        count+=1
        if count>max:
            max=count
    else:
        count=0
print(max)                
    