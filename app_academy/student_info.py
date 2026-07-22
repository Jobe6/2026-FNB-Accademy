first_name = input("Enter your first name : ")
surname = input("Enter your surname : ")
age =  int(input("Enter your age : "))
fav_Number = float(input("Enter your favorite number : "))

print(f"Welcome, {first_name}  {surname}! \n")

print("Name in UPPERCASES : ", f"{first_name}  {surname}".upper())
print("Name in Tittle Case : ", f"{first_name}  {surname}".title())

Age = age * 12;
print(f"Age in months is : " + str(Age))

print(f"2 decimals of favorite number is : " + str(round(fav_Number, 2)) + "\n")

print("Below is all the data type of each printed data!!!!: ")
print("First name(s) has a data type of : ", type(first_name))
print("surname has a data type of : ", type(surname))
print("Age has a data type of : ", type(Age))
print("Favorite number has a data type of : ", type(fav_Number))

