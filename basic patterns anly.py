# pattern first (using for loop)
# right angle
n= int(input("enter the no of rows you want to print"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
#inverted right angle
n= int(input("enter the no of rows you want to print"))
for i in range(n):
    for j in range(i,n):
        print("*",end="")
    print()
#image of  right angle 
n= int(input("enter the no of rows you want to print"))
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
# downward image of right angle
n= int(input("enter the no of rows you want to print"))
for  i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end="")
    print()
#next appreoch of this problem
n= int(input("enter the no of rows you want to print"))
for i in range(1,n+1):
    for j in range(i):
        print(" ",end="")
    for j in range(i,n+1):
        print("*",end="")
    print()
# pyramid shape
n= int(input("enter the no of rows you want to print"))
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()

# downward pyramid 
n= int(input("enter the no of rows you want to print"))
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end=" ")
    print()