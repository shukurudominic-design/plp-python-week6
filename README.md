# PLP Python Week 3 Assignment

This repository contains my Python Week 3 assignment.

* `name_greeter.py` — asks for a full name, splits it into parts, and greets the user by their first name.
* `bug_hunt.py` — fixes three bugs in the provided Python program and includes three `# BUG:` comments explaining the fixes.
* `ticket_checker.py` — checks whether a person is an adult and displays the appropriate ticket price.
* `screenshots/` — contains screenshots showing each Python program running successfully.
* `README.md` — provides an overview of the assignment files and the Part B debugging experience.

### Part B Debugging

The bug that took me longest to find was the age calculation because `input()` returns the age as a string, so Python could not add `1` directly to it. The error message helped me understand that I needed to convert the input into an integer using `int()`.
# PLP Python Week 4 Assignment

This repository contains my Python Week 4 assignment covering conditional statements, validation, logical operators, and nested decisions.

### Files

* `grade_classifier.py` — Classifies a score from 0 to 100 into grades A, B, C, D, or F and validates the input.
* `eligibility_checker.py` — Checks whether a person is eligible to join a local coding club based on age and parental consent.
* `atm_menu.py` — Simulates a simple ATM withdrawal using a PIN, balance checking, and nested decisions.
* `screenshots/` — Contains screenshots showing the programs running with the required test cases.

### When is `elif` better than several separate `if` statements?

`elif` is better when you are checking several mutually exclusive conditions and only one result should be selected. It makes the code clearer and ensures that once one condition is true, the remaining conditions are not checked.
