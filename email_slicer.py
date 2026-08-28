#email_slicer programm
email=input("enter your email:")
user_name=email[:email.index("@")]
domain_name=email[email.index("@")+1:]
print(f"your user name is:{user_name} and domain name is:{domain_name}")