#Variable(to store data/as our location
#bool : true or false
#if we are round up something: round(what are we rounding, how many decimals)
first_name = input("Enter your first name : ").upper().title()
surname = input("Enter your surname : ").upper().title()
age = int(input("Enter your age : "))
favorite_number = float(input("Enter your favorite number : "))

age_months = age * 12
rounded_number = round(favorite_number, 2)

print(f"Welcome, " + first_name + " " + surname)
print(f"Your age in months is : " + str(age_months) + " months")
print(f"Your rounded number is : " + str(rounded_number))
