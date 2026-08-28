username=input("enter the username")
if len(username)>12:
    print("your username cant be more than 12 letters")
elif not username.find(" ")==-1:
    print("your username cant be contain spaces")
elif not username.isalpha():
    print("your user name cant be contains digits")
else:
    print(f"hello {username}")