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