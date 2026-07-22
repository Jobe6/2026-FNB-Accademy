students = [
    {"Name": "Sboniso", "Maths": 90, "English": 89, "Physics": 67},
    {"Name": "Senzo", "Maths": 60, "English": 98, "Physics": 70},
    {"Name": "Sihle", "Maths": 100, "English": 80, "Physics": 73},
    {"Name": "Joe", "Maths": 60, "English": 86, "Physics": 70},
    {"Name": "Haland", "Maths": 59, "English": 84, "Physics": 65}
]

results = []

# Process each student
for student in students:
    average = (student["Maths"] + student["English"] + student["Physics"]) / 3

    if average >= 80:
        grade = "A"
        status = "Pass"
    elif average >= 70:
        grade = "B"
        status = "Pass"
    elif average >= 60:
        grade = "C"
        status = "Pass"
    elif average >= 50:
        grade = "D"
        status = "Pass"
    else:
        grade = "F"
        status = "Fail"

    results.append({
        "Name": student["Name"],
        "average": round(average, 2),
        "grade": grade,
        "status": status
    })

# Collect all marks
marks = []
for m in students:
    marks.extend([m["Maths"], m["English"], m["Physics"]])

# Class statistics
total_avg = sum(r["average"] for r in results)
class_avg = total_avg / len(results)
highest_mark = max(marks)
lowest_mark = min(marks)

# Print report
print("\n--- CLASS REPORT ---")
for r in results:
    print(f"{r['Name']:10} | Average: {r['average']:5} | Grade: {r['grade']} | Status: {r['status']}")

print("\n--- CLASS STATISTICS ---")
print(f"Class Average : {round(class_avg, 2)}")
print(f"Highest Mark  : {highest_mark}")
print(f"Lowest Mark   : {lowest_mark}")

# Search loop
while True:
    search_name = input("\nEnter a student name to search (or type 'exit' to quit): ").capitalize()
    if search_name.lower() == "exit":
        print("Exiting search. Goodbye!")
        break

    found = False
    for r in results:
        if r["Name"] == search_name:
            print(f"Result for {r['Name']}: Average {r['average']}, Grade {r['grade']}, Status {r['status']}")
            found = True
            break

    if not found:
        print("Student not found. Try again.")
