#Next example : Loan eligibility check based on age and salary - Nested if else
sal = int(input("Enter your salary: "))
age = int(input("Enter your age: "))
if sal >= 20000 or age <=25:
    print("You are eligible for the loan")
    loan_amt = int(input("Enter the loan amount: "))
    if loan_amt <= 50000:
        print("Loan approved")
    else:
        print("Maximum loan amount is 50000")
else:
    print("You are not eligible for the loan")

############################################################################################################
#Next problem : Get input for 5 marks, add all of them and find the average. If the average is less than 35,
#print Additional class is required, else print Good to go
############################################################################################################
m1 = int(input("Enter mark1 :"))
m2 = int(input("Enter mark2 :"))
m3 = int(input("Enter mark3 :"))
m4 = int(input("Enter mark4 :"))
m5 = int(input("Enter mark5 :"))
if (m1+m2+m3+m4+m5)/5 < 35:
    print("Additional Class if required")
else:
    print("You are good to go")

