#arbitary arguments in python

def substract(*args):
  total=0
  for arg in args:
    total+=arg
  return total
print(substract(1,2,3)) 

def user_name(*args):
  for arg in args:
    print(arg,end="")
user_name("Engineer"," ","ganesh"," ","sheelvant") 
print()

def calculate_percentage(*args):
  percentages=[]
  for arg in args:
    percentage=(arg/600)*100
    percentages.append(percentage)
  return percentages
print(calculate_percentage(600,500,700))

#kargs
def display (*args,**kargs):
  for arg in args:
    print(arg,end=" ")
  print() 
  if "fav_sport" in kargs:
    print(f"{kargs.get('name')} {kargs.get('surname')} {kargs.get('fav_sport')}")
  else:
     print(f"{kargs.get('name')} {kargs.get('surname')}")

  print(f"{kargs.get('name')} {kargs.get('surname')}")
  print(f"{kargs.get('fav_sub')},{kargs.get('dream')}") 
#   for key,value in kargs.items():
#     print(f"{key}:{value}") 

 

display("dr","ganesh","sheelvath","is","very","good","human",
        name="ganesh",
        surname="sheelvant",
        fav_sport="cricket",
        fav_sub="maths",
        dream="to become a software engineer")  

def school_info(**kwargs):
  for key,value in kwargs.items():
    print(f"{key}:{value}")

school_info(name_of_school="shantiniketan",
                  area="hiremet_colony",
                  city="basavakalyan",
                  district="bidar",
                  name_of_principle="chanveer sir",
                  recognization_for="good education",
                  facility="privide smart_class,digital board,practical experience of labs")