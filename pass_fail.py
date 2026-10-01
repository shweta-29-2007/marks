# Get marks for 4 subjects
mark1 = int(input("Enter marks for Subject 1: "))
mark2 = int(input("Enter marks for Subject 2: "))
mark3 = int(input("Enter marks for Subject 3: "))
mark4 = int(input("Enter marks for Subject 4: "))

passed = mark1 >= 40 and mark2 >= 40 and mark3 >= 40 and mark4 >= 40

# Check eligibility
if not passed:
    print("Student is FAIL")
else:
    print("Student is PASS")

# Grading section
average = (mark1 + mark2 + mark3 + mark4) / 4
if not passed:
    grade = "F"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "E"

print(f"Grade: {grade}")