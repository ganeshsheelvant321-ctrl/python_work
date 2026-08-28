num_pad=((1,2,3),
         (4,5,6),
         (7,8,9),
         ("#",0,"*"))
for x in num_pad:
    for num in x:
        print(num ,end="  ")
    print()    