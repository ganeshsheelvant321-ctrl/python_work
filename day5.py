#2d lists,2d tuples,2d sets
# fruiets=["apple","banana","mango","pineapple","orange"]
# gadgets=["phone","laptops","watchs","hair drir"]
# books=  ["bhagvadgeeta","ramayana","mahabharat","ego"]
# items=[fruiets,gadgets,books]
# print(items)
# print(items[2])
# print(items[0][0])
# print(items[0][1])
# print(items[0][2])
# print(items[0][3])
# print(items[1][0])
# print(items[1][1])
# print(items[1][2])
# print(items[1][3])
# print(items[2][0])
# print(items[2][1])
# print(items[2][2])
# print(items[2][3])
# items=[["apple","banana","mango","pineapple","orange"],
#        ["phone","laptops","watchs","hair drir"],
#        ["bhagvadgeeta","ramayana","mahabharat","ego"]]
# print(items)
# for collection in items:
#     for item in collection:
#         print(item ,end=" ")
#     print()  
#dictionaries in python
students={
    "name":"ganesh",
    "fathername":"suryakant",
    "mother name":"sunita",
    "class":"engineering 3rd year",
    "cgpa":"8.41",
    "usn":"1da24ec038",
    "fav_sub":"mathematics"
}
print(type(students))
print(students.get("usn"))
print(students.get("marks"))
if students.get("marks"):
    print("this student has written exam")
else:
    print("this student has not written exam")
print(students.update({"marks":"88%"}))  
print(students.pop("marks"))
print(students.popitem())
print(students.keys())
print(students) 
for key in students.keys():
    print(key,end=" ") 

print(students.values())
for value in students.values():
    print(value)

print(students.items())
for key,value in students.items():
    print(f"{key}:{value}")

food={"pizza":89,
      "parata":90,
      "popcorn":100
      }
print(food.get("pizza"))



