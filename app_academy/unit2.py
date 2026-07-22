#creating an email
first_name = input("Enter your first  name : ").strip()
last_name = input("Enter your last name : ").strip() 
bio = input("Enter your bio : ").strip()

username = f"{first_name[0]}{last_name}"
print(f"Your email is : " + username.lower() + "@gmail.com")
print(f"Your bio is : " + bio)