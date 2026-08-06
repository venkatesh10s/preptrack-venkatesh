print("=" * 50)
print("           PREPTRACK APPLICATION")
print("=" * 50)
# Validate that the student name is not empty.
student_name = input("Enter student name: ")
while student_name == "":
    print("Student name cannot be empty.")
    student_name = input("Enter student name: ")
registration_number = input("Enter registration number: ")
graduation_year = int(input("Enter graduation year: "))
graduation_eligible = (
    graduation_year >= 2025
    and graduation_year <= 2027
)
if not graduation_eligible:
    print("You are not eligible for graduation.")
    graduation_year = int(input("Enter graduation year: "))

# Validate attendance between 0 and 100.
while True:
    attendance = float(input("Enter attendance percentage: "))
    if attendance >= 0 and attendance <= 100:
        break
    print("Invalid attendance. Enter a value between 0 and 100.")

# Accept only yes or no.
while True:
    project_input = input(
        "Has the student completed the required project? Enter yes or no: "
    )
    if project_input == "yes" or project_input == "no":
        break
    print("Invalid input. Enter only yes or no.")

# Convert project_input into True or False.
if project_input == "yes":
    project_completed = True
else:
    project_completed = False

# Accept only yes or no.
while True:
    profile_input = input(
        "Is the student profile verified? Enter yes or no: "
    )
    if profile_input == "yes" or profile_input == "no":
        break
    print("Invalid input. Enter only yes or no.")

# Convert profile_input into True or False.
if profile_input == "yes":
    profile_verified = True
else:
    profile_verified = False