print("=" * 50)
print("           PREPTRACK APPLICATION")
print("=" * 50)

# --------------------------------------------------
# 1. COLLECT STUDENT DETAILS
# --------------------------------------------------

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

# ------------------------------------------------------------
# 2. INITIALIZE COUNTERS AND VARIABLES
# ------------------------------------------------------------

total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0

# ------------------------------------------------------------
# 3. PROCESS SEVEN PRACTICE DAYS
# ------------------------------------------------------------

for day in range(1, 8):

    # Use a while loop to accept only:
    # -1 or a score between 0 and 100.
    while True:
        score = int(
            input(
                f"Enter Day {day} score from 0 to 100, "
                "or -1 for absent: "
            )
        )
        if score == -1 or (score >= 0 and score <= 100):
            break
        print("Invalid score. Enter -1 or a value between 0 and 100.")

    # Handle absence.
    if score == -1:
        absent_days += 1
        print(f"Day {day} Result: Absent")
        continue

    # Increase attempted_days and total_score.
    attempted_days += 1
    total_score += score

    # Initialize or update:
    # highest_score, highest_score_day,
    # lowest_score and lowest_score_day.
    if not first_attempt_found:
        highest_score = score
        highest_score_day = day

        lowest_score = score
        lowest_score_day = day

        first_attempt_found = True
    else:
        if score > highest_score:
            highest_score = score
            highest_score_day = day

        if score < lowest_score:
            lowest_score = score
            lowest_score_day = day

    # Classify the score:
    # 75-100  -> Strong
    # 60-74   -> Satisfactory
    # 40-59   -> Needs Improvement
    # 0-39    -> Critical
    if score >= 75:
        strong_days += 1
        print(f"Day {day} Result: Strong")
    elif score >= 60:
        satisfactory_days += 1
        print(f"Day {day} Result: Satisfactory")
    elif score >= 40:
        improvement_days += 1
        print(f"Day {day} Result: Needs Improvement")
    else:
        critical_days += 1
        print(f"Day {day} Result: Critical")

    # Count passed and failed days.
    if score >= 60:
        passed_days += 1
    else:
        failed_days += 1

    # Store only the first critical day and score.
    if score < 40:
        if not critical_score_found:
            critical_score_found = True
            first_critical_day = day
            first_critical_score = score