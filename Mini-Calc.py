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
