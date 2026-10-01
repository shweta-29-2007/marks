# Get marks for 4 subjects
mark1 = int(input("Enter marks for Subject 1: "))
mark2 = int(input("Enter marks for Subject 2: "))
mark3 = int(input("Enter marks for Subject 3: "))
mark4 = int(input("Enter marks for Subject 4: "))

# Check eligibility
if mark1 < 40 or mark2 < 40 or mark3 < 40 or mark4 < 40:
    print("Student is FAIL")
else:
    print("Student is PASS")