# This program checks if a student can be admitted into a department
# It supports two departments: Computer Science and Mass Communication

# Ask student for the department they are applying to
department = input("Enter the department you are applying to (Computer Science or Mass Communication): ").strip().lower()

# Ask for the student's JAMB score
jamb_score = int(input("Enter your JAMB score: "))

# Ask how many key subjects the student got credit in (must be at least 5)
credits = int(input("How many key subjects did you get credit in? "))

# Ask if the student passed the interview (yes or no)
interview_passed = input("Did you pass the interview? (yes or no): ").strip().lower()

# We now check the conditions for each department

if department == "computer science":
    if jamb_score >= 250 and credits >= 5 and interview_passed == "yes":
        print("Congratulations! You are admitted into Computer Science.")
    else:
        print("Sorry, you did not meet the requirements for Computer Science.")

elif department == "mass communication":
    if jamb_score > 230 and credits >= 5 and interview_passed == "yes":
        print("Congratulations! You are admitted into Mass Communication.")
    else:
        print("Sorry, you did not meet the requirements for Mass Communication.")

else:
    print("Sorry, the department you entered is not available.")
