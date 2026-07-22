student_Name = input("Enter your name : ")
mark_1 = float(input("Enter your mark for subject 1 : "))
mark_2 = float(input("Enter your mark for subject 2 : "))
mark_3 = float(input("Enter your mark for subject 3 : "))

average = (mark_1 + mark_2 + mark_3)/3

if average >= 80:
    grade = "A"
    status = "Pass with Distiction!!!"
    print(f"Your GRADE is : " + grade + " and your STATUS is : " + status)
elif average >= 70 and average <= 79:
    grade = "B"
    status = "Pass"
    print(f"Your GRADE is : " + grade + " and your STATUS is : " + status)
elif average >= 60 and average <= 69:
    grade = "C"
    status = "Pass"
    print(f"Your GRADE is : " + grade + " and your STATUS is : " + status)
elif average >= 50 and average <= 59:
    grade = "D"
    status = "Pass"
    print(f"Your GRADE is : " + grade + " and your STATUS is : " + status)
else:
    grade = "F"
    status = "Failed"
    print(f"Your GRADE is : " + grade + " and your STATUS is : " + status)


intervetion = []

if mark_1 < 40:
    intervetion.append("Sbuject 1")
if mark_2 < 40:
    intervetion.append("Subject 2")
if mark_3 < 40:
    intervetion.append("Subject 3")
        
if intervetion:
    print("You need an intervesion for : " + str(intervetion))
else:
    print("No intervesion is required!!")