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

#Next example : If a student is below average, average, above average or distinction
mark = int(input("Please key in the mark: "))
if mark < 35:
    print("The student is a below average performer")
elif 35 <= mark < 60:
    print("The student is an average performer")
elif 60 <= mark < 75:
    print("The student is an above average performer")
elif 75 >= mark <=100:
    print("The student is a distinction holder")
else:
    print("Please provide a valid mark")

#Next Example : Building a mini calculator
user_input = int(input("Please choose the option 1. Add 2. Sub 3. Mul 4. Div:"))
num1 = int(input("Please provide the 1st number: "))
num2 = int(input("Please provide the 2nd number:"))
if user_input == 1 :
    print("The sum of the numbers is : ", num1 + num2)
elif user_input == 2 :
    print("The difference between the numbers is : ", num1 - num2)
elif user_input == 3 :
    print("The product of the numbers is : ", num1 * num2)
elif user_input == 4:
    print("The division of the numbers is : ", num1 / num2)
else:
    print("Please provide a valid input")


