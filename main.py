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

# ------------------------------------------------------------
# 4. CALCULATE THE AVERAGE
# ------------------------------------------------------------

# Prevent division by zero.
if attempted_days > 0:
    average_score = total_score / attempted_days
else:
    average_score = 0

# ------------------------------------------------------------
# 5. CREATE ELIGIBILITY CONDITIONS
# ------------------------------------------------------------

graduation_eligible = (
    graduation_year >= 2025
    and graduation_year <= 2027
)

attendance_eligible = attendance >= 75
practice_count_eligible = attempted_days >= 6
average_eligible = average_score >= 70
critical_score_clear = not critical_score_found
passed_days_eligible = passed_days >= 4

placement_ready = (
    graduation_eligible
    and attendance_eligible
    and practice_count_eligible
    and average_eligible
    and critical_score_clear
    and passed_days_eligible
    and project_completed
    and profile_verified
)


# ------------------------------------------------------------
# 6. DETERMINE FINAL STATUS
# ------------------------------------------------------------

# Check conditions in this priority:
# 1. No practice attempted
# 2. Critical score found
# 3. Fewer than six attempts
# 4. Fewer than four passed days
# 5. Average below 70
# 6. Attendance below 75
# 7. Graduation year not eligible
# 8. Project incomplete
# 9. Profile not verified
# 10. Ready for Mock Interview

final_status = ""
primary_blocker = ""
next_action = ""

if attempted_days == 0:
    final_status = "Practice Not Evaluated"
    primary_blocker = "No practice attempted"
    next_action = "Attempt the required coding practices"

elif critical_score_found:
    final_status = "Critical Support Required"
    primary_blocker = "A critical score exists"
    next_action = "Revise the concepts from the first critical day"

elif attempted_days < 6:
    final_status = "Practice Incomplete"
    primary_blocker = "Fewer than six practices were attempted"
    next_action = "Complete at least six practice days"

elif passed_days < 4:
    final_status = "Insufficient Passed Practices"
    primary_blocker = "Fewer than four practices were passed"
    next_action = "Pass at least four coding practices"

elif average_score < 70:
    final_status = "Practice Improvement Required"
    primary_blocker = "Average score is below 70"
    next_action = "Improve the average score to at least 70"

elif attendance < 75:
    final_status = "Attendance Improvement Required"
    primary_blocker = "Attendance is below 75"
    next_action = "Improve attendance to at least 75 percent"

elif not graduation_eligible:
    final_status = "Graduation Criteria Not Met"
    primary_blocker = "Graduation year is not eligible"
    next_action = "Check the eligible graduation-year requirement"

elif not project_completed:
    final_status = "Project Submission Required"
    primary_blocker = "Project is incomplete"
    next_action = "Complete the required project"

elif not profile_verified:
    final_status = "Profile Verification Required"
    primary_blocker = "Profile is not verified"
    next_action = "Get the student profile verified"

else:
    final_status = "Ready for Mock Interview"
    primary_blocker = "None"
    next_action = "Proceed to the placement mock interview"


# ------------------------------------------------------------
# 7. DISPLAY FINAL REPORT
# ------------------------------------------------------------

print()
print("=" * 50)
print("           PREPTRACK REPORT")
print("=" * 50)

print(f"Student Name          : {student_name}")
print(f"Registration Number   : {registration_number}")
print(f"Graduation Year       : {graduation_year}")
print(f"Attendance            : {attendance}%")

print()
print(f"Attempted Days        : {attempted_days}")
print(f"Absent Days           : {absent_days}")
print(f"Passed Days           : {passed_days}")
print(f"Failed Days           : {failed_days}")

print()
print(f"Strong Days           : {strong_days}")
print(f"Satisfactory Days     : {satisfactory_days}")
print(f"Needs Improvement Days: {improvement_days}")
print(f"Critical Days         : {critical_days}")

print()
print(f"Total Score           : {total_score}")
print(f"Average Score         : {average_score:.2f}")

# Display highest and lowest values only when
# at least one practice was attempted.
if first_attempt_found:
    print(f"Highest Score         : {highest_score}")
    print(f"Highest Score Day     : {highest_score_day}")
    print(f"Lowest Score          : {lowest_score}")
    print(f"Lowest Score Day      : {lowest_score_day}")
else:
    print("Highest Score         : Not Available")
    print("Highest Score Day     : Not Available")
    print("Lowest Score          : Not Available")
    print("Lowest Score Day      : Not Available")

# Display first critical details only when
# a critical score exists.
print()
if critical_score_found:
    print(f"Critical Score Found  : Yes")
    print(f"First Critical Day    : {first_critical_day}")
    print(f"First Critical Score  : {first_critical_score}")
else:
    print(f"Critical Score Found  : No")
    print("First Critical Day    : Not Applicable")
    print("First Critical Score  : Not Applicable")

print()
print(f"Final Status          : {final_status}")
print(f"Primary Blocker       : {primary_blocker}")
print(f"Next Action           : {next_action}")

print("=" * 50)