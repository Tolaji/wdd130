print("~\n~~~~~~~ Grade calculator program ~~~~~~~\n")

grade_percent = float(input("What is your grade percentage? "))
grade = ""

if grade_percent >= 90:
    grade = "A"
elif grade_percent >= 80:
    grade = "B"
elif grade_percent >= 70:
    grade = "C"
elif grade_percent >= 60:
    grade = "D"
elif grade_percent >= 50:
    grade = "E"
else:
    grade = "F"
    print()

positive = "+"
negative = "-"


print("Your Grade is:", grade)

if grade_percent >= 70:
    print("Congratulations, you passed the course.")
else:
    print(
        "Sorry you failed the course, not to worry, am sure you will do better next time."
    )

print()
