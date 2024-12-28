a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
for i in range(a+1,b):
    print(i)
print("############################################################################################################")
#Example 2 : Print the even numbers between 1 and 10
for i in range(1,11):
    if i%2==0:
        print(i)
print("############################################################################################################")
#Example 3 : Count the odd numbers between 1 and 10
count=0
for i in range(1,11):
    if i%2!=0:
        count+=1