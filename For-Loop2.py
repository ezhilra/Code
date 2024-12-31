
#Example 1 : Print the numbers between 2 numbers
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
for i in range(a + 1, b):
    print(i)
print("############################################################################################################")
#Example 2 : Print the even numbers between 1 and 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
print("############################################################################################################")
#Example 3 : Count the odd numbers between 1 and 10
count = 0
for i in range(1, 10):
    if i % 2 != 0:
        count += 1
print("The odd numbers between 1 and 10 are: ", count)

#Example 4 : Count the even numbers between 1 and 5
count = 0
for i in range(1, 5):
    if i % 2 == 0:
        count += 1
print("The even numbers between 1 and 5 are: ", count)

# Example 5 : Count and print the odd and even numbers between 1 and 10
count = 0
count1 = 0
for i in range(1, 11):
    if i % 2 == 0:
        count += 1
    else:
        count1 += 1
print("Even numbers count: ", count)
print("Odd numbers count: ", count1)

# Example 6 : Count and print the numbers between 1 and 100 that are divisible by 3 and 5
count = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        count += 1
        #print(i)
print("The number of numbers between 1 and 100, that are divisible by 3 and 5 are: ", count)

# Example 7 : Sum of first 5 natural numbers
sum = 0
for i in range(1, 6):
    sum += i
print("The sum of first 5 natural numbers is: ", sum)


# Example 8 : Take input for 10 natural numbers in a list, print the list and print the sum of the numbers
list = []
print("Enter 10 natural numbers: ")
for i in range(10):
    num=(int(input("Enter number " + str(i+1) + ": ")))
    list.append(num)
print("The numbers that have been added to the list are :",list)

sum = 0
for sum in list:
    sum += sum
print("The sum of the numbers is :", sum)
