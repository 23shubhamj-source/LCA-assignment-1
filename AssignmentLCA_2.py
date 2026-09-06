# Taking input from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# The Algorithm
if (a >= b) and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c

print("The largest number is:", largest)

# FAQ 2

marks = float(input("Enter marks in Math:: "))
if marks >= 90 and marks <= 100:
    grade =  "O"
elif marks >=80:
    grade = "A+"
elif marks >=70:
    grade = "A"
elif marks >=60:
    grade = "B"
elif marks >=50:
    grade = "C"
elif marks >=40:
    grade = "P"
else:
    grade = "F"

print("Grade Assigned: ", grade)