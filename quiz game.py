quitions=["what is the scientific name of mango?:",
          "what is the full form of ai?:",
          "what is the value of pi?:",
          "who ivented zero?:",
          "who invented mathematics?:"]

options=(("A.mangifera indica","B.volvo","C.cat","D.dog"),
         ("A.artificial intelligence","B.aeronotical intelligence","C.arithmatic intelligence","D.aerospesic intelligence"),
         ("A.4","B.56","C.3.14","D.4.4"),
         ("A.pythagoras","B.thels","C.aryabhat","D.shrinivas ramanujan"),
         ("A.aryabhat","B.no single person","C.shrinivas ramanujan","D.pythagorous"))

answers=["A","A","C","C","B"]
guesses=[]
quition_num=0
score=0
for quition in quitions:
    print("-----------------------------------------")
    print(quition)
    for option in options[quition_num]:
        print(option)
    guess=input("enter (A,B,C,D):").upper()    
    guesses.append(guess)
    if guess==answers[quition_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[quition_num]} is the correct answer")
    quition_num+=1  
print("-------------------------------------------------------")  
print(              "RESULT"                   )    
print("answers:",end="")
for answer in answers:
    print(answer,end="")
print() 
print("guesses:",end="") 
for guess in guesses:
    print(guess,end="")  
print()  
score=int(score/len(quitions)*100)  
print(f"your score is:{score}%")