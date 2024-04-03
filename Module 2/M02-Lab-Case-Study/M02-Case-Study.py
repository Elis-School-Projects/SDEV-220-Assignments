# Github Repo Link: https://github.com/Elis-School-Projects/M02-Lab-Case-Study

# Name: Eli Walters
# File Name: M02-Case-Study.py
# Description: This application will accept student names and GPAs and test 
# if the student qualifies for either the Dean's List or the Honor Roll

while True:
    lname = str(input("What is the student's last name? (ZZZ to quit): "))

    if lname == "ZZZ":
        break

    fname = str(input("What is the student's first name?: "))
    gpa = float(input("What is the student's GPA?: "))

    if gpa >= 3.5:
        print(f"{fname} {lname} has made the Dean's List!")
    elif gpa >= 3.25:
        print(f"{fname} {lname} has made the Honor Roll!")