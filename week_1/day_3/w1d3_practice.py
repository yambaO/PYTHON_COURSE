# ITP Week 1 Day 3 (In-Class) Practice

# Take an user's input and assign it to a variable named "student_grade_string"
student_grade_string = input ("Please enter your grade")

# The user input comes in as a string so we have to cast it to a Int to a variable named "student_grade_int"
student_grade_int = int(student_grade_string)

# Create an If statement with the appropriate Elif and Else statement for the following grading system.

"""
A : 90 - 100
B : 80 - 89
C : 70 - 79
D : 60 - 69
F : 0 - 59
"""

if student_grade_int <= 100 and student_grade_int >= 90 : print("grade A")
elif student_grade_int <= 89 and student_grade_int >= 80 : print("grade B")
elif student_grade_int <= 79 and student_grade_int >= 70 : print("grade c")
elif student_grade_int <= 69 and student_grade_int >= 60 : print("grade D")
else : print("grade F")
# elif student_grade_int <= 89 and student_grade_int >= 80


# Within each "block" print out the appropriate letter grade.