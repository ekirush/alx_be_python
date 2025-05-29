'''
Drawing Patterns with Nested Loops
**********************************
Utilize while loops and nested for loops to draw a simple text-based pattern
'''
size =  int(input("Enter the size of the pattern: "))
row = 0
while size > row:
    for siz in range(size):
        print("*", end="")
    print()
    row +=1    
    