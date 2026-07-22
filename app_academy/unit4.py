Age = int(input("Enter your age : "))
Gender = input("Enter your gender : ").upper()

if Age >= 18:
    print("You can enter!!")
if Gender.upper() == "F":
    print("Go to the Female side on your LEFT!!")
if Gender.upper() == "M":
    print("Go to the Male side on your Right!!!")
else:
    print("Your inputs are invalid!! try again!!")