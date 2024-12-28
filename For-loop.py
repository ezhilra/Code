for i in range(1,11):
    print(i,"x2=",i*2)
print("############################################################################################################")
#Example 2
for i in "Apple":
    print(i)
#Example 3 : For all non-negative integers i < n, print i^2
n = int(input("Enter the number: "))
for i in range(n):
    print(i**2)
# Example 4 : Check if a year is a leap year or not
year = int(input("Enter the year: "))
if year % 4 == 0:
    print("Leap year")

#Example 5: Take an input and print the consecutive numbers on the same line
n = int(input("Enter the number: "))
for i in range(1,n+1):
    print(i,end=" ")

