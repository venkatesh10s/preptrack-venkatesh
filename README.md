# PrepTrack Application

A command-line Python application that tracks a student's 7-day coding practice performance, validates eligibility criteria, and determines placement interview readiness.

## Table of Contents
- Project Overview
- Features
- Python Concepts Used
- How to Run
- Sample Output
- Individual Contribution

## Project Overview
PrepTrack collects a student's profile details and 7 days of practice scores, then generates a complete performance report. The report includes score classification, attendance and eligibility checks, and a final placement-readiness decision with a recommended next action.

## Features

### Student Profile Collection
- Name entry with empty-input validation
- Registration number and graduation year capture
- Graduation-year eligibility check (2025–2027)
- Attendance validation (0–100)
- Project completion and profile verification

### Daily Practice Tracking
- 7-day score entry with validation
- Absence tracking using `-1`
- Total score and average calculation
- Highest and lowest score tracking
- Daily score classification
- Pass/fail count
- Critical score detection

### Performance Analysis
- Average score calculation
- Eligibility checks
- Placement readiness evaluation
- Final performance report

## Python Concepts Used
- Variables and Data Types
- Type Conversion
- Conditional Statements
- Loops (`for`, `while`)
- `break` and `continue`
- Boolean Logic
- f-Strings
- Accumulators and Counters
- Flag Variables

## How to Run

1. Install Python 3.
2. Save the program as `main.py`.
3. Open a terminal in the project folder.
4. Run:

```bash
python main.py
```

5. Enter the required student details and 7-day practice scores.
6. View the generated PrepTrack report.

## Sample Output

```text
==================================================
           PREPTRACK REPORT
==================================================
Student Name          : venkatesh
Registration Number   : 22751A05D9
Graduation Year       : 2026
Attendance            : 97.0%

Attempted Days        : 7
Absent Days           : 0
Passed Days           : 7
Failed Days           : 0

Strong Days           : 6
Satisfactory Days     : 1
Needs Improvement Days: 0
Critical Days         : 0

Total Score           : 611
Average Score         : 87.29
Highest Score         : 99
Highest Score Day     : 6
Lowest Score          : 67
Lowest Score Day      : 3

Critical Score Found  : No
First Critical Day    : Not Applicable
First Critical Score  : Not Applicable

Final Status          : Ready for Mock Interview
Primary Blocker       : None
Next Action           : Proceed to the placement mock interview
```

## Individual Contribution
- Implemented input validation.
- Developed the 7-day practice tracking logic.
- Built the placement eligibility checks.
- Created the final performance report.
- Tested the application with different test cases.