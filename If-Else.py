mark = int(input("Please provide the mark: "))
if mark > 35:
    print("Pass")
else:
    print("Fail")

#Next example
income = int(input("Please key in the income: "))
if income > 7000:
    print("Ineligible for Scholarship")
else:
    print("Eligible for Scholarship")

#Next example
num = int(input("Please key in the number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by 3 and 5")
else:
    print("Not Divisible by 3 and 5")

#Next example : Find if the number is even or odd
num = int(input("Please key in the number: "))
if num % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

#Next example : Find if a student has passed or failed
marks = int(input("Please provide the marks: "))
if marks >= 35:
    print("The student has passed")
else:
    print("The student has failed")

#Next example : If a number is positive or negative
num = int(input("Please key in the number: "))
if num > 0:
    print("The number is positive")
else:
    print("The number is negative")

#Next example : If a number is positive, negative or zero
num = int(input("Please key in the number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

