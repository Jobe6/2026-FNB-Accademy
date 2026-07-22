weight = float(input("Enter your weight : "))
unit = input("Enter your weight units : ")

if unit.upper() == "K":
    convert = weight / 0.45
    print("Weight in LBs is : " + str(convert))
else:
    convert = weight * 0.45
    print("Weight in Kgs is : " + str(convert))

