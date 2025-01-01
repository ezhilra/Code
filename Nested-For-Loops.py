# Example 1 : Nested For Loop
for i in range(1, 5):
    for j in range(i):
        print("*",end="")
    print()
"""
# Example 2 : Nested For Loop with if condition
for i in range(1, 6):
    for j in range(1, 6):
        if i == j:
            print(i, j)
            
# Example 3 : Nested For Loop with if condition and break
for i in range(1, 6):
    for j in range(1, 6):
        if i == j:
            print(i, j)
            break
            
# Example 4 : Nested For Loop with if condition and continue
for i in range(1, 6):
    for j in range(1, 6):
        if i == j:
            print(i, j)
            continue
            
# Example 5 : Nested For Loop with if condition and pass
for i in range(1, 6):
    for j in range(1, 6):
        if i == j:
            print(i, j)
            pass
        
# Example 6 : Nested For Loop with if condition and pass
for i in range(1, 6):
    for j in range(1, 6):
        if i == j:
            print(i, j)
            pass
    print("End of Inner Loop")
print("End of Outer Loop")

# Example 7 : Nested For Loop with if condition and pass
for i in range(1, 6):
    for j in range(1, 6):
        if i == j:
            print(i, j)
            pass
        print("End of Inner Loop")
print("End of Outer Loop")
"""
