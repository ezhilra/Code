""""
i = 1
while(i<=5):
    print(i)
    i+=1

i = 10
while(i<=200):
    print(i,end=",")
    i+=10

i = 10
while(i>0):
    print(i,end=",")
    i-=1
"""

#While loop : Find the factorial of a number
num = int(input("Enter a number: "))
fact = 1
i = 1
while(i<=num):
    fact = fact * i
    i+=1
print("Factorial of",num,"is",fact)

x, y = map(int,input().split())
print(x * y)